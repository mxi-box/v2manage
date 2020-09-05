import asyncio
import ssl
import struct
import pymysql
import logger
from logger import logger as log
import signal

import userman
from netutil import readProtoFrom, writeProtoIn
import config
import command_pb2

class UserInMaster(userman.User):
	speedLimit = 0
	expireDate = None

class Client:
	socket_writer = None
	def __init__(self, token:str, name:str):
		self.token = token
		self.name = name

class ManagerInMaster(userman.UserManager):
	_mysql_db = None
	_clients = {}
	_server = None

	async def __loadFromDatabase(self):
		with self._mysql_db.cursor() as cursor:
			try:
				cursor.execute("CREATE TABLE user (tag VARCHAR(10), uuid CHAR(36), speedLimit INT)")
				cursor.execute("CREATE TABLE client (token CHAR(36), name TINYTEXT)")
				cursor.commit()
			except:
				pass
			cursor.execute("SELECT * FROM user")
			self._users.clear()
			for row in cursor.fetchall_unbuffered():
				user = UserInMaster()
				user.tag = row[0]
				user.uuid = row[1]
				user.speedLimit = row[2]
				self._users[user.tag] = user

			cursor.execute("SELECT * FROM client")
			self._clients.clear()
			for row in cursor.fetchall_unbuffered():
				client = Client(row[0], row[1])
				self._clients[client.token] = client

	async def connectAndInit(self, mysql_host:str, mysql_port:int, mysql_db:str, mysql_user:str, mysql_pw:str, host:str, port:int):
		log.info("connecting to mysql")
		self._mysql_db = pymysql.connections.Connection(
		host=mysql_host,
		port=mysql_port,
		user=mysql_user,
		passwd=mysql_pw,
		db=mysql_db,
		cursorclass=pymysql.cursors.SSCursor
		)

		await self.__loadFromDatabase()

		async def serverEcho(reader:asyncio.StreamReader, writer:asyncio.StreamWriter):
			peeraddress = writer.get_extra_info('peername')[:2]
			logger.logger.info("client at %s:%d is trying to connect" % peeraddress)

			handshake = command_pb2.ClientHandShakeRequest()
			await readProtoFrom(reader, handshake)

			response = command_pb2.ServerHandShakeResponse()
			client = self._clients[handshake.clientToken]
			if client is None:
				response.status = command_pb2.ServerHandShakeResponse.Status.INVAILD_TOKEN
				success = False
			elif client.socket_writer is not None:
				response.status = command_pb2.ServerHandShakeResponse.Status.UNAVAILABLE_TOKEN
				success = False
			else:
				response.status = command_pb2.ServerHandShakeResponse.Status.OK
				client.socket_writer = writer
				for user in self._users:
					user_info = response.users.add()
					user_info.tag = user.tag
					user_info.uuid = user.uuid
					user_info.speedLimit = user.speedLimit
				success = True

			writeProtoIn(writer, response)
			await writer.drain()
			if not success:
				writer.close()
				return
			logger.logger.warning("client at %s:%d connected successfully" % peeraddress)

		logger.logger.info("starting listener")

		ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
		ssl_context.load_cert_chain("./fullchain.pem", "./privkey.pem")
		self._server = await asyncio.start_server(serverEcho, host, port, ssl=ssl_context)
		logger.logger.warning("Initialized")

	async def close(self):
		self._server.close()
		self._mysql_db.close()
		
if __name__ == "__main__":


	def shutdown(*args):
		manager.close()
		loop.close()
		logger.logger.warning("shutdown")


	signal.signal(signal.SIGINT, shutdown)
	loop = asyncio.get_event_loop()
	manager = ManagerInMaster()
	loop.run_until_complete(manager.connectAndInit(
		mysql_host=config.MYSQL_HOST,
		mysql_port=config.MYSQL_PORT,
		mysql_db=config.MYSQL_DATABASE,
		mysql_user=config.MYSQL_USER,
		mysql_pw=config.MYSQL_PASSWORD,
		host=config.MASTER_HOST,
		port=config.MASTER_PORT
	))
	try:
		loop.run_forever()
	except KeyboardInterrupt:
		shutdown()
	
	




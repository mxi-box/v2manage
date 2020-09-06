import grpc
import asyncio
import ssl

import userman
from netutil import readProtoFrom, writeProtoIn
import config

import command_pb2
import v2ray.com.core.app.stats.command.command_pb2_grpc as stat_command_grpc
import v2ray.com.core.app.stats.command.command_pb2 as stat_command_pb2
import v2ray.com.core.app.proxyman.command.command_pb2 as handler_command_pb2
import v2ray.com.core.app.proxyman.command.command_pb2_grpc as handler_command_grpc
import v2ray.com.core.common.protocol.user_pb2 as user_pb2
import v2ray.com.core.common.serial.typed_message_pb2 as typed_message_pb2
import v2ray.com.core.proxy.vmess.account_pb2 as vmess_account_pb2

class UserInSlave(userman.User):
	speedLimit = 0

	def __init__(self, user_info:command_pb2.User):
		if user_info is None:
			return
		self.tag = user_info.tag
		self.uuid = user_info.uuid
		self.speedLimit = user_info.speedLimit


class ManagerInSlave(userman.UserManager):
	_isActive = False
	_slave_token = None
	_v2ray_channel = None
	_socket_reader = None
	socket_writer = None

	def __init__(self, token:str):
		self._slave_token = token

	async def __doMasterHandshake(self, initUsers:bool):
		handshake = command_pb2.ClientHandShakeRequest()
		handshake.clientToken = self._slave_token
		handshake.isQueryUsers = initUsers


		writeProtoIn(self.socket_writer, handshake)
		await self.socket_writer.drain()

		response = command_pb2.ServerHandShakeResponse()
		await readProtoFrom(self._socket_reader, response)
		if response.status != command_pb2.ServerHandShakeResponse.Status.OK:
			raise Exception('handshake failed') #TODO complete exception process

		self._isActive = True
		if initUsers:
			self._users.clear()
			for user_info in response.users:
				self._users[user_info.tag] = UserInSlave(user_info)

			for user in self._users.values():
				user_v2 = user_pb2.User(level = 0, email = user.tag)
				account_v2 = vmess_account_pb2.Account(uuid = user.uuid, alter_id = 32)
				user_v2.account = typed_message_pb2.TypedMessage(type='v2ray.core.proxy.vmess.Account', value=account_v2.SerializeToString())
				with handler_command_grpc.HandlerServiceStub(self._v2ray_channel) as stub:
					for inbound_tag in config.V2RAY_INBOUNDS: #TODO dont call config directly
						stub.AlterInbound(handler_command_pb2.AlterInboundRequest(
							tag=inbound_tag,
							operation=typed_message_pb2.TypedMessage(
								name='v2ray.core.app.proxyman.command.AddUserOperation',
								value=handler_command_pb2.AddUserOperation(
									user=user_v2
								)
							)
						))
				


	async def connectAndInit(self, v2ray_api_address:str, master_host:str, master_port:int, master_cert:str):
		self.master_host = master_host
		self.master_port = master_port
		self._v2ray_channel = grpc.insecure_channel(v2ray_api_address)

		self.ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=master_cert)
		self.ssl_context.check_hostname = False
		(self._socket_reader, self.socket_writer) = await asyncio.open_connection(master_host, master_port, ssl=self.ssl_context)

		await self.__doMasterHandshake(True)

	async def reconnect(self):
		(self._socket_reader, self.socket_writer) = await asyncio.open_connection(self.master_host, self.master_port, ssl=self.ssl_context)
		await self.__doMasterHandshake(False) #TODO add server command queue for network traffic jam


	async def watchCommand(self):
		if self._socket_reader is None:
			raise Exception("Manager is not initialized")
		while self._isActive:
			try:
				command = command_pb2.ServerUserCommand()
				await readProtoFrom(self._socket_reader, command)
				
				if command.type == command_pb2.ServerUserCommand.Type.UPDATE:
					self._users[command.user.tag] = UserInSlave(command.user)
				elif command.type == command_pb2.ServerUserCommand.Type.DELETE:
					self._users.pop(command.user.tag)
			except EOFError:
				await self.reconnect()

if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	manager = ManagerInSlave('89d4c782-641a-4bdc-82f7-c7245046a7cd')
	loop.run_until_complete(manager.connectAndInit(
		v2ray_api_address=config.V2RAY_API_ADDRESS,
		master_host=config.MASTER_HOST,
		master_port=config.MASTER_PORT,
		master_cert=None
	))
	try:
		loop.run_forever()
	except KeyboardInterrupt:
		pass

import asyncio
import struct

pb_length_struct = struct.Struct('!I')


def writeProtoIn(writer:asyncio.StreamWriter, protoBuf):
	protoBuf_string = protoBuf.SerializeToString()
	writer.write(pb_length_struct.pack(len(protoBuf_string)))
	writer.write(protoBuf_string)


async def readProtoFrom(reader:asyncio.StreamReader, protoBuf):
	(length,) = pb_length_struct.unpack(await reader.readexactly(4))
	protoBuf.ParseFromString(await reader.readexactly(length))
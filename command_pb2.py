# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='command.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rcommand.proto\"5\n\x04User\x12\x0b\n\x03tag\x18\x01 \x02(\t\x12\x0c\n\x04uuid\x18\x02 \x02(\t\x12\x12\n\nspeedLimit\x18\x03 \x01(\x05\"C\n\x16\x43lientHandShakeRequest\x12\x13\n\x0b\x63lientToken\x18\x01 \x02(\t\x12\x14\n\x0cisQueryUsers\x18\x02 \x02(\x08\"\x9c\x01\n\x17ServerHandShakeResponse\x12/\n\x06status\x18\x01 \x02(\x0e\x32\x1f.ServerHandShakeResponse.Status\x12\x14\n\x05users\x18\x02 \x03(\x0b\x32\x05.User\":\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\x11\n\rINVAILD_TOKEN\x10\x01\x12\x15\n\x11UNAVAILABLE_TOKEN\x10\x02\"`\n\x10SimpleUserReport\x12\x0b\n\x03tag\x18\x01 \x02(\t\x12\x12\n\nbyteUpload\x18\x02 \x02(\x03\x12\x14\n\x0c\x62yteDownload\x18\x03 \x02(\x03\x12\x15\n\rKiloPeakSpeed\x18\x04 \x02(\x03\"N\n\x11\x43lientUsersReport\x12\x11\n\ttimestamp\x18\x01 \x02(\x06\x12&\n\x0buserReports\x18\x02 \x03(\x0b\x32\x11.SimpleUserReport\"x\n\x11ServerUserCommand\x12%\n\x04type\x18\x01 \x02(\x0e\x32\x17.ServerUserCommand.Type\x12\x13\n\x04user\x18\x02 \x02(\x0b\x32\x05.User\"\'\n\x04Type\x12\n\n\x06UPDATE\x10\x00\x12\n\n\x06\x44\x45LETE\x10\x01\x12\x07\n\x03\x41\x44\x44\x10\x02'
)



_SERVERHANDSHAKERESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='ServerHandShakeResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVAILD_TOKEN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNAVAILABLE_TOKEN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=240,
  serialized_end=298,
)
_sym_db.RegisterEnumDescriptor(_SERVERHANDSHAKERESPONSE_STATUS)

_SERVERUSERCOMMAND_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='ServerUserCommand.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADD', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=559,
  serialized_end=598,
)
_sym_db.RegisterEnumDescriptor(_SERVERUSERCOMMAND_TYPE)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='User.tag', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='User.uuid', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speedLimit', full_name='User.speedLimit', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=70,
)


_CLIENTHANDSHAKEREQUEST = _descriptor.Descriptor(
  name='ClientHandShakeRequest',
  full_name='ClientHandShakeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientToken', full_name='ClientHandShakeRequest.clientToken', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isQueryUsers', full_name='ClientHandShakeRequest.isQueryUsers', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=139,
)


_SERVERHANDSHAKERESPONSE = _descriptor.Descriptor(
  name='ServerHandShakeResponse',
  full_name='ServerHandShakeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ServerHandShakeResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='users', full_name='ServerHandShakeResponse.users', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SERVERHANDSHAKERESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=298,
)


_SIMPLEUSERREPORT = _descriptor.Descriptor(
  name='SimpleUserReport',
  full_name='SimpleUserReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='SimpleUserReport.tag', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='byteUpload', full_name='SimpleUserReport.byteUpload', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='byteDownload', full_name='SimpleUserReport.byteDownload', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='KiloPeakSpeed', full_name='SimpleUserReport.KiloPeakSpeed', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=300,
  serialized_end=396,
)


_CLIENTUSERSREPORT = _descriptor.Descriptor(
  name='ClientUsersReport',
  full_name='ClientUsersReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ClientUsersReport.timestamp', index=0,
      number=1, type=6, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userReports', full_name='ClientUsersReport.userReports', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=398,
  serialized_end=476,
)


_SERVERUSERCOMMAND = _descriptor.Descriptor(
  name='ServerUserCommand',
  full_name='ServerUserCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ServerUserCommand.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='ServerUserCommand.user', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SERVERUSERCOMMAND_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=478,
  serialized_end=598,
)

_SERVERHANDSHAKERESPONSE.fields_by_name['status'].enum_type = _SERVERHANDSHAKERESPONSE_STATUS
_SERVERHANDSHAKERESPONSE.fields_by_name['users'].message_type = _USER
_SERVERHANDSHAKERESPONSE_STATUS.containing_type = _SERVERHANDSHAKERESPONSE
_CLIENTUSERSREPORT.fields_by_name['userReports'].message_type = _SIMPLEUSERREPORT
_SERVERUSERCOMMAND.fields_by_name['type'].enum_type = _SERVERUSERCOMMAND_TYPE
_SERVERUSERCOMMAND.fields_by_name['user'].message_type = _USER
_SERVERUSERCOMMAND_TYPE.containing_type = _SERVERUSERCOMMAND
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['ClientHandShakeRequest'] = _CLIENTHANDSHAKEREQUEST
DESCRIPTOR.message_types_by_name['ServerHandShakeResponse'] = _SERVERHANDSHAKERESPONSE
DESCRIPTOR.message_types_by_name['SimpleUserReport'] = _SIMPLEUSERREPORT
DESCRIPTOR.message_types_by_name['ClientUsersReport'] = _CLIENTUSERSREPORT
DESCRIPTOR.message_types_by_name['ServerUserCommand'] = _SERVERUSERCOMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'command_pb2'
  # @@protoc_insertion_point(class_scope:User)
  })
_sym_db.RegisterMessage(User)

ClientHandShakeRequest = _reflection.GeneratedProtocolMessageType('ClientHandShakeRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTHANDSHAKEREQUEST,
  '__module__' : 'command_pb2'
  # @@protoc_insertion_point(class_scope:ClientHandShakeRequest)
  })
_sym_db.RegisterMessage(ClientHandShakeRequest)

ServerHandShakeResponse = _reflection.GeneratedProtocolMessageType('ServerHandShakeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVERHANDSHAKERESPONSE,
  '__module__' : 'command_pb2'
  # @@protoc_insertion_point(class_scope:ServerHandShakeResponse)
  })
_sym_db.RegisterMessage(ServerHandShakeResponse)

SimpleUserReport = _reflection.GeneratedProtocolMessageType('SimpleUserReport', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLEUSERREPORT,
  '__module__' : 'command_pb2'
  # @@protoc_insertion_point(class_scope:SimpleUserReport)
  })
_sym_db.RegisterMessage(SimpleUserReport)

ClientUsersReport = _reflection.GeneratedProtocolMessageType('ClientUsersReport', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTUSERSREPORT,
  '__module__' : 'command_pb2'
  # @@protoc_insertion_point(class_scope:ClientUsersReport)
  })
_sym_db.RegisterMessage(ClientUsersReport)

ServerUserCommand = _reflection.GeneratedProtocolMessageType('ServerUserCommand', (_message.Message,), {
  'DESCRIPTOR' : _SERVERUSERCOMMAND,
  '__module__' : 'command_pb2'
  # @@protoc_insertion_point(class_scope:ServerUserCommand)
  })
_sym_db.RegisterMessage(ServerUserCommand)


# @@protoc_insertion_point(module_scope)

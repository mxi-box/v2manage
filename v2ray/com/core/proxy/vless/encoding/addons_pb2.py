# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/proxy/vless/encoding/addons.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/proxy/vless/encoding/addons.proto',
  package='v2ray.core.proxy.vless.encoding',
  syntax='proto3',
  serialized_options=b'\n#com.v2ray.core.proxy.vless.encodingP\001Z\010encoding\252\002\037V2Ray.Core.Proxy.Vless.Encoding',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n0v2ray.com/core/proxy/vless/encoding/addons.proto\x12\x1fv2ray.core.proxy.vless.encoding\"/\n\x06\x41\x64\x64ons\x12\x11\n\tScheduler\x18\x01 \x01(\t\x12\x12\n\nSchedulerV\x18\x02 \x01(\x0c\x42S\n#com.v2ray.core.proxy.vless.encodingP\x01Z\x08\x65ncoding\xaa\x02\x1fV2Ray.Core.Proxy.Vless.Encodingb\x06proto3'
)




_ADDONS = _descriptor.Descriptor(
  name='Addons',
  full_name='v2ray.core.proxy.vless.encoding.Addons',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Scheduler', full_name='v2ray.core.proxy.vless.encoding.Addons.Scheduler', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='SchedulerV', full_name='v2ray.core.proxy.vless.encoding.Addons.SchedulerV', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=132,
)

DESCRIPTOR.message_types_by_name['Addons'] = _ADDONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Addons = _reflection.GeneratedProtocolMessageType('Addons', (_message.Message,), {
  'DESCRIPTOR' : _ADDONS,
  '__module__' : 'v2ray.com.core.proxy.vless.encoding.addons_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.vless.encoding.Addons)
  })
_sym_db.RegisterMessage(Addons)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
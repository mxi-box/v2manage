# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/transport/internet/domainsocket/config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/transport/internet/domainsocket/config.proto',
  package='v2ray.core.transport.internet.domainsocket',
  syntax='proto3',
  serialized_options=b'\n.com.v2ray.core.transport.internet.domainsocketP\001Z\014domainsocket\252\002*V2Ray.Core.Transport.Internet.DomainSocket',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n;v2ray.com/core/transport/internet/domainsocket/config.proto\x12*v2ray.core.transport.internet.domainsocket\"(\n\x06\x43onfig\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x10\n\x08\x61\x62stract\x18\x02 \x01(\x08\x42m\n.com.v2ray.core.transport.internet.domainsocketP\x01Z\x0c\x64omainsocket\xaa\x02*V2Ray.Core.Transport.Internet.DomainSocketb\x06proto3'
)




_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.transport.internet.domainsocket.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='v2ray.core.transport.internet.domainsocket.Config.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='abstract', full_name='v2ray.core.transport.internet.domainsocket.Config.abstract', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=147,
)

DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'v2ray.com.core.transport.internet.domainsocket.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.domainsocket.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
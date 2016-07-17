# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RequestEnvelop.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import EnvelopData_pb2 as EnvelopData__pb2
from Enums import RequestEnums_pb2 as Enums_dot_RequestEnums__pb2

from EnvelopData_pb2 import *
from Enums.RequestEnums_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='RequestEnvelop.proto',
  package='Protos',
  syntax='proto3',
  serialized_pb=_b('\n\x14RequestEnvelop.proto\x12\x06Protos\x1a\x11\x45nvelopData.proto\x1a\x18\x45nums/RequestEnums.proto\"R\n\x0eRequestWrapper\x12/\n\x0crequest_type\x18\x01 \x01(\x0e\x32\x19.Protos.Enums.RequestType\x12\x0f\n\x07message\x18\x02 \x01(\x0c\"\xa2\x03\n\x0eRequestEnvelop\x12\x13\n\x0bstatus_code\x18\x01 \x01(\x05\x12\x0e\n\x06rpc_id\x18\x03 \x01(\x04\x12(\n\x08requests\x18\x04 \x03(\x0b\x32\x16.Protos.RequestWrapper\x12\x31\n\x08unknown6\x18\x06 \x01(\x0b\x32\x1f.Protos.RequestEnvelop.Unknown6\x12\x10\n\x08latitude\x18\x07 \x01(\x01\x12\x11\n\tlongitude\x18\x08 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\t \x01(\x01\x12#\n\tauth_info\x18\n \x01(\x0b\x32\x10.Protos.AuthInfo\x12\'\n\x0b\x61uth_ticket\x18\x0b \x01(\x0b\x32\x12.Protos.AuthTicket\x12\x11\n\tunknown12\x18\x0c \x01(\x03\x1av\n\x08Unknown6\x12\x10\n\x08unknown1\x18\x01 \x01(\x05\x12:\n\x08unknown2\x18\x02 \x01(\x0b\x32(.Protos.RequestEnvelop.Unknown6.Unknown2\x1a\x1c\n\x08Unknown2\x12\x10\n\x08unknown1\x18\x01 \x01(\x0cP\x00P\x01\x62\x06proto3')
  ,
  dependencies=[EnvelopData__pb2.DESCRIPTOR,Enums_dot_RequestEnums__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REQUESTWRAPPER = _descriptor.Descriptor(
  name='RequestWrapper',
  full_name='Protos.RequestWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_type', full_name='Protos.RequestWrapper.request_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='Protos.RequestWrapper.message', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=159,
)


_REQUESTENVELOP_UNKNOWN6_UNKNOWN2 = _descriptor.Descriptor(
  name='Unknown2',
  full_name='Protos.RequestEnvelop.Unknown6.Unknown2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='Protos.RequestEnvelop.Unknown6.Unknown2.unknown1', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=552,
  serialized_end=580,
)

_REQUESTENVELOP_UNKNOWN6 = _descriptor.Descriptor(
  name='Unknown6',
  full_name='Protos.RequestEnvelop.Unknown6',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='Protos.RequestEnvelop.Unknown6.unknown1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown2', full_name='Protos.RequestEnvelop.Unknown6.unknown2', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUESTENVELOP_UNKNOWN6_UNKNOWN2, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=462,
  serialized_end=580,
)

_REQUESTENVELOP = _descriptor.Descriptor(
  name='RequestEnvelop',
  full_name='Protos.RequestEnvelop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status_code', full_name='Protos.RequestEnvelop.status_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rpc_id', full_name='Protos.RequestEnvelop.rpc_id', index=1,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='requests', full_name='Protos.RequestEnvelop.requests', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown6', full_name='Protos.RequestEnvelop.unknown6', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='Protos.RequestEnvelop.latitude', index=4,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='Protos.RequestEnvelop.longitude', index=5,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='Protos.RequestEnvelop.altitude', index=6,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth_info', full_name='Protos.RequestEnvelop.auth_info', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth_ticket', full_name='Protos.RequestEnvelop.auth_ticket', index=8,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown12', full_name='Protos.RequestEnvelop.unknown12', index=9,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUESTENVELOP_UNKNOWN6, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=580,
)

_REQUESTWRAPPER.fields_by_name['request_type'].enum_type = Enums_dot_RequestEnums__pb2._REQUESTTYPE
_REQUESTENVELOP_UNKNOWN6_UNKNOWN2.containing_type = _REQUESTENVELOP_UNKNOWN6
_REQUESTENVELOP_UNKNOWN6.fields_by_name['unknown2'].message_type = _REQUESTENVELOP_UNKNOWN6_UNKNOWN2
_REQUESTENVELOP_UNKNOWN6.containing_type = _REQUESTENVELOP
_REQUESTENVELOP.fields_by_name['requests'].message_type = _REQUESTWRAPPER
_REQUESTENVELOP.fields_by_name['unknown6'].message_type = _REQUESTENVELOP_UNKNOWN6
_REQUESTENVELOP.fields_by_name['auth_info'].message_type = EnvelopData__pb2._AUTHINFO
_REQUESTENVELOP.fields_by_name['auth_ticket'].message_type = EnvelopData__pb2._AUTHTICKET
DESCRIPTOR.message_types_by_name['RequestWrapper'] = _REQUESTWRAPPER
DESCRIPTOR.message_types_by_name['RequestEnvelop'] = _REQUESTENVELOP

RequestWrapper = _reflection.GeneratedProtocolMessageType('RequestWrapper', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTWRAPPER,
  __module__ = 'RequestEnvelop_pb2'
  # @@protoc_insertion_point(class_scope:Protos.RequestWrapper)
  ))
_sym_db.RegisterMessage(RequestWrapper)

RequestEnvelop = _reflection.GeneratedProtocolMessageType('RequestEnvelop', (_message.Message,), dict(

  Unknown6 = _reflection.GeneratedProtocolMessageType('Unknown6', (_message.Message,), dict(

    Unknown2 = _reflection.GeneratedProtocolMessageType('Unknown2', (_message.Message,), dict(
      DESCRIPTOR = _REQUESTENVELOP_UNKNOWN6_UNKNOWN2,
      __module__ = 'RequestEnvelop_pb2'
      # @@protoc_insertion_point(class_scope:Protos.RequestEnvelop.Unknown6.Unknown2)
      ))
    ,
    DESCRIPTOR = _REQUESTENVELOP_UNKNOWN6,
    __module__ = 'RequestEnvelop_pb2'
    # @@protoc_insertion_point(class_scope:Protos.RequestEnvelop.Unknown6)
    ))
  ,
  DESCRIPTOR = _REQUESTENVELOP,
  __module__ = 'RequestEnvelop_pb2'
  # @@protoc_insertion_point(class_scope:Protos.RequestEnvelop)
  ))
_sym_db.RegisterMessage(RequestEnvelop)
_sym_db.RegisterMessage(RequestEnvelop.Unknown6)
_sym_db.RegisterMessage(RequestEnvelop.Unknown6.Unknown2)


# @@protoc_insertion_point(module_scope)
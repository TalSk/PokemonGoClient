# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: request.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='request.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rrequest.proto\"\xbf\x05\n\x0eRequestEnvelop\x12\x10\n\x08unknown1\x18\x01 \x01(\x05\x12\x0e\n\x06rpc_id\x18\x03 \x01(\x03\x12)\n\x08requests\x18\x04 \x03(\x0b\x32\x17.RequestEnvelop.Request\x12*\n\x08unknown6\x18\x06 \x01(\x0b\x32\x18.RequestEnvelop.Unknown6\x12\r\n\x05gps_x\x18\x07 \x01(\x06\x12\r\n\x05gps_y\x18\x08 \x01(\x06\x12\r\n\x05gps_z\x18\t \x01(\x06\x12&\n\x04\x61uth\x18\n \x01(\x0b\x32\x18.RequestEnvelop.AuthInfo\x12(\n\x05token\x18\x0b \x01(\x0b\x32\x19.RequestEnvelop.TokenData\x12\x12\n\ntime_delta\x18\x0c \x01(\x03\x1a(\n\x07Request\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\x0c\x1ao\n\x08Unknown6\x12\x10\n\x08unknown1\x18\x01 \x01(\x05\x12\x33\n\x08unknown2\x18\x02 \x01(\x0b\x32!.RequestEnvelop.Unknown6.Unknown2\x1a\x1c\n\x08Unknown2\x12\x10\n\x08unknown1\x18\x01 \x01(\x0c\x1a\x62\n\x08\x41uthInfo\x12\x10\n\x08provider\x18\x01 \x01(\t\x12+\n\x05token\x18\x02 \x01(\x0b\x32\x1c.RequestEnvelop.AuthInfo.JWT\x1a\x17\n\x03JWT\x12\x10\n\x08\x63ontents\x18\x01 \x01(\t\x1a:\n\tTokenData\x12\r\n\x05token\x18\x01 \x01(\x0c\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12\x0b\n\x03sig\x18\x03 \x01(\x0c\x1a\x66\n\x14GetMapObjectsRequest\x12\x0f\n\x07\x63\x65ll_id\x18\x01 \x01(\x0c\x12\x15\n\rsince_time_ms\x18\x02 \x01(\x0c\x12\x12\n\nplayer_lat\x18\x03 \x01(\x06\x12\x12\n\nplayer_lng\x18\x04 \x01(\x06\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REQUESTENVELOP_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='RequestEnvelop.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='RequestEnvelop.Request.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='RequestEnvelop.Request.message', index=1,
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
  serialized_start=304,
  serialized_end=344,
)

_REQUESTENVELOP_UNKNOWN6_UNKNOWN2 = _descriptor.Descriptor(
  name='Unknown2',
  full_name='RequestEnvelop.Unknown6.Unknown2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='RequestEnvelop.Unknown6.Unknown2.unknown1', index=0,
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
  serialized_start=429,
  serialized_end=457,
)

_REQUESTENVELOP_UNKNOWN6 = _descriptor.Descriptor(
  name='Unknown6',
  full_name='RequestEnvelop.Unknown6',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='RequestEnvelop.Unknown6.unknown1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown2', full_name='RequestEnvelop.Unknown6.unknown2', index=1,
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
  serialized_start=346,
  serialized_end=457,
)

_REQUESTENVELOP_AUTHINFO_JWT = _descriptor.Descriptor(
  name='JWT',
  full_name='RequestEnvelop.AuthInfo.JWT',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contents', full_name='RequestEnvelop.AuthInfo.JWT.contents', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=534,
  serialized_end=557,
)

_REQUESTENVELOP_AUTHINFO = _descriptor.Descriptor(
  name='AuthInfo',
  full_name='RequestEnvelop.AuthInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='provider', full_name='RequestEnvelop.AuthInfo.provider', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='token', full_name='RequestEnvelop.AuthInfo.token', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUESTENVELOP_AUTHINFO_JWT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=459,
  serialized_end=557,
)

_REQUESTENVELOP_TOKENDATA = _descriptor.Descriptor(
  name='TokenData',
  full_name='RequestEnvelop.TokenData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='RequestEnvelop.TokenData.token', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='RequestEnvelop.TokenData.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sig', full_name='RequestEnvelop.TokenData.sig', index=2,
      number=3, type=12, cpp_type=9, label=1,
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
  serialized_start=559,
  serialized_end=617,
)

_REQUESTENVELOP_GETMAPOBJECTSREQUEST = _descriptor.Descriptor(
  name='GetMapObjectsRequest',
  full_name='RequestEnvelop.GetMapObjectsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cell_id', full_name='RequestEnvelop.GetMapObjectsRequest.cell_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='since_time_ms', full_name='RequestEnvelop.GetMapObjectsRequest.since_time_ms', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_lat', full_name='RequestEnvelop.GetMapObjectsRequest.player_lat', index=2,
      number=3, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_lng', full_name='RequestEnvelop.GetMapObjectsRequest.player_lng', index=3,
      number=4, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=619,
  serialized_end=721,
)

_REQUESTENVELOP = _descriptor.Descriptor(
  name='RequestEnvelop',
  full_name='RequestEnvelop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='RequestEnvelop.unknown1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rpc_id', full_name='RequestEnvelop.rpc_id', index=1,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='requests', full_name='RequestEnvelop.requests', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown6', full_name='RequestEnvelop.unknown6', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gps_x', full_name='RequestEnvelop.gps_x', index=4,
      number=7, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gps_y', full_name='RequestEnvelop.gps_y', index=5,
      number=8, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gps_z', full_name='RequestEnvelop.gps_z', index=6,
      number=9, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth', full_name='RequestEnvelop.auth', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='token', full_name='RequestEnvelop.token', index=8,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_delta', full_name='RequestEnvelop.time_delta', index=9,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUESTENVELOP_REQUEST, _REQUESTENVELOP_UNKNOWN6, _REQUESTENVELOP_AUTHINFO, _REQUESTENVELOP_TOKENDATA, _REQUESTENVELOP_GETMAPOBJECTSREQUEST, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=721,
)

_REQUESTENVELOP_REQUEST.containing_type = _REQUESTENVELOP
_REQUESTENVELOP_UNKNOWN6_UNKNOWN2.containing_type = _REQUESTENVELOP_UNKNOWN6
_REQUESTENVELOP_UNKNOWN6.fields_by_name['unknown2'].message_type = _REQUESTENVELOP_UNKNOWN6_UNKNOWN2
_REQUESTENVELOP_UNKNOWN6.containing_type = _REQUESTENVELOP
_REQUESTENVELOP_AUTHINFO_JWT.containing_type = _REQUESTENVELOP_AUTHINFO
_REQUESTENVELOP_AUTHINFO.fields_by_name['token'].message_type = _REQUESTENVELOP_AUTHINFO_JWT
_REQUESTENVELOP_AUTHINFO.containing_type = _REQUESTENVELOP
_REQUESTENVELOP_TOKENDATA.containing_type = _REQUESTENVELOP
_REQUESTENVELOP_GETMAPOBJECTSREQUEST.containing_type = _REQUESTENVELOP
_REQUESTENVELOP.fields_by_name['requests'].message_type = _REQUESTENVELOP_REQUEST
_REQUESTENVELOP.fields_by_name['unknown6'].message_type = _REQUESTENVELOP_UNKNOWN6
_REQUESTENVELOP.fields_by_name['auth'].message_type = _REQUESTENVELOP_AUTHINFO
_REQUESTENVELOP.fields_by_name['token'].message_type = _REQUESTENVELOP_TOKENDATA
DESCRIPTOR.message_types_by_name['RequestEnvelop'] = _REQUESTENVELOP

RequestEnvelop = _reflection.GeneratedProtocolMessageType('RequestEnvelop', (_message.Message,), dict(

  Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
    DESCRIPTOR = _REQUESTENVELOP_REQUEST,
    __module__ = 'request_pb2'
    # @@protoc_insertion_point(class_scope:RequestEnvelop.Request)
    ))
  ,

  Unknown6 = _reflection.GeneratedProtocolMessageType('Unknown6', (_message.Message,), dict(

    Unknown2 = _reflection.GeneratedProtocolMessageType('Unknown2', (_message.Message,), dict(
      DESCRIPTOR = _REQUESTENVELOP_UNKNOWN6_UNKNOWN2,
      __module__ = 'request_pb2'
      # @@protoc_insertion_point(class_scope:RequestEnvelop.Unknown6.Unknown2)
      ))
    ,
    DESCRIPTOR = _REQUESTENVELOP_UNKNOWN6,
    __module__ = 'request_pb2'
    # @@protoc_insertion_point(class_scope:RequestEnvelop.Unknown6)
    ))
  ,

  AuthInfo = _reflection.GeneratedProtocolMessageType('AuthInfo', (_message.Message,), dict(

    JWT = _reflection.GeneratedProtocolMessageType('JWT', (_message.Message,), dict(
      DESCRIPTOR = _REQUESTENVELOP_AUTHINFO_JWT,
      __module__ = 'request_pb2'
      # @@protoc_insertion_point(class_scope:RequestEnvelop.AuthInfo.JWT)
      ))
    ,
    DESCRIPTOR = _REQUESTENVELOP_AUTHINFO,
    __module__ = 'request_pb2'
    # @@protoc_insertion_point(class_scope:RequestEnvelop.AuthInfo)
    ))
  ,

  TokenData = _reflection.GeneratedProtocolMessageType('TokenData', (_message.Message,), dict(
    DESCRIPTOR = _REQUESTENVELOP_TOKENDATA,
    __module__ = 'request_pb2'
    # @@protoc_insertion_point(class_scope:RequestEnvelop.TokenData)
    ))
  ,

  GetMapObjectsRequest = _reflection.GeneratedProtocolMessageType('GetMapObjectsRequest', (_message.Message,), dict(
    DESCRIPTOR = _REQUESTENVELOP_GETMAPOBJECTSREQUEST,
    __module__ = 'request_pb2'
    # @@protoc_insertion_point(class_scope:RequestEnvelop.GetMapObjectsRequest)
    ))
  ,
  DESCRIPTOR = _REQUESTENVELOP,
  __module__ = 'request_pb2'
  # @@protoc_insertion_point(class_scope:RequestEnvelop)
  ))
_sym_db.RegisterMessage(RequestEnvelop)
_sym_db.RegisterMessage(RequestEnvelop.Request)
_sym_db.RegisterMessage(RequestEnvelop.Unknown6)
_sym_db.RegisterMessage(RequestEnvelop.Unknown6.Unknown2)
_sym_db.RegisterMessage(RequestEnvelop.AuthInfo)
_sym_db.RegisterMessage(RequestEnvelop.AuthInfo.JWT)
_sym_db.RegisterMessage(RequestEnvelop.TokenData)
_sym_db.RegisterMessage(RequestEnvelop.GetMapObjectsRequest)


# @@protoc_insertion_point(module_scope)
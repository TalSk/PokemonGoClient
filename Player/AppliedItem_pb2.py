# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Player/AppliedItem.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Enums import PlayerEnums_pb2 as Enums_dot_PlayerEnums__pb2

from Enums.PlayerEnums_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='Player/AppliedItem.proto',
  package='Protos.Player',
  syntax='proto3',
  serialized_pb=_b('\n\x18Player/AppliedItem.proto\x12\rProtos.Player\x1a\x17\x45nums/PlayerEnums.proto\"\x9b\x01\n\x0b\x41ppliedItem\x12)\n\titem_type\x18\x01 \x01(\x0e\x32\x16.Protos.Enums.ItemType\x12:\n\x12item_type_category\x18\x02 \x01(\x0e\x32\x1e.Protos.Enums.ItemTypeCategory\x12\x11\n\texpire_ms\x18\x03 \x01(\x03\x12\x12\n\napplied_ms\x18\x04 \x01(\x03P\x00\x62\x06proto3')
  ,
  dependencies=[Enums_dot_PlayerEnums__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_APPLIEDITEM = _descriptor.Descriptor(
  name='AppliedItem',
  full_name='Protos.Player.AppliedItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_type', full_name='Protos.Player.AppliedItem.item_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_type_category', full_name='Protos.Player.AppliedItem.item_type_category', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expire_ms', full_name='Protos.Player.AppliedItem.expire_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='applied_ms', full_name='Protos.Player.AppliedItem.applied_ms', index=3,
      number=4, type=3, cpp_type=2, label=1,
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
  serialized_start=69,
  serialized_end=224,
)

_APPLIEDITEM.fields_by_name['item_type'].enum_type = Enums_dot_PlayerEnums__pb2._ITEMTYPE
_APPLIEDITEM.fields_by_name['item_type_category'].enum_type = Enums_dot_PlayerEnums__pb2._ITEMTYPECATEGORY
DESCRIPTOR.message_types_by_name['AppliedItem'] = _APPLIEDITEM

AppliedItem = _reflection.GeneratedProtocolMessageType('AppliedItem', (_message.Message,), dict(
  DESCRIPTOR = _APPLIEDITEM,
  __module__ = 'Player.AppliedItem_pb2'
  # @@protoc_insertion_point(class_scope:Protos.Player.AppliedItem)
  ))
_sym_db.RegisterMessage(AppliedItem)


# @@protoc_insertion_point(module_scope)
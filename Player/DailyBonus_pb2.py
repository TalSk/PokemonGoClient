# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Player/DailyBonus.proto

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
  name='Player/DailyBonus.proto',
  package='Protos.Player',
  syntax='proto3',
  serialized_pb=_b('\n\x17Player/DailyBonus.proto\x12\rProtos.Player\"c\n\nDailyBonus\x12#\n\x1bnext_collected_timestamp_ms\x18\x01 \x01(\x03\x12\x30\n(next_defender_bonus_collect_timestamp_ms\x18\x02 \x01(\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DAILYBONUS = _descriptor.Descriptor(
  name='DailyBonus',
  full_name='Protos.Player.DailyBonus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='next_collected_timestamp_ms', full_name='Protos.Player.DailyBonus.next_collected_timestamp_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_defender_bonus_collect_timestamp_ms', full_name='Protos.Player.DailyBonus.next_defender_bonus_collect_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=42,
  serialized_end=141,
)

DESCRIPTOR.message_types_by_name['DailyBonus'] = _DAILYBONUS

DailyBonus = _reflection.GeneratedProtocolMessageType('DailyBonus', (_message.Message,), dict(
  DESCRIPTOR = _DAILYBONUS,
  __module__ = 'Player.DailyBonus_pb2'
  # @@protoc_insertion_point(class_scope:Protos.Player.DailyBonus)
  ))
_sym_db.RegisterMessage(DailyBonus)


# @@protoc_insertion_point(module_scope)

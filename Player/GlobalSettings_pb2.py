# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Player/GlobalSettings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Map.Fort import FortSettings_pb2 as Map_dot_Fort_dot_FortSettings__pb2
from Map import MapSettings_pb2 as Map_dot_MapSettings__pb2
from Player import LevelSettings_pb2 as Player_dot_LevelSettings__pb2
from Player import InventorySettings_pb2 as Player_dot_InventorySettings__pb2

from Map.Fort.FortSettings_pb2 import *
from Map.MapSettings_pb2 import *
from Player.LevelSettings_pb2 import *
from Player.InventorySettings_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='Player/GlobalSettings.proto',
  package='Protos.Player',
  syntax='proto3',
  serialized_pb=_b('\n\x1bPlayer/GlobalSettings.proto\x12\rProtos.Player\x1a\x1bMap/Fort/FortSettings.proto\x1a\x15Map/MapSettings.proto\x1a\x1aPlayer/LevelSettings.proto\x1a\x1ePlayer/InventorySettings.proto\"\xe5\x01\n\x0eGlobalSettings\x12+\n\x04\x66ort\x18\x02 \x01(\x0b\x32\x1d.Protos.Map.Fort.FortSettings\x12$\n\x03map\x18\x03 \x01(\x0b\x32\x17.Protos.Map.MapSettings\x12+\n\x05level\x18\x04 \x01(\x0b\x32\x1c.Protos.Player.LevelSettings\x12\x33\n\tinventory\x18\x05 \x01(\x0b\x32 .Protos.Player.InventorySettings\x12\x1e\n\x16minimum_client_version\x18\x06 \x01(\tP\x00P\x01P\x02P\x03\x62\x06proto3')
  ,
  dependencies=[Map_dot_Fort_dot_FortSettings__pb2.DESCRIPTOR,Map_dot_MapSettings__pb2.DESCRIPTOR,Player_dot_LevelSettings__pb2.DESCRIPTOR,Player_dot_InventorySettings__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GLOBALSETTINGS = _descriptor.Descriptor(
  name='GlobalSettings',
  full_name='Protos.Player.GlobalSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort', full_name='Protos.Player.GlobalSettings.fort', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map', full_name='Protos.Player.GlobalSettings.map', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='Protos.Player.GlobalSettings.level', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inventory', full_name='Protos.Player.GlobalSettings.inventory', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minimum_client_version', full_name='Protos.Player.GlobalSettings.minimum_client_version', index=4,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=159,
  serialized_end=388,
)

_GLOBALSETTINGS.fields_by_name['fort'].message_type = Map_dot_Fort_dot_FortSettings__pb2._FORTSETTINGS
_GLOBALSETTINGS.fields_by_name['map'].message_type = Map_dot_MapSettings__pb2._MAPSETTINGS
_GLOBALSETTINGS.fields_by_name['level'].message_type = Player_dot_LevelSettings__pb2._LEVELSETTINGS
_GLOBALSETTINGS.fields_by_name['inventory'].message_type = Player_dot_InventorySettings__pb2._INVENTORYSETTINGS
DESCRIPTOR.message_types_by_name['GlobalSettings'] = _GLOBALSETTINGS

GlobalSettings = _reflection.GeneratedProtocolMessageType('GlobalSettings', (_message.Message,), dict(
  DESCRIPTOR = _GLOBALSETTINGS,
  __module__ = 'Player.GlobalSettings_pb2'
  # @@protoc_insertion_point(class_scope:Protos.Player.GlobalSettings)
  ))
_sym_db.RegisterMessage(GlobalSettings)


# @@protoc_insertion_point(module_scope)

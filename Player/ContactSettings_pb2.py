# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Player/ContactSettings.proto

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
  name='Player/ContactSettings.proto',
  package='Protos.Player',
  syntax='proto3',
  serialized_pb=_b('\n\x1cPlayer/ContactSettings.proto\x12\rProtos.Player\"Q\n\x0f\x43ontactSettings\x12\x1d\n\x15send_marketing_emails\x18\x01 \x01(\x08\x12\x1f\n\x17send_push_notifications\x18\x02 \x01(\x08\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CONTACTSETTINGS = _descriptor.Descriptor(
  name='ContactSettings',
  full_name='Protos.Player.ContactSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='send_marketing_emails', full_name='Protos.Player.ContactSettings.send_marketing_emails', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='send_push_notifications', full_name='Protos.Player.ContactSettings.send_push_notifications', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=47,
  serialized_end=128,
)

DESCRIPTOR.message_types_by_name['ContactSettings'] = _CONTACTSETTINGS

ContactSettings = _reflection.GeneratedProtocolMessageType('ContactSettings', (_message.Message,), dict(
  DESCRIPTOR = _CONTACTSETTINGS,
  __module__ = 'Player.ContactSettings_pb2'
  # @@protoc_insertion_point(class_scope:Protos.Player.ContactSettings)
  ))
_sym_db.RegisterMessage(ContactSettings)


# @@protoc_insertion_point(module_scope)

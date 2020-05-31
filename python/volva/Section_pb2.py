# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Section.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import Block_pb2 as Block__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Section.proto',
  package='volva.proto',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\rSection.proto\x12\x0bvolva.proto\x1a\x0b\x42lock.proto\"\xc8\x01\n\x07Section\x12\n\n\x02id\x18\x01 \x02(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\'\n\x06\x62locks\x18\x03 \x03(\x0b\x32\x17.volva.proto.BlockGroup\x12\'\n\x04kind\x18\x04 \x03(\x0e\x32\x19.volva.proto.Section.Kind\"Q\n\x04Kind\x12\x0c\n\x08Readable\x10\x00\x12\x0c\n\x08Writable\x10\x01\x12\x0e\n\nExecutable\x10\x02\x12\x0c\n\x08Loadable\x10\x03\x12\x0f\n\x0bInitialised\x10\x04'
  ,
  dependencies=[Block__pb2.DESCRIPTOR,])



_SECTION_KIND = _descriptor.EnumDescriptor(
  name='Kind',
  full_name='volva.proto.Section.Kind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Readable', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Writable', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Executable', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Loadable', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Initialised', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=163,
  serialized_end=244,
)
_sym_db.RegisterEnumDescriptor(_SECTION_KIND)


_SECTION = _descriptor.Descriptor(
  name='Section',
  full_name='volva.proto.Section',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='volva.proto.Section.id', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='volva.proto.Section.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blocks', full_name='volva.proto.Section.blocks', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kind', full_name='volva.proto.Section.kind', index=3,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SECTION_KIND,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=244,
)

_SECTION.fields_by_name['blocks'].message_type = Block__pb2._BLOCKGROUP
_SECTION.fields_by_name['kind'].enum_type = _SECTION_KIND
_SECTION_KIND.containing_type = _SECTION
DESCRIPTOR.message_types_by_name['Section'] = _SECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Section = _reflection.GeneratedProtocolMessageType('Section', (_message.Message,), {
  'DESCRIPTOR' : _SECTION,
  '__module__' : 'Section_pb2'
  # @@protoc_insertion_point(class_scope:volva.proto.Section)
  })
_sym_db.RegisterMessage(Section)


# @@protoc_insertion_point(module_scope)
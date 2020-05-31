# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Module.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import Machine_pb2 as Machine__pb2
from . import Section_pb2 as Section__pb2
from . import Symbol_pb2 as Symbol__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Module.proto',
  package='volva.proto',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x0cModule.proto\x12\x0bvolva.proto\x1a\rMachine.proto\x1a\rSection.proto\x1a\x0cSymbol.proto\"\xbe\x01\n\x06Module\x12\n\n\x02id\x18\x01 \x02(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\'\n\x04\x61rch\x18\x03 \x02(\x0e\x32\x19.volva.proto.Architecture\x12#\n\x06\x65ndian\x18\x04 \x02(\x0e\x32\x13.volva.proto.Endian\x12$\n\x07symbols\x18\x05 \x03(\x0b\x32\x13.volva.proto.Symbol\x12&\n\x08sections\x18\x06 \x03(\x0b\x32\x14.volva.proto.Section'
  ,
  dependencies=[Machine__pb2.DESCRIPTOR,Section__pb2.DESCRIPTOR,Symbol__pb2.DESCRIPTOR,])




_MODULE = _descriptor.Descriptor(
  name='Module',
  full_name='volva.proto.Module',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='volva.proto.Module.id', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='volva.proto.Module.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arch', full_name='volva.proto.Module.arch', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endian', full_name='volva.proto.Module.endian', index=3,
      number=4, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbols', full_name='volva.proto.Module.symbols', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sections', full_name='volva.proto.Module.sections', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=74,
  serialized_end=264,
)

_MODULE.fields_by_name['arch'].enum_type = Machine__pb2._ARCHITECTURE
_MODULE.fields_by_name['endian'].enum_type = Machine__pb2._ENDIAN
_MODULE.fields_by_name['symbols'].message_type = Symbol__pb2._SYMBOL
_MODULE.fields_by_name['sections'].message_type = Section__pb2._SECTION
DESCRIPTOR.message_types_by_name['Module'] = _MODULE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Module = _reflection.GeneratedProtocolMessageType('Module', (_message.Message,), {
  'DESCRIPTOR' : _MODULE,
  '__module__' : 'Module_pb2'
  # @@protoc_insertion_point(class_scope:volva.proto.Module)
  })
_sym_db.RegisterMessage(Module)


# @@protoc_insertion_point(module_scope)
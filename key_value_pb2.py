# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: key_value.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='key_value.proto',
  package='key_value',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fkey_value.proto\x12\tkey_value\"*\n\x0cPairKeyValue\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t\"\x1c\n\x0bInsertReply\x12\r\n\x05reply\x18\x01 \x01(\x05\"\x12\n\x03Key\x12\x0b\n\x03key\x18\x01 \x01(\x05\"\x16\n\x05Value\x12\r\n\x05value\x18\x01 \x01(\t\"\x17\n\x06\x46inish\x12\r\n\x05reply\x18\x01 \x01(\t\"\x0e\n\x0c\x66inishParams2\xa9\x01\n\x07Storage\x12;\n\x06insert\x12\x17.key_value.PairKeyValue\x1a\x16.key_value.InsertReply\"\x00\x12)\n\x03get\x12\x0e.key_value.Key\x1a\x10.key_value.Value\"\x00\x12\x36\n\x06\x66inish\x12\x17.key_value.finishParams\x1a\x11.key_value.Finish\"\x00\x62\x06proto3'
)




_PAIRKEYVALUE = _descriptor.Descriptor(
  name='PairKeyValue',
  full_name='key_value.PairKeyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='key_value.PairKeyValue.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='key_value.PairKeyValue.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=30,
  serialized_end=72,
)


_INSERTREPLY = _descriptor.Descriptor(
  name='InsertReply',
  full_name='key_value.InsertReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply', full_name='key_value.InsertReply.reply', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=74,
  serialized_end=102,
)


_KEY = _descriptor.Descriptor(
  name='Key',
  full_name='key_value.Key',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='key_value.Key.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=104,
  serialized_end=122,
)


_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='key_value.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='key_value.Value.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=124,
  serialized_end=146,
)


_FINISH = _descriptor.Descriptor(
  name='Finish',
  full_name='key_value.Finish',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply', full_name='key_value.Finish.reply', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=148,
  serialized_end=171,
)


_FINISHPARAMS = _descriptor.Descriptor(
  name='finishParams',
  full_name='key_value.finishParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=173,
  serialized_end=187,
)

DESCRIPTOR.message_types_by_name['PairKeyValue'] = _PAIRKEYVALUE
DESCRIPTOR.message_types_by_name['InsertReply'] = _INSERTREPLY
DESCRIPTOR.message_types_by_name['Key'] = _KEY
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['Finish'] = _FINISH
DESCRIPTOR.message_types_by_name['finishParams'] = _FINISHPARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PairKeyValue = _reflection.GeneratedProtocolMessageType('PairKeyValue', (_message.Message,), {
  'DESCRIPTOR' : _PAIRKEYVALUE,
  '__module__' : 'key_value_pb2'
  # @@protoc_insertion_point(class_scope:key_value.PairKeyValue)
  })
_sym_db.RegisterMessage(PairKeyValue)

InsertReply = _reflection.GeneratedProtocolMessageType('InsertReply', (_message.Message,), {
  'DESCRIPTOR' : _INSERTREPLY,
  '__module__' : 'key_value_pb2'
  # @@protoc_insertion_point(class_scope:key_value.InsertReply)
  })
_sym_db.RegisterMessage(InsertReply)

Key = _reflection.GeneratedProtocolMessageType('Key', (_message.Message,), {
  'DESCRIPTOR' : _KEY,
  '__module__' : 'key_value_pb2'
  # @@protoc_insertion_point(class_scope:key_value.Key)
  })
_sym_db.RegisterMessage(Key)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'key_value_pb2'
  # @@protoc_insertion_point(class_scope:key_value.Value)
  })
_sym_db.RegisterMessage(Value)

Finish = _reflection.GeneratedProtocolMessageType('Finish', (_message.Message,), {
  'DESCRIPTOR' : _FINISH,
  '__module__' : 'key_value_pb2'
  # @@protoc_insertion_point(class_scope:key_value.Finish)
  })
_sym_db.RegisterMessage(Finish)

finishParams = _reflection.GeneratedProtocolMessageType('finishParams', (_message.Message,), {
  'DESCRIPTOR' : _FINISHPARAMS,
  '__module__' : 'key_value_pb2'
  # @@protoc_insertion_point(class_scope:key_value.finishParams)
  })
_sym_db.RegisterMessage(finishParams)



_STORAGE = _descriptor.ServiceDescriptor(
  name='Storage',
  full_name='key_value.Storage',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=190,
  serialized_end=359,
  methods=[
  _descriptor.MethodDescriptor(
    name='insert',
    full_name='key_value.Storage.insert',
    index=0,
    containing_service=None,
    input_type=_PAIRKEYVALUE,
    output_type=_INSERTREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='key_value.Storage.get',
    index=1,
    containing_service=None,
    input_type=_KEY,
    output_type=_VALUE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='finish',
    full_name='key_value.Storage.finish',
    index=2,
    containing_service=None,
    input_type=_FINISHPARAMS,
    output_type=_FINISH,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STORAGE)

DESCRIPTOR.services_by_name['Storage'] = _STORAGE

# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: service.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\"$\n\x0eMessageRequest\x12\x12\n\nmessagecom\x18\x01 \x01(\t\"%\n\x0fMessageResponse\x12\x12\n\nmessagecom\x18\x01 \x01(\t\"\x07\n\x05\x45mpty2g\n\x0eMessageService\x12&\n\x0bSendMessage\x12\x0f.MessageRequest\x1a\x06.Empty\x12-\n\x0fReceiveMessages\x12\x06.Empty\x1a\x10.MessageResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MESSAGEREQUEST']._serialized_start=17
  _globals['_MESSAGEREQUEST']._serialized_end=53
  _globals['_MESSAGERESPONSE']._serialized_start=55
  _globals['_MESSAGERESPONSE']._serialized_end=92
  _globals['_EMPTY']._serialized_start=94
  _globals['_EMPTY']._serialized_end=101
  _globals['_MESSAGESERVICE']._serialized_start=103
  _globals['_MESSAGESERVICE']._serialized_end=206
# @@protoc_insertion_point(module_scope)

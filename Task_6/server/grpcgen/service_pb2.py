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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\x12\x07service\"\x9f\x01\n\x0bUserRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06nombre\x18\x02 \x01(\t\x12\x10\n\x08\x61pellido\x18\x03 \x01(\t\x12\x0e\n\x06\x63orreo\x18\x04 \x01(\t\x12\x18\n\x10\x66\x65\x63ha_nacimiento\x18\x05 \x01(\t\x12\x10\n\x08semestre\x18\x06 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x07 \x01(\t\x12\x16\n\x0e\x63orrelation_id\x18\x08 \x01(\t\"\x1b\n\rUserIdRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"x\n\x0cUserResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06nombre\x18\x02 \x01(\t\x12\x10\n\x08\x61pellido\x18\x03 \x01(\t\x12\x0e\n\x06\x63orreo\x18\x04 \x01(\t\x12\x18\n\x10\x66\x65\x63ha_nacimiento\x18\x05 \x01(\t\x12\x10\n\x08semestre\x18\x06 \x01(\t\"\x07\n\x05\x45mpty\"[\n\rActionMessage\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\x12\x16\n\x0e\x63orrelation_id\x18\x02 \x01(\t\x12\"\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x14.service.UserRequest2\xb9\x01\n\x0bUserService\x12\x33\n\x0bSendMessage\x12\x14.service.UserRequest\x1a\x0e.service.Empty\x12;\n\x0fReceiveMessages\x12\x0e.service.Empty\x1a\x16.service.ActionMessage0\x01\x12\x38\n\x07GetUser\x12\x16.service.UserIdRequest\x1a\x15.service.UserResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USERREQUEST']._serialized_start=27
  _globals['_USERREQUEST']._serialized_end=186
  _globals['_USERIDREQUEST']._serialized_start=188
  _globals['_USERIDREQUEST']._serialized_end=215
  _globals['_USERRESPONSE']._serialized_start=217
  _globals['_USERRESPONSE']._serialized_end=337
  _globals['_EMPTY']._serialized_start=339
  _globals['_EMPTY']._serialized_end=346
  _globals['_ACTIONMESSAGE']._serialized_start=348
  _globals['_ACTIONMESSAGE']._serialized_end=439
  _globals['_USERSERVICE']._serialized_start=442
  _globals['_USERSERVICE']._serialized_end=627
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: actuators_services.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x61\x63tuators_services.proto\"\x07\n\x05\x45mpty\"!\n\x0fTempPowerStatus\x12\x0e\n\x06status\x18\x01 \x01(\t\"\"\n\x0bTempRequest\x12\x13\n\x0btempCelsius\x18\x01 \x01(\x01\"#\n\x0cTempResponse\x12\x13\n\x0btempCelsius\x18\x01 \x01(\x01\x32\x63\n\x02\x41\x43\x12)\n\x0bswitchPower\x12\x06.Empty\x1a\x10.TempPowerStatus\"\x00\x12\x32\n\x11\x63hangeTemperature\x12\x0c.TempRequest\x1a\r.TempResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'actuators_services_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=28
  _EMPTY._serialized_end=35
  _TEMPPOWERSTATUS._serialized_start=37
  _TEMPPOWERSTATUS._serialized_end=70
  _TEMPREQUEST._serialized_start=72
  _TEMPREQUEST._serialized_end=106
  _TEMPRESPONSE._serialized_start=108
  _TEMPRESPONSE._serialized_end=143
  _AC._serialized_start=145
  _AC._serialized_end=244
# @@protoc_insertion_point(module_scope)

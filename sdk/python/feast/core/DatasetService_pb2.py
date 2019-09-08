# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/core/DatasetService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/core/DatasetService.proto',
  package='feast.core',
  syntax='proto3',
  serialized_options=_b('\n\nfeast.coreB\023DatasetServiceProtoZ5github.com/gojek/feast/protos/generated/go/feast/core'),
  serialized_pb=_b('\n\x1f\x66\x65\x61st/core/DatasetService.proto\x12\nfeast.core\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa4\x03\n\x13\x44\x61tasetServiceTypes\x1a\xc5\x02\n\x14\x43reateDatasetRequest\x12*\n\nfeatureSet\x18\x01 \x01(\x0b\x32\x16.feast.core.FeatureSet\x12-\n\tstartDate\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07\x65ndDate\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05limit\x18\x04 \x01(\x03\x12\x12\n\nnamePrefix\x18\x05 \x01(\t\x12R\n\x07\x66ilters\x18\x06 \x03(\x0b\x32\x41.feast.core.DatasetServiceTypes.CreateDatasetRequest.FiltersEntry\x1a.\n\x0c\x46iltersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x45\n\x15\x43reateDatasetResponse\x12,\n\x0b\x64\x61tasetInfo\x18\x01 \x01(\x0b\x32\x17.feast.core.DatasetInfo\"4\n\nFeatureSet\x12\x12\n\nentityName\x18\x01 \x01(\t\x12\x12\n\nfeatureIds\x18\x02 \x03(\t\"-\n\x0b\x44\x61tasetInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08tableUrl\x18\x02 \x01(\t2\x90\x01\n\x0e\x44\x61tasetService\x12~\n\rCreateDataset\x12\x34.feast.core.DatasetServiceTypes.CreateDatasetRequest\x1a\x35.feast.core.DatasetServiceTypes.CreateDatasetResponse\"\x00\x42X\n\nfeast.coreB\x13\x44\x61tasetServiceProtoZ5github.com/gojek/feast/protos/generated/go/feast/coreb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_DATASETSERVICETYPES_CREATEDATASETREQUEST_FILTERSENTRY = _descriptor.Descriptor(
  name='FiltersEntry',
  full_name='feast.core.DatasetServiceTypes.CreateDatasetRequest.FiltersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='feast.core.DatasetServiceTypes.CreateDatasetRequest.FiltersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='feast.core.DatasetServiceTypes.CreateDatasetRequest.FiltersEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=384,
  serialized_end=430,
)

_DATASETSERVICETYPES_CREATEDATASETREQUEST = _descriptor.Descriptor(
  name='CreateDatasetRequest',
  full_name='feast.core.DatasetServiceTypes.CreateDatasetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='featureSet', full_name='feast.core.DatasetServiceTypes.CreateDatasetRequest.featureSet', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startDate', full_name='feast.core.DatasetServiceTypes.CreateDatasetRequest.startDate', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endDate', full_name='feast.core.DatasetServiceTypes.CreateDatasetRequest.endDate', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='feast.core.DatasetServiceTypes.CreateDatasetRequest.limit', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='namePrefix', full_name='feast.core.DatasetServiceTypes.CreateDatasetRequest.namePrefix', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filters', full_name='feast.core.DatasetServiceTypes.CreateDatasetRequest.filters', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DATASETSERVICETYPES_CREATEDATASETREQUEST_FILTERSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=430,
)

_DATASETSERVICETYPES_CREATEDATASETRESPONSE = _descriptor.Descriptor(
  name='CreateDatasetResponse',
  full_name='feast.core.DatasetServiceTypes.CreateDatasetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='datasetInfo', full_name='feast.core.DatasetServiceTypes.CreateDatasetResponse.datasetInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=432,
  serialized_end=501,
)

_DATASETSERVICETYPES = _descriptor.Descriptor(
  name='DatasetServiceTypes',
  full_name='feast.core.DatasetServiceTypes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_DATASETSERVICETYPES_CREATEDATASETREQUEST, _DATASETSERVICETYPES_CREATEDATASETRESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=501,
)


_FEATURESET = _descriptor.Descriptor(
  name='FeatureSet',
  full_name='feast.core.FeatureSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entityName', full_name='feast.core.FeatureSet.entityName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='featureIds', full_name='feast.core.FeatureSet.featureIds', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=503,
  serialized_end=555,
)


_DATASETINFO = _descriptor.Descriptor(
  name='DatasetInfo',
  full_name='feast.core.DatasetInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='feast.core.DatasetInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tableUrl', full_name='feast.core.DatasetInfo.tableUrl', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=557,
  serialized_end=602,
)

_DATASETSERVICETYPES_CREATEDATASETREQUEST_FILTERSENTRY.containing_type = _DATASETSERVICETYPES_CREATEDATASETREQUEST
_DATASETSERVICETYPES_CREATEDATASETREQUEST.fields_by_name['featureSet'].message_type = _FEATURESET
_DATASETSERVICETYPES_CREATEDATASETREQUEST.fields_by_name['startDate'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DATASETSERVICETYPES_CREATEDATASETREQUEST.fields_by_name['endDate'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DATASETSERVICETYPES_CREATEDATASETREQUEST.fields_by_name['filters'].message_type = _DATASETSERVICETYPES_CREATEDATASETREQUEST_FILTERSENTRY
_DATASETSERVICETYPES_CREATEDATASETREQUEST.containing_type = _DATASETSERVICETYPES
_DATASETSERVICETYPES_CREATEDATASETRESPONSE.fields_by_name['datasetInfo'].message_type = _DATASETINFO
_DATASETSERVICETYPES_CREATEDATASETRESPONSE.containing_type = _DATASETSERVICETYPES
DESCRIPTOR.message_types_by_name['DatasetServiceTypes'] = _DATASETSERVICETYPES
DESCRIPTOR.message_types_by_name['FeatureSet'] = _FEATURESET
DESCRIPTOR.message_types_by_name['DatasetInfo'] = _DATASETINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DatasetServiceTypes = _reflection.GeneratedProtocolMessageType('DatasetServiceTypes', (_message.Message,), dict(

  CreateDatasetRequest = _reflection.GeneratedProtocolMessageType('CreateDatasetRequest', (_message.Message,), dict(

    FiltersEntry = _reflection.GeneratedProtocolMessageType('FiltersEntry', (_message.Message,), dict(
      DESCRIPTOR = _DATASETSERVICETYPES_CREATEDATASETREQUEST_FILTERSENTRY,
      __module__ = 'feast.core.DatasetService_pb2'
      # @@protoc_insertion_point(class_scope:feast.core.DatasetServiceTypes.CreateDatasetRequest.FiltersEntry)
      ))
    ,
    DESCRIPTOR = _DATASETSERVICETYPES_CREATEDATASETREQUEST,
    __module__ = 'feast.core.DatasetService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.DatasetServiceTypes.CreateDatasetRequest)
    ))
  ,

  CreateDatasetResponse = _reflection.GeneratedProtocolMessageType('CreateDatasetResponse', (_message.Message,), dict(
    DESCRIPTOR = _DATASETSERVICETYPES_CREATEDATASETRESPONSE,
    __module__ = 'feast.core.DatasetService_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.DatasetServiceTypes.CreateDatasetResponse)
    ))
  ,
  DESCRIPTOR = _DATASETSERVICETYPES,
  __module__ = 'feast.core.DatasetService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.DatasetServiceTypes)
  ))
_sym_db.RegisterMessage(DatasetServiceTypes)
_sym_db.RegisterMessage(DatasetServiceTypes.CreateDatasetRequest)
_sym_db.RegisterMessage(DatasetServiceTypes.CreateDatasetRequest.FiltersEntry)
_sym_db.RegisterMessage(DatasetServiceTypes.CreateDatasetResponse)

FeatureSet = _reflection.GeneratedProtocolMessageType('FeatureSet', (_message.Message,), dict(
  DESCRIPTOR = _FEATURESET,
  __module__ = 'feast.core.DatasetService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.FeatureSet)
  ))
_sym_db.RegisterMessage(FeatureSet)

DatasetInfo = _reflection.GeneratedProtocolMessageType('DatasetInfo', (_message.Message,), dict(
  DESCRIPTOR = _DATASETINFO,
  __module__ = 'feast.core.DatasetService_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.DatasetInfo)
  ))
_sym_db.RegisterMessage(DatasetInfo)


DESCRIPTOR._options = None
_DATASETSERVICETYPES_CREATEDATASETREQUEST_FILTERSENTRY._options = None

_DATASETSERVICE = _descriptor.ServiceDescriptor(
  name='DatasetService',
  full_name='feast.core.DatasetService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=605,
  serialized_end=749,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateDataset',
    full_name='feast.core.DatasetService.CreateDataset',
    index=0,
    containing_service=None,
    input_type=_DATASETSERVICETYPES_CREATEDATASETREQUEST,
    output_type=_DATASETSERVICETYPES_CREATEDATASETRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATASETSERVICE)

DESCRIPTOR.services_by_name['DatasetService'] = _DATASETSERVICE

# @@protoc_insertion_point(module_scope)

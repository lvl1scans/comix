# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: comix.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='comix.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x08comix.proto\"=\n\rComicResponse\x12\x15\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x06.Error\x12\x15\n\x05\x63omic\x18\x02 \x01(\x0b\x32\x06.Comic\"\x19\n\x05\x45rror\x12\x10\n\x08\x65rrormsg\x18\x02 \x01(\t\"^\n\x05\x43omic\x12\x10\n\x08\x63omic_id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x19\n\x05issue\x18\x03 \x01(\x0b\x32\n.IssueInfo\x12\x17\n\x04\x62ook\x18\x04 \x01(\x0b\x32\t.BookInfo\"\x9a\x01\n\tIssueInfo\x12\r\n\x05title\x18\x01 \x01(\t\x12\x1d\n\tpublisher\x18\x02 \x01(\x0b\x32\n.Publisher\x12\x17\n\x06series\x18\x03 \x01(\x0b\x32\x07.Series\x12!\n\x12print_release_date\x18\x05 \x01(\x0b\x32\x05.Date\x12#\n\x14\x64igital_release_date\x18\x06 \x01(\x0b\x32\x05.Date\"!\n\tPublisher\x12\x14\n\x0cpublisher_id\x18\x01 \x01(\t\"\x17\n\x06Series\x12\r\n\x05issue\x18\x08 \x01(\r\"0\n\x04\x44\x61te\x12\x0c\n\x04year\x18\x01 \x01(\r\x12\r\n\x05month\x18\x02 \x01(\r\x12\x0b\n\x03\x64\x61y\x18\x03 \x01(\r\" \n\x08\x42ookInfo\x12\x14\n\x05pages\x18\x05 \x03(\x0b\x32\x05.Page\"#\n\x04Page\x12\x1b\n\x08pageinfo\x18\x03 \x01(\x0b\x32\t.PageInfo\"\"\n\x08PageInfo\x12\x16\n\x06images\x18\x01 \x03(\x0b\x32\x06.Image\"\x8a\x01\n\x05Image\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x19\n\x04type\x18\x06 \x01(\x0e\x32\x0b.Image.Type\x12\x17\n\x06\x64igest\x18\x07 \x01(\x0b\x32\x07.Digest\x12\x18\n\x07\x65\x64igest\x18\x08 \x01(\x0b\x32\x07.Digest\"&\n\x04Type\x12\t\n\x05OTHER\x10\x00\x12\t\n\x05THUMB\x10\x01\x12\x08\n\x04\x46ULL\x10\x02\"\x16\n\x06\x44igest\x12\x0c\n\x04\x64\x61ta\x18\x07 \x01(\x0c'
)



_IMAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Image.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='THUMB', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FULL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=673,
  serialized_end=711,
)
_sym_db.RegisterEnumDescriptor(_IMAGE_TYPE)


_COMICRESPONSE = _descriptor.Descriptor(
  name='ComicResponse',
  full_name='ComicResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='ComicResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='comic', full_name='ComicResponse.comic', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=12,
  serialized_end=73,
)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='errormsg', full_name='Error.errormsg', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=100,
)


_COMIC = _descriptor.Descriptor(
  name='Comic',
  full_name='Comic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='comic_id', full_name='Comic.comic_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='Comic.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='issue', full_name='Comic.issue', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='book', full_name='Comic.book', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=196,
)


_ISSUEINFO = _descriptor.Descriptor(
  name='IssueInfo',
  full_name='IssueInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='IssueInfo.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='publisher', full_name='IssueInfo.publisher', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='series', full_name='IssueInfo.series', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='print_release_date', full_name='IssueInfo.print_release_date', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='digital_release_date', full_name='IssueInfo.digital_release_date', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=199,
  serialized_end=353,
)


_PUBLISHER = _descriptor.Descriptor(
  name='Publisher',
  full_name='Publisher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='Publisher.publisher_id', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=355,
  serialized_end=388,
)


_SERIES = _descriptor.Descriptor(
  name='Series',
  full_name='Series',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='issue', full_name='Series.issue', index=0,
      number=8, type=13, cpp_type=3, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=390,
  serialized_end=413,
)


_DATE = _descriptor.Descriptor(
  name='Date',
  full_name='Date',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='year', full_name='Date.year', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='month', full_name='Date.month', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='day', full_name='Date.day', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=415,
  serialized_end=463,
)


_BOOKINFO = _descriptor.Descriptor(
  name='BookInfo',
  full_name='BookInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pages', full_name='BookInfo.pages', index=0,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=465,
  serialized_end=497,
)


_PAGE = _descriptor.Descriptor(
  name='Page',
  full_name='Page',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pageinfo', full_name='Page.pageinfo', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=499,
  serialized_end=534,
)


_PAGEINFO = _descriptor.Descriptor(
  name='PageInfo',
  full_name='PageInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='images', full_name='PageInfo.images', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=536,
  serialized_end=570,
)


_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uri', full_name='Image.uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='Image.type', index=1,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='digest', full_name='Image.digest', index=2,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='edigest', full_name='Image.edigest', index=3,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _IMAGE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=573,
  serialized_end=711,
)


_DIGEST = _descriptor.Descriptor(
  name='Digest',
  full_name='Digest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='Digest.data', index=0,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=713,
  serialized_end=735,
)

_COMICRESPONSE.fields_by_name['error'].message_type = _ERROR
_COMICRESPONSE.fields_by_name['comic'].message_type = _COMIC
_COMIC.fields_by_name['issue'].message_type = _ISSUEINFO
_COMIC.fields_by_name['book'].message_type = _BOOKINFO
_ISSUEINFO.fields_by_name['publisher'].message_type = _PUBLISHER
_ISSUEINFO.fields_by_name['series'].message_type = _SERIES
_ISSUEINFO.fields_by_name['print_release_date'].message_type = _DATE
_ISSUEINFO.fields_by_name['digital_release_date'].message_type = _DATE
_BOOKINFO.fields_by_name['pages'].message_type = _PAGE
_PAGE.fields_by_name['pageinfo'].message_type = _PAGEINFO
_PAGEINFO.fields_by_name['images'].message_type = _IMAGE
_IMAGE.fields_by_name['type'].enum_type = _IMAGE_TYPE
_IMAGE.fields_by_name['digest'].message_type = _DIGEST
_IMAGE.fields_by_name['edigest'].message_type = _DIGEST
_IMAGE_TYPE.containing_type = _IMAGE
DESCRIPTOR.message_types_by_name['ComicResponse'] = _COMICRESPONSE
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.message_types_by_name['Comic'] = _COMIC
DESCRIPTOR.message_types_by_name['IssueInfo'] = _ISSUEINFO
DESCRIPTOR.message_types_by_name['Publisher'] = _PUBLISHER
DESCRIPTOR.message_types_by_name['Series'] = _SERIES
DESCRIPTOR.message_types_by_name['Date'] = _DATE
DESCRIPTOR.message_types_by_name['BookInfo'] = _BOOKINFO
DESCRIPTOR.message_types_by_name['Page'] = _PAGE
DESCRIPTOR.message_types_by_name['PageInfo'] = _PAGEINFO
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['Digest'] = _DIGEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ComicResponse = _reflection.GeneratedProtocolMessageType('ComicResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMICRESPONSE,
  '__module__' : 'comix_pb2'
  # @@protoc_insertion_point(class_scope:ComicResponse)
  })
_sym_db.RegisterMessage(ComicResponse)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {
  'DESCRIPTOR' : _ERROR,
  '__module__' : 'comix_pb2'
  # @@protoc_insertion_point(class_scope:Error)
  })
_sym_db.RegisterMessage(Error)

Comic = _reflection.GeneratedProtocolMessageType('Comic', (_message.Message,), {
  'DESCRIPTOR' : _COMIC,
  '__module__' : 'comix_pb2'
  # @@protoc_insertion_point(class_scope:Comic)
  })
_sym_db.RegisterMessage(Comic)

IssueInfo = _reflection.GeneratedProtocolMessageType('IssueInfo', (_message.Message,), {
  'DESCRIPTOR' : _ISSUEINFO,
  '__module__' : 'comix_pb2'
  # @@protoc_insertion_point(class_scope:IssueInfo)
  })
_sym_db.RegisterMessage(IssueInfo)

Publisher = _reflection.GeneratedProtocolMessageType('Publisher', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHER,
  '__module__' : 'comix_pb2'
  # @@protoc_insertion_point(class_scope:Publisher)
  })
_sym_db.RegisterMessage(Publisher)

Series = _reflection.GeneratedProtocolMessageType('Series', (_message.Message,), {
  'DESCRIPTOR' : _SERIES,
  '__module__' : 'comix_pb2'
  # @@protoc_insertion_point(class_scope:Series)
  })
_sym_db.RegisterMessage(Series)

Date = _reflection.GeneratedProtocolMessageType('Date', (_message.Message,), {
  'DESCRIPTOR' : _DATE,
  '__module__' : 'comix_pb2'
  # @@protoc_insertion_point(class_scope:Date)
  })
_sym_db.RegisterMessage(Date)

BookInfo = _reflection.GeneratedProtocolMessageType('BookInfo', (_message.Message,), {
  'DESCRIPTOR' : _BOOKINFO,
  '__module__' : 'comix_pb2'
  # @@protoc_insertion_point(class_scope:BookInfo)
  })
_sym_db.RegisterMessage(BookInfo)

Page = _reflection.GeneratedProtocolMessageType('Page', (_message.Message,), {
  'DESCRIPTOR' : _PAGE,
  '__module__' : 'comix_pb2'
  # @@protoc_insertion_point(class_scope:Page)
  })
_sym_db.RegisterMessage(Page)

PageInfo = _reflection.GeneratedProtocolMessageType('PageInfo', (_message.Message,), {
  'DESCRIPTOR' : _PAGEINFO,
  '__module__' : 'comix_pb2'
  # @@protoc_insertion_point(class_scope:PageInfo)
  })
_sym_db.RegisterMessage(PageInfo)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
  'DESCRIPTOR' : _IMAGE,
  '__module__' : 'comix_pb2'
  # @@protoc_insertion_point(class_scope:Image)
  })
_sym_db.RegisterMessage(Image)

Digest = _reflection.GeneratedProtocolMessageType('Digest', (_message.Message,), {
  'DESCRIPTOR' : _DIGEST,
  '__module__' : 'comix_pb2'
  # @@protoc_insertion_point(class_scope:Digest)
  })
_sym_db.RegisterMessage(Digest)


# @@protoc_insertion_point(module_scope)

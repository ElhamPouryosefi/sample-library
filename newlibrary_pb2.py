# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: newlibrary.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10newlibrary.proto\x12\nnewlibrary\x1a\x1bgoogle/protobuf/empty.proto\"D\n\x04\x42ook\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tbook_name\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\r\n\x05pages\x18\x04 \x01(\x05\"\x11\n\x0f\x42ookListRequest\"!\n\x13\x42ookRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x32\xa3\x02\n\x0e\x42ookController\x12\x39\n\x04List\x12\x1b.newlibrary.BookListRequest\x1a\x10.newlibrary.Book\"\x00\x30\x01\x12.\n\x06\x43reate\x12\x10.newlibrary.Book\x1a\x10.newlibrary.Book\"\x00\x12?\n\x08Retrieve\x12\x1f.newlibrary.BookRetrieveRequest\x1a\x10.newlibrary.Book\"\x00\x12.\n\x06Update\x12\x10.newlibrary.Book\x1a\x10.newlibrary.Book\"\x00\x12\x35\n\x07\x44\x65stroy\x12\x10.newlibrary.Book\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')



_BOOK = DESCRIPTOR.message_types_by_name['Book']
_BOOKLISTREQUEST = DESCRIPTOR.message_types_by_name['BookListRequest']
_BOOKRETRIEVEREQUEST = DESCRIPTOR.message_types_by_name['BookRetrieveRequest']
Book = _reflection.GeneratedProtocolMessageType('Book', (_message.Message,), {
  'DESCRIPTOR' : _BOOK,
  '__module__' : 'newlibrary_pb2'
  # @@protoc_insertion_point(class_scope:newlibrary.Book)
  })
_sym_db.RegisterMessage(Book)

BookListRequest = _reflection.GeneratedProtocolMessageType('BookListRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOOKLISTREQUEST,
  '__module__' : 'newlibrary_pb2'
  # @@protoc_insertion_point(class_scope:newlibrary.BookListRequest)
  })
_sym_db.RegisterMessage(BookListRequest)

BookRetrieveRequest = _reflection.GeneratedProtocolMessageType('BookRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOOKRETRIEVEREQUEST,
  '__module__' : 'newlibrary_pb2'
  # @@protoc_insertion_point(class_scope:newlibrary.BookRetrieveRequest)
  })
_sym_db.RegisterMessage(BookRetrieveRequest)

_BOOKCONTROLLER = DESCRIPTOR.services_by_name['BookController']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOOK._serialized_start=61
  _BOOK._serialized_end=129
  _BOOKLISTREQUEST._serialized_start=131
  _BOOKLISTREQUEST._serialized_end=148
  _BOOKRETRIEVEREQUEST._serialized_start=150
  _BOOKRETRIEVEREQUEST._serialized_end=183
  _BOOKCONTROLLER._serialized_start=186
  _BOOKCONTROLLER._serialized_end=477
# @@protoc_insertion_point(module_scope)
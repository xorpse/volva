#!/bin/sh

INIT_FILE=volva/__init__.py

rm -rf volva/*
protoc --proto_path=../proto --python_out=volva ../proto/*.proto

touch ${INIT_FILE}
2to3 volva -w -n

echo "from __future__ import absolute_import" > ${INIT_FILE}

for f in volva/*_pb2.py; do
    f=$(basename -- $f)
    echo "from . import ${f%.py} as ${f%_pb2.py}" >> ${INIT_FILE}
done

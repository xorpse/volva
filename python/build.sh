#!/bin/sh

rm -rf volva/*
protoc --proto_path=../proto --python_out=volva ../proto/*.proto
touch volva/__init__.py
2to3 volva -w -n

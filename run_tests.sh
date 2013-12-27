#!/usr/bin/env bash

set -e

if [ -e ./test.env ]; then
  source ./test.env
fi

py.test test_template.py

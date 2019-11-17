#!/bin/bash
grep class aarch64_instructions.py | cut -d"(" -f1 | cut -c 7- | tail -n+2

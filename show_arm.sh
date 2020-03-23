#!/bin/bash

aarch64-linux-gnu-gcc -march=armv8.3-a -S -o - $@

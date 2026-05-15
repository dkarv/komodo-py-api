#!/bin/bash

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD_DIR="${ROOT_DIR}/build"
cd $BUILD_DIR

cargo install typeshare-cli --features python --version 1.13.4
node ../scripts/generate_types.mjs

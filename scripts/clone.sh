#!/bin/bash

set -euo pipefail

TAG="${1:-main}"
REPO_URL="https://github.com/moghtech/komodo"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD_DIR="${ROOT_DIR}/build"

mkdir -p "${BUILD_DIR}"

echo "Cloning ${REPO_URL} at tag/branch ${TAG} into ${BUILD_DIR}"
git clone --depth 1 --branch "${TAG}" "${REPO_URL}" "${BUILD_DIR}"

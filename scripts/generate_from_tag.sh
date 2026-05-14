#!/usr/bin/env bash
set -euo pipefail

TAG="${1:-main}"
REPO_URL="https://github.com/moghtech/komodo.git"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
PATCH_DIR="${SCRIPT_DIR}/patches"
WORK_DIR="$(mktemp -d)"

cleanup() {
  rm -rf "${WORK_DIR}"
}
trap cleanup EXIT

git clone --branch "${TAG}" --single-branch "${REPO_URL}" "${WORK_DIR}/komodo"

if compgen -G "${PATCH_DIR}/*.patch" > /dev/null; then
  for patch_file in "${PATCH_DIR}"/*.patch; do
    git -C "${WORK_DIR}/komodo" apply "${patch_file}"
  done
fi

(
  cd "${WORK_DIR}/komodo"
  typeshare -V || cargo install typeshare-cli@1.13.3 -F python
  node client/core/py/generate_types.mjs
)

GENERATED_API_PATH="${WORK_DIR}/komodo/client/core/py/komodo_api"
if [ ! -d "${GENERATED_API_PATH}" ]; then
  echo "Generated API path not found: ${GENERATED_API_PATH}" >&2
  exit 1
fi

rm -rf "${REPO_ROOT}/komodo_api"
cp -R "${GENERATED_API_PATH}" "${REPO_ROOT}/komodo_api"

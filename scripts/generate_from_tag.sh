#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 3 ]; then
  echo "Usage: $0 <tag> <generate-command> <generated-api-path> [repo-url]"
  exit 1
fi

TAG="$1"
GENERATE_COMMAND="$2"
GENERATED_API_PATH="$3"
REPO_URL="${4:-https://github.com/moghtech/komodo.git}"

python scripts/generate_komodo_api.py \
  "$TAG" \
  --repo-url "$REPO_URL" \
  --generate-command "$GENERATE_COMMAND" \
  --generated-api-path "$GENERATED_API_PATH"

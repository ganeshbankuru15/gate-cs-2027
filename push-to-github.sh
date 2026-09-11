#!/usr/bin/env bash
# Push the GATE CS 2027 notes repo to GitHub using the dedicated deploy key.
# Usage:  ./push-to-github.sh <github-username> [repo-name]
set -euo pipefail

USER_NAME="${1:-}"
REPO="${2:-gate-cs-2027}"
KEY="$HOME/.ssh/github_deploy"

if [ -z "$USER_NAME" ]; then
  echo "Usage: $0 <github-username> [repo-name]" >&2
  exit 1
fi
if [ ! -f "$KEY" ]; then
  echo "ERROR: deploy key not found at $KEY" >&2
  exit 1
fi

cd "$(dirname "$0")"

# Use ONLY this key for github.com (does not affect any other git usage).
export GIT_SSH_COMMAND="ssh -i $KEY -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new"

echo "==> Testing deploy key against github.com ..."
if ssh -i "$KEY" -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new -T git@github.com 2>&1 | grep -q "successfully authenticated"; then
  echo "    deploy key accepted"
else
  echo "    NOTE: GitHub usually replies 'does not provide shell access' even on success — checking repo access next."
fi

echo "==> Configuring remote ..."
git remote remove origin 2>/dev/null || true
git remote add origin "git@github.com:${USER_NAME}/${REPO}.git"
echo "    origin -> git@github.com:${USER_NAME}/${REPO}.git"

echo "==> Pushing main ..."
git push -u origin main

echo
echo "==> Done."
echo "    Repository : https://github.com/${USER_NAME}/${REPO}"
echo "    Site (once Pages is enabled): https://${USER_NAME}.github.io/${REPO}/"

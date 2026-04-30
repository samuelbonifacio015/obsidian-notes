#!/bin/bash
# Auto-sync Obsidian vault to GitHub
# Runs: git add → commit → push
# Designed for cron: 30 22 * * * /path/to/git-sync.sh

set -e

VAULT_DIR="/home/samuel/obsidian-notes"
cd "$VAULT_DIR"

# Check for changes
if [[ -z $(git status --porcelain) ]]; then
    echo "[$(date '+%Y-%m-%d %H:%M')] ✅ No changes to commit"
    exit 0
fi

# Show what's changed
CHANGED=$(git status --porcelain | wc -l)
echo "[$(date '+%Y-%m-%d %H:%M')] 📝 Found $CHANGED changed files"

git add -A

# Generate commit message with summary of changes
FILES=$(git diff --cached --name-only | head -10)
SUMMARY=$(echo "$FILES" | sed 's|obsidian/||' | tr '\n' ', ' | sed 's/, $//')

if [[ -z "$SUMMARY" ]]; then
    SUMMARY="auto-sync"
fi

git commit -m "chore(vault): auto-sync $(date '+%Y-%m-%dT%H:%M') — ${SUMMARY:0:80}"

if git push origin main 2>&1; then
    echo "[$(date '+%Y-%m-%d %H:%M')] ✅ Pushed to GitHub"
else
    echo "[$(date '+%Y-%m-%d %H:%M')] ⚠️ Push failed (may need pull first)" >&2
    exit 1
fi

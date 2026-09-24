#!/bin/zsh
# Sync Obsidian vault changes to GitHub (and deploy to Blot via Actions)

cd "/Users/johnphilpin/Documents/Claude/1-PROJECTS-CLAUDE-LIVE/WIKI/Studio"

# Check for changes
git status

# Stage all changes
git add -A

# Commit with timestamp
git commit -m "Studio sync: $(date '+%Y-%m-%d %H:%M:%S')" || echo "No changes to commit"

# Push to GitHub (triggers deploy-to-blot GitHub Action)
git push origin main

echo "✓ Sync complete. GitHub Actions will deploy to Blot."

#!/bin/bash
# STG-UNIFIED: AUTHENTICATED BASH PROVISIONING WORKFLOW
# Objective: Zero-Touch Build Compilation for the TRISULA Chainstack Stack

echo "============================================================"
echo "📡 INITIALIZING SOVEREIGN BUILD PROVISIONER [CHAINSTACK AUTH]"
echo "============================================================"

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE}")/.." && pwd)"
BACKEND_DIR="$ROOT_DIR/STG-ECOSYSTEM/backend"
FRONTEND_DIR="$ROOT_DIR/STG-ECOSYSTEM/frontend"

# Check for dotenv deployment tools inside environment paths
if [ -f "$BACKEND_DIR/.env" ]; then
    export $(cat "$BACKEND_DIR/.env" | xargs)
    echo "🔐 SECURITY: Authenticated Node Credentials Loaded for Node ID: $CHAINSTACK_NODE_ID"
else
    echo "⚠️  Security Warning: .env execution parameters missing."
fi

cd "$FRONTEND_DIR" || exit 1

if ! command -v npm &> /dev/null; then
    echo "🚨 Environment Error: npm executable toolchain not found."
    exit 1
fi

echo "📦 Step 1: Syncing clean toolchain modules..."
npm install --silent

echo "⚙️  Step 2: Triggering automated Vite compilation engine..."
npm run build --silent

echo "============================================================"
echo "✅ ARCHITECTURE LOCKED: Authenticated Chainstack Assets Pre-Compiled."
echo "============================================================"

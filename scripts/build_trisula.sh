#!/bin/bash
# STG-UNIFIED: AUTOMATED BASH PROVISIONING WORKFLOW
# Objective: Zero-Touch Build Compilation for the TRISULA Stack

echo "============================================================"
echo "📡 INITIALIZING SOVEREIGN BUILD PROVISIONER (SENJATA TRISULA)"
echo "============================================================"

# Navigate to application workspace core
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FRONTEND_DIR="$ROOT_DIR/STG-ECOSYSTEM/frontend"

cd "$FRONTEND_DIR" || exit 1

# Check for node package deployment tools
if ! command -v npm &> /dev/null; then
    echo "🚨 Environment Error: npm executable toolchain not found."
    exit 1
fi

echo "📦 Step 1: Syncing clean toolchain modules..."
npm install --silent

echo "⚙️  Step 2: Triggering automated Vite compilation engine..."
npm run build --silent

echo "============================================================"
echo "✅ ARCHITECTURE LOCKED: Static assets successfully pre-compiled."
echo "🏁 Terminal path: dist/frontend/"
echo "============================================================"

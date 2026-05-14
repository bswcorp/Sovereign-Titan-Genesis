#!/bin/bash
# 🏛️ STG UNIFIED - SYSTEM BOOT AUTOMATION
# Purpose: Orchestrates both Express Backend and Vite Frontend Processes

echo "============================================================"
echo "📡 STARTING UNIFIED SYSTEM BOOT PIPELINE [SENJATA TRISULA]"
echo "============================================================"

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE}")/.." && pwd)"
BACKEND_DIR="$ROOT_DIR/STG-ECOSYSTEM/backend"
FRONTEND_DIR="$ROOT_DIR/STG-ECOSYSTEM/frontend"

# Trap system exit commands to kill background tasks cleanly
cleanup() {
    echo -e "\n🛑 [SYSTEM] Shutting down background server processes gracefully..."
    kill "$BACKEND_PID" 2>/dev/null
    kill "$FRONTEND_PID" 2>/dev/null
    exit 0
}
trap cleanup SIGINT SIGTERM

echo "📡 Step 1: Spinning up Express REST API Backend Engine..."
cd "$BACKEND_DIR" || exit 1
npm start > "$ROOT_DIR/backend_runtime.log" 2>&1 &
BACKEND_PID=$!

echo "⚡ Step 2: Spinning up Automated Vite Frontend Compiler Server..."
cd "$FRONTEND_DIR" || exit 1
npm run dev > "$ROOT_DIR/frontend_runtime.log" 2>&1 &
FRONTEND_PID=$!

echo "------------------------------------------------------------"
echo "🟢 STACK BOOT SUCCESSFUL"
echo "🔗 Backend REST API Gateway : http://127.0.0.1:5000"
echo "🔗 Frontend UX Terminal    : http://127.0.0.1:3000"
echo "------------------------------------------------------------"
echo "💡 Press [CTRL+C] at any time to freeze and terminate processes cleanly."

# Keep parent script alive to preserve process tree tracking
while true; do
    sleep 1
done

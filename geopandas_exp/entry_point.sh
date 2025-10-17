#!/usr/bin/env bash
set -e  # exit if any command fails

# --- Configuration ---
IMAGE_NAME="conda-notebook"
TOKEN="supersecret"
PORT=8888
NOTEBOOK_DIR="$PWD/notebooks"

echo "🔧 Setting up JupyterLab Conda notebook environment..."

# --- Ensure notebooks directory exists ---
if [ ! -d "$NOTEBOOK_DIR" ]; then
  echo "📁 Creating notebooks folder in repo..."
  mkdir -p "$NOTEBOOK_DIR"
fi

# --- Build Docker image ---
echo "🐳 Building Docker image: $IMAGE_NAME ..."
docker build -t "$IMAGE_NAME" .

# --- Run the container ---
echo "🚀 Starting JupyterLab at http://localhost:$PORT ..."
docker run -it --rm \
  -p "$PORT:$PORT" \
  -e JUPYTER_TOKEN="$TOKEN" \
  -v "$NOTEBOOK_DIR":/srv/notebooks \
  "$IMAGE_NAME"

echo "✅ Done! Access your notebook at http://localhost:$PORT"

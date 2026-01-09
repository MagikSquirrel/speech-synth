#!/usr/bin/env bash

# Exit on error and undefined vars
set -euo pipefail

# Ensure a prompt was provided
if [ "$#" -lt 1 ]; then
  echo "Usage: $0 \"your prompt here\""
  exit 1
fi

PROMPT="$1"

# Run Ollama once and capture output
RESPONSE="$(ollama run gemma3:270m "$PROMPT")"

# Print the response
echo "Prompt:"
echo "----------------"
echo "$PROMPT"
echo
echo "Ollama response:"
echo "----------------"
echo "$RESPONSE"
echo

# Speak the response (flatten newlines for nicer speech)
espeak "$(echo "$RESPONSE" | tr '\n' ' ')"

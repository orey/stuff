#!/bin/bash
# Environment variables
OLLAMA_PATH="/home/olivier/ai/ollama"
PATH="$OLLAMA_PATH/bin:$OLLAMA_PATH/lib/ollama:$PATH"
LD_LIBRARY_PATH="$OLLAMA_PATH/lib/ollama:$LD_LIBRARY_PATH"
echo PATH = $PATH

# Allow all Chrome, Firefox, and Safari extensions
OLLAMA_ORIGINS=chrome-extension://*,moz-extension://*,http://127.0.0.1:8000 ollama serve


@echo off

llama-server.exe ^
 -m models\MiniCPM5-1B-Claude-Opus-Fable5-Thinking-Q8_0.gguf ^
 -c 8192 ^
 -ngl 0 ^
 --ctx-size 128000 ^
 --embedding ^
 --host 127.0.0.1 ^
 --port 8080
 

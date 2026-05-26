@echo off

llama-server.exe ^
 -m models\qwen2.5-0.5b-instruct-q4_k_m.gguf ^
 -c 8192 ^
 -ngl 0 ^
 --host 127.0.0.1 ^
 --port 8080
 

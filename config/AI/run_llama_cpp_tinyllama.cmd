@echo off

llama-server.exe ^
 -m models\tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf ^
 -c 8192 ^
 -ngl 0 ^
 --host 127.0.0.1 ^
 --port 8080
 

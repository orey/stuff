@echo off
title LLAMA.CPP EMBEDDING

llama-server.exe ^
 --embedding ^
 -m models\bge-base-en-v1.5-f32.gguf ^
 -c 512 ^
 --host 127.0.0.1 ^
 --port 1212
 
pause

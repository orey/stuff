@echo off
:beginning
setlocal enabledelayedexpansion

set /p QUESTION=Ask llama:

curl http://127.0.0.1:8080/v1/chat/completions ^
-H "Content-Type: application/json" ^
-d "{\"model\":\"llama\",\"messages\":[{\"role\":\"user\",\"content\":\"!QUESTION!\"}],\"temperature\":0.2}"

echo.
pause
goto :beginning

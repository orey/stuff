cls
@echo off
set /p "message=Enter message: "

git add *
git commit -a -m %message%
git push origin main

:end
echo Done
pause

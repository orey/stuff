cls
@echo off

if "%1" == "" (
    echo Publish all script
    echo Usage : publish-all.bat [comments without space]
    goto :end
)

for /f %%a IN ('dir /b /ad') do (
    cd %%a
    echo Repo: %%a
    git add *
    git commit -a -m "%*"
    git push origin master
    cd ..
)

:end
echo Done
pause

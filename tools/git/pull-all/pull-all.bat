cls
@echo off

echo Pull all repos in this folder

pause

for /f %%a IN ('dir /b /ad') do (
    cd %%a
    echo -----------------------------
    echo Repo: %%a
    git pull
    cd ..
)

echo Done

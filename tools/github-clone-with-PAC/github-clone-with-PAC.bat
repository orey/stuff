cls
@echo off

if "%1" == "" (
    echo Github clone script using PAC
    echo Usage : clone-github.bat [name_of_repo]
    goto :end
)

set /p pac=<PAC.txt
git clone https://orey:%pac%@github.com/orey/%1.git

:end
echo Done

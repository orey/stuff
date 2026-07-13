@echo off
setlocal

REM Check if a directory was provided as an argument
if "%~1"=="" (
    echo Usage: list_subfolders.bat [directory]
    echo.
    echo If no directory is specified, the current directory will be used.
    set "target_dir=%CD%"
) else (
    set "target_dir=%~1"
)

REM Check if the directory exists
if not exist "%target_dir%" (
    echo Error: Directory "%target_dir%" does not exist.
    pause
    exit /b 1
)

echo ========================================
echo Subfolders in: %target_dir%
echo ========================================
echo.

REM List all subdirectories (non-recursive by default)
for /d %%D in ("%target_dir%\*") do (
    echo %%~nxD
)

echo.
echo Total: %errorlevel% subfolder(s) found.
echo.

pause

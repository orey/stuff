@echo off

set target=d:
rem set target=C:\ProgramData\orey

set /a num=%random%
dir > %num%.txt
echo Generated file: %num%.txt
move %num%.txt %target%

pause


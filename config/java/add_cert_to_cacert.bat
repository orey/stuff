@echo off
if "%1"=="" GOTO USAGE
if "%2"=="" GOTO USAGE
if "%1"=="" GOTO USAGE

echo INFO Default password is "changeit"

set JAVA_HOME=C:\ProgramData\orey\Software\open-jdk-java-se-8u41-ri
set PATH=%JAVA_HOME%\bin;%PATH%

keytool.exe -import -alias %2 -file %3 -keystore %1 -storepass changeit

goto:EOF

:USAGE
echo Usage:
echo   add_cert_to_cacert.bat [path_to_cacert] [alias] [path_to_cert]
echo   Certificates should be DER encoded binary X509 .cer


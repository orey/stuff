@ECHO OFF
IF "%1"=="" GOTO USAGE
IF "%2"=="" GOTO USAGE

ECHO INFO: Default password is "changeit"

SET archi_jre=C:\Tools\DEV\Software\Archi\jre

%archi_jre%\bin\keytool -keystore %archi_jre%\lib\security\cacerts -importcert -alias %1 -file %2

:USAGE
ECHO Usage:
ECHO add_cert_to_Archi.bat ALIAS PATH_TO_CERT
GOTO:EOF


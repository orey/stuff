@ECHO OFF
ECHO List certificates

SET archi_jre=C:\Tools\DEV\Software\Archi4.4\jre

%archi_jre%\bin\keytool -keystore %archi_jre%\lib\security\cacerts -list -storepass changeit



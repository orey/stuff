@ECHO OFF
ECHO List certificates

set JAVA_HOME=C:\ProgramData\orey\Software\open-jdk-java-se-8u41-ri
set PATH=%JAVA_HOME%\bin;%PATH%

keytool.exe -keystore cacerts -list -storepass changeit > listcerts.txt



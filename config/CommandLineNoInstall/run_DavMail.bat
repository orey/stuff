set CLASSPATH=.;.\lib\*.jar

java -Xmx512M -Dsun.net.inetaddr.ttl=60 -cp davmail.jar:%CLASSPATH% davmail.DavGateway

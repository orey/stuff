#!/bin/bash

# Letting the default JDK of the OS
#export JAVA_HOME=/home/olivier/Software/java
#export PATH=$JAVA_HOME/bin:$JAVA_HOME/lib:$PATH

which java
java --version
java -Dsun.java2d.uiScale=1 -jar yed.jar


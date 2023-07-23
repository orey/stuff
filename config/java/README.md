# Java stuff

## Solve Java font size problem under Linux

### Default installation of OpenJDK in Debian does not work

The default software installed under Linux (OpenJDK) seems to embed in an hardcoded way a value of the `JAVA_TOOL_OPTIONS` with a default scale of `2`. When searching through the JDK it seems that `libjvm.so` is containing this hard coding. When running in console mode, the following message appears.

```
Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.uiScale=2
```

### Fixing the problem

Fixing the problem is easy: Create a batch file to override the option :

```
#!/bin/bash
java -Dsun.java2d.uiScale=1 -jar test.jar
```

You can also change the `JAVA_TOOL_OPTIONS` in the batch.

```
#!/bin/bash
export JAVA_TOOL_OPTIONS="-Dsun.java2d.uiScale=1"
java -jar test.jar
```

### Font2DTest

In some distributions of OpenJDK, you have the original demos. In the demos, you can find a tool named `Font2DTest` that can help you seeing the parameters associated to all fonts.

Sometimes the 

## Default JRE

Check what is your default JRE by typing `java -version` in a shell or console.

## Old JDKs

Some old products may run with an old JDK. You can find the old Java reference implementations here: https://jdk.java.net

## Adding certificates to cacerts

The Java certificate vault is located in `jre/lib/security` and is called `cacerts`.

The certificates must be exported in DER encoded binary X509 and should have the extension `.cer`.

The two attached batches enable:

  * To import a certificate into the `cacerts`;
  * To list all certificates in the `cacerts` (this batch is generating a text file named `list-certs.txt` with the dump of the `cacerts` vault).
  
  


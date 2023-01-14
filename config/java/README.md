# Java stuff

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


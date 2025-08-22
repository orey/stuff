# README

For maven like for the rest, several actions to do:

* Download the crt certificate of `repo.maven.apache.org.crt`
* Download the ROOT certificate of your proxy `Company-Root-CA`

Use the script to add the certificates to the `cacert` file.

On my side, I have also the proxy to declare in Maven config `settings.xml`.

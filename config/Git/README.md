# Install Git without installation rights

## Prerequisite

You need to have a folder from where you have the right to execute any program (except the ones that are blocked by your antivirus).

## Portable version

Download the portable version.

https://git-scm.com/downloads

## Firewall and certificates

Declare the firewall option:

```
git config --global http.proxy http://user:password@firewal.com:8080
```

If your firewall is using a certificate that is internally signed, Git may complain like ```SSL Certificate problem: unable to get local issuer```. Try this.

```
git config --global http.sslVerify false
```

Good page to browse: https://confluence.atlassian.com/bitbucketserverkb/ssl-certificate-problem-unable-to-get-local-issuer-certificate-816521128.html

## See also

Look at the `Archi` folder to have the scripts to write certificates in certificate archives.

*(Last update: June 2020)*

# Tips for running development tools in professional environment

## Portable versions

Prefer portable versions. Use ```.bat``` scripts to include the various binaries.

```
set PATH="C:\Tools\MyPath":%PATH
```

## Important tools

Here is a list of important tools and tricks to install the portable versions:

### Git

Use the portable version. Declare the firewall option:

```
git config --global http.proxy http://user:password@firewal.com:8080
```

If your firewall is using a certificate that is internally signed, Git may complain like ```SSL Certificate problem: unable to get local issuer```. Try this.

```
git config --global http.sslVerify false
```

Good page to browse: https://confluence.atlassian.com/bitbucketserverkb/ssl-certificate-problem-unable-to-get-local-issuer-certificate-816521128.html


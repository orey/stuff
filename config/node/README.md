# Tips for node configuration

## Setup Proxy

```
npm config set proxy http://localhost:3128
npm config set https-proxy http://localhost:3128
```

Look the to the `/home/.npmrc` and add the following to it to disable SSL control.
```
struct-ssl=false
```

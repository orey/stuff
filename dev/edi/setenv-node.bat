@echo off
set NODEPATH=C:\ProgramData\orey\Software\node-v24.11.1-win-x64\
set PATH=%NODEPATH%;%PATH%

set proxy=http://127.0.0.1:3128

set http_proxy=%proxy%
set HTTP_PROXY=%proxy%
set https_proxy=%proxy%
set HTTPS_PROXY=%proxy%

set SSL_CERT_DIR=C:\ProgramData\orey\home\cert

set REQUESTS_CA_BUNDLE=%SSL_CERT_DIR%\cacert.pem
set CURL_CA_BUNDLE=%SSL_CERT_DIR%\cacert.pem
set SSL_CERT_FILE=%SSL_CERT_DIR%\cacert.pem

set NODE_EXTRA_CA_CERTS=%SSL_CERT_DIR%\cacert.pem

set PIP_CONFIG_FILE=C:\ProgramData\orey\home\pip.ini

echo Variables set
node --version
npm --version

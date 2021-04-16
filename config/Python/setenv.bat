set PYTHON3PATH=C:\MyFolder\MyStuff\Software\Python-3.7.2
rem set PYTHONHOME=%PYTHON3PATH%
set PYTHONPATH=%PYTHON3PATH%;%PYTHON3PATH%\Lib;%PYTHON3PATH%\Scripts
set PATH=%PYTHONPATH%;%PATH%

set proxy=http://127.0.0.1:3128

set http_proxy=%proxy%
set HTTP_PROXY=%proxy%
set https_proxy=%proxy%
set HTTPS_PROXY=%proxy%

set REQUESTS_CA_BUNDLE=C:\MyFolder\MyStuff\cert\cacert.pem


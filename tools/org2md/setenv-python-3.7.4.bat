rem This script does not work

set PYTHON3PATH=C:\ProgramData\orey\Python-3.7.4
rem set PYTHONHOME=%PYTHON3PATH%
set PYTHONPATH=%PYTHON3PATH%;%PYTHON3PATH%\Lib;%PYTHON3PATH%\Scripts
set PATH=%PYTHONPATH%;%PATH%

set proxy=127.0.0.1:3128

set http_proxy=%proxy%
set HTTP_PROXY=%proxy%
set https_proxy=%proxy%
set HTTPS_PROXY=%proxy%

set REQUESTS_CA_BUNDLE=C:\ProgramData\orey\cert\cacert.pem

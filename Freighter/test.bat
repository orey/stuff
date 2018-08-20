@echo off
cls
color f1
title DIVA REPORT FREIGHTER TEST
if {%1}=={1} (
echo Testing bayplan report - verbose mode
freighter.py -b -f XN183SANLBayplanReport.csv -p IntragroupRatesTest01.csv -v
echo Done
goto End
)
if {%1}=={2} (
echo Testing documentation report - verbose mode
freighter.py -d -f XN183SANLDocumentationReport.csv -p IntragroupRatesTest01.csv -v
echo Done
goto End
)
if {%1}=={3} (
echo Testing bayplan report - non verbose mode
freighter.py -b -f XN183SANLBayplanReport.csv -p IntragroupRatesTest01.csv
echo Done
goto End
)
if {%1}=={4} (
echo Testing documentation report - non verbose mode
freighter.py -d -f XN183SANLDocumentationReport.csv -p IntragroupRatesTest01.csv
echo Done
goto End
)
echo Usage:
echo test.bat 1 - for bayplan report testing - verbose mode
echo test.bat 2 - for documentation report testing - verbose mode
echo test.bat 3 - for bayplan report testing - non verbose mode
echo test.bat 4 - for documentation report testing - non verbose mode
goto EndEnd
:End
dir /O-D
:EndEnd
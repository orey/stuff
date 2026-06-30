(@For /F "Delims=" %%A in ('dir *.txt /B/S/A-D') Do @Echo %%~fA;%%~zA) >input_txt.csv
(@For /F "Delims=" %%A in ('dir *.sum1 /B/S/A-D') Do @Echo %%~fA;%%~zA) >output_sum1.csv
(@For /F "Delims=" %%A in ('dir *.sum2 /B/S/A-D') Do @Echo %%~fA;%%~zA) >output_sum2.csv


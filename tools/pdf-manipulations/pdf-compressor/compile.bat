javac -cp .\itextpdf-5.5.13.3-withCompressor Compressor.java
pause
copy Compressor.class itextpdf-5.5.13.3-withCompressor\com
rem copy MANIFEST.MF itextpdf-5.5.13.3-withCompressor\META-INF
jar cvfm compressor.jar MANIFEST.MF -C itextpdf-5.5.13.3-withCompressor\ .



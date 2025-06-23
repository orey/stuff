for %%f in (C:\ProgramData\orey\data\outlook\test2\*.pptx) do (
echo %%f
C:\ProgramData\orey\Software\python-3.13.4\Scripts\pptx2md -o "%%f.md" --disable-image --disable-notes --disable-color --enable-slides --disable-escaping "%%f"
rem pause
)

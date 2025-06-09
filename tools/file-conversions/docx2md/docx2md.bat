for %%f in (C:\ProgramData\orey\data\outlook\test2\*.docx) do (
echo %%f
python convert_docx_to_md.py "%%f" "%%f.md"
rem pause
)

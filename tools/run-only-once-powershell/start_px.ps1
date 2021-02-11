if (Get-Process -Name "px" -ErrorAction SilentlyContinue)
{
    Write-Warning -Message "px is already running."
    #Write-Output "px is already running."
    #Write-Host "px is already running."
}
else
{
    Start-Process -FilePath C:\ProgramData\orey\Software\px-v0.4.0\px.exe
}
exit


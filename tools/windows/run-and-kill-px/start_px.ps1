if (Get-Process -Name "px" -ErrorAction SilentlyContinue)
{
    Write-Warning -Message "px is already running. Killing it."
    Stop-Process -Name "px"
    #Write-Output "px is already running."
    #Write-Host "px is already running."
}
else
{
    Start-Process -FilePath C:\ProgramData\orey\Software\px\px.exe
    Write-Output -Message "px started"
}
exit


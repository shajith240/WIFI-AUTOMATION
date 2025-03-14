@echo off
echo Checking for running automation...
tasklist /FI "IMAGENAME eq pythonw.exe"
echo.
echo If you see pythonw.exe in the list above, the script is running.
pause
Set WShell = CreateObject("WScript.Shell")
WShell.CurrentDirectory = "C:\Users\SHAJITH\OneDrive\Desktop\wifi_automation_project"
' Run pythonw directly instead of using batch file
WShell.Run "cmd /c venv\Scripts\activate.bat && pythonw wifi_login_automation.py", 0, False
Set WShell = Nothing
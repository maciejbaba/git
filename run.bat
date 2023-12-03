cd "C:\Users\Bombson\Documents\Github\git" & "C:\Users\Bombson\AppData\Local\Programs\Python\Python39\python.exe" "C:\Users\Bombson\Documents\GitHub\git\main.py"


REM super turbo hack for windows, ping takes 1 sec to execute, so we ping 120 times to get 2 minutes and use it as a timer

ping localhost -n 60 > nul


REM then we put the computer to sleep
rundll32.exe powrprof.dll, SetSuspendState Sleep

:: version 0.2
:: commit by Security-Learning

@echo off
  setlocal enableextensions disabledelayedexpansion

  call :getTime now

  set "task=day"
  :: update the task time in this section, follow the time format
  if "%now%" lss "06:30:00,00" ( set "task=night" )
  if "%now%" geq "18:30:00,00" ( set "task=night" )

  call :task_%task%

  echo %now%
  endlocal
  exit /b

:task_day
  :: do day task
  :: change to light theme
  reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 1 /f
  goto :eof

:task_night
  :: do night task
  ::change to dark theme
  reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 0 /f
  goto :eof

:: getTime
::    This routine returns the current( or passed as argument) time
::     in the form hh:mm:ss,cc in 24hr format, with two digits in each of the segments, 0 prefixed where needed

:getTime returnVar [time]
  setlocal enableextensions disabledelayedexpansion
  
  :: Retrieve parameters if present, else take the current time
  if "%~2"=="" ( set "t=%time%" ) else ( set "t=%~2" )

  :: test if the time contains correct (usual) data, else try something else
  echo(%t%|findstr /i /r /x /c:"[0-9:,.apm -]*" >nul || (
    set "t="
    for /f "tokens=2" %%a in ('2^>nul robocopy "|" . /njh') do (
      if not defined t set "t=%%a,00"
    )
    rem If we do not have a valid time string, leave
    if not defined t exit /b
  ))

  :: check if 24h time, adjust accordingly
  if not "%t:pm=%"=="%t%" ( set "p=12" ) else ( set "p=0" )

  :: seperate the elements of the time string
  for /f "tokens=1-5 delims=:.,-PpAaMm " %%a in ("%t%") do (
    set "h=%%a" & set "m=00%%b" & set "s=00%%c" & set "c=00%%d"
  )

  :: adjust the hour part of the time string
  set /a "h=100%h%+%p%"

  :: clean up and return the new time string
  endlocal & if not "%~1"=="" set "%~1=%h:~-2%:%m:~-2%:%s:~-2%,%c:~-2%" & exit /b

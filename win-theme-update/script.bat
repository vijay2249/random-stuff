:: version 0.1
:: source https://stackoverflow.com/questions/21809027/batch-file-run-cmd1-if-time-10pm-4am-else-run-cmd2
:: edited by VHCN

:: this double ":" symbol represents comments in bat script

:: this @echo off is used to hide the commands that we are going to execute from the user, 
:: means that once this script is being executed, user sees the blink of terminal opening and closing,
:: but user cannot see what operations that are being executed in the terminal
@echo off
  setlocal enableextensions disabledelayedexpansion

  :: get the current time and store it in the variable now
  set "now=%time: =0%"

  set "whatTheme=day"
  :: update the task time in this section, follow the time format
  if "%now%" lss "06:30:00,00" ( set "whatTheme=night" )
  if "%now%" geq "18:30:00,00" ( set "whatTheme=night" )

  call :%whatTheme%_theme

  endlocal
  :: end of the local function type command instructions
  exit /b
  :: exit from execution script instructions

:light_theme
  :: reg command to execute and set/update the value
  reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 1 /f
  reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /t REG_DWORD /d 1 /f
  goto :eof
  :: ignore any instruction that are specified in this function after this line and go to end of file

:dark_theme
  :: reg command to execute and set/update the value
  reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 0 /f
  reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /t REG_DWORD /d 0 /f
  goto :eof
  :: ignore any instruction that are specified in this function after this line and go to end of file

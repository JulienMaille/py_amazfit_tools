@echo off

IF "%1"=="" GOTO :Continue

set file=%~n1
set mPath=%~dp1
set mPathScript=%~dp0
echo %file%

python %mPathScript%\main.py --bip3 %2 --file %1

echo.
echo Install "%mPath%%file%_packed.bin" to Watch
echo.
pause

:Continue
IF "%1"=="" echo No json given. Usage: %~nx0 path\to\file.json


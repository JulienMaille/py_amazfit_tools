@echo off

set file=%~n1
set mPath=%~dp1
set mPathScript=%~dp0
 
python %mPathScript%\main.py --gts2 --file "%1"

echo.
echo Resources and JSON in "%mPath%%file%_unpacked"
echo.
pause

:Continue
IF "%1"=="" echo No bin file given. Usage: %~nx0 path\to\file.bin


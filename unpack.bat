@echo off

IF "%1"=="" GOTO :Continue

set file=%~n1
set mPath=%~dp1
set mPathScript=%~dp0

%mPathScript%\GTR2_Packer.exe -unc2 %1
ren "%1.unc" "%file%_unpacked.bin"
python %mPathScript%\main.py --gts2 --file "%mPath%%file%_unpacked.bin"

echo.
echo Resources and JSON in "%mPath%%file%_unpacked"
echo.
pause

:Continue
IF "%1"=="" echo No bin file given. Usage: %~nx0 path\to\file.bin


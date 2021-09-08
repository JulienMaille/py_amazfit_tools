@echo off

IF "%1"=="" GOTO :Continue

set file=%~n1
set mPath=%~dp1

GTR2_Packer.exe -unc %1
ren "%1.unc" "%file%_unpacked.bin"
python main.py --gts --file "%mPath%%file%_unpacked.bin"

echo.
echo Resources and JSON in "%mPath%%file%_unpacked"
echo.
pause

:Continue
IF "%1"=="" echo No bin file given. Usage: %~nx0 path\to\file.bin


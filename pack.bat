@echo off

IF "%1"=="" GOTO :Continue

set file=%~n1
set mPath=%~dp1
set mPathScript=%~dp0
echo %file%

python %mPathScript%\main.py --gts2 %2 --file %1
%mPathScript%\GTR2_Packer.exe -cmp2 %mPath%%file%_packed.bin
if exist "%mPath%%file%_packed_cmp.bin" del "%mPath%%file%_packed_cmp.bin"
ren "%mPath%%file%_packed.bin.cmp" "%file%_packed_cmp.bin"

echo.
echo Install "%mPath%%file%_packed_cmp.bin" to Watch
adb push %mPath%%file%_packed_cmp.bin /storage/emulated/0/Android/data/com.huami.watch.hmwatchmanager/files/watch_skin_local/209/22a779c9b1badae90f4eb521c0d21afe/22a779c9b1badae90f4eb521c0d21afe.bin


echo.
pause

:Continue
IF "%1"=="" echo No json given. Usage: %~nx0 path\to\file.json


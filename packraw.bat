@echo off

IF "%1"=="" GOTO :Continue

set file=%~n1
set mPath=%~dp1

python main.py --gts2 --from_raw --file %1
GTR2_Packer.exe -cmp2 %1\%file%_packed.bin
if exist "%1\%file%_packed_cmp.bin" del "%1\%file%_packed_cmp.bin"
ren "%1\%file%_packed.bin.cmp" "%file%_packed_cmp.bin"

echo.
echo Install "%1\%file%_packed_cmp.bin" to Watch
echo.
pause

:Continue
IF "%1"=="" echo No resource folder given. Usage: %~nx0 foldername


@echo off

IF "%1"=="" GOTO :Continue

set file=%~n1
set mPath=%~dp1
set mPathScript=%~dp0

for /d %%i in (%1\*) do (
    echo "%%i"
    for %%x in (%%i\*.bin) do (
        echo "%%x"
        call python %mPathScript%\main.py --bip3 --file "%%x"
    )
)

pause

:Continue
IF "%1"=="" echo No folder given. Usage: %~nx0 path\to\binfiles\


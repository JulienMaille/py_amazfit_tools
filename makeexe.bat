pyinstaller --noconfirm --onefile --console --icon "assets\icons8-smartwatch-32.ico" --distpath "output\gts2mini"  "main.py"



mkdir tmp\AmazFit_PackUnpack-GTS2mini

xcopy /S /E /Y wingui\* tmp\AmazFit_PackUnpack-GTS2mini\

copy output\gts2mini\main.exe tmp\AmazFit_PackUnpack-GTS2mini\py_amazfit_tools-GTS2mini\

"C:\Program Files\7-Zip\7z.exe" a -tzip .\output\gts2mini\AmazFit_PackUnpack-GTS2mini.zip .\tmp\AmazFit_PackUnpack-GTS2mini

rmdir /s /q tmp
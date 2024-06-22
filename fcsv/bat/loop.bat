@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

set /p inp="%cd%>"

for /f "tokens=1,2 delims= " %%a in ("%inp%") do (
    set str1=%%a
    set str2=%%b
)

echo @echo off > eng.bat
echo py ../src/main.py !str1! !str2! >> eng.bat

echo import os > ../src/y.py
echo os.system("cd ../bat && eng.bat") >> ../src/y.py
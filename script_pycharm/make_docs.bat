@echo off
cd docs
rmdir /S /Q .\build 2>NUL
..\venv\Scripts\sphinx-apidoc.exe -f -d 4 -e -o source ..\porcello
..\venv\Scripts\sphinx-build.exe -M html source build
..\venv\Scripts\sphinx-build.exe -b rinoh source build\rinoh
copy /Y build\rinoh\porcello.pdf porcello.pdf
cd ..

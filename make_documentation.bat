::@echo off
REM Ativar o ambiente virtual
call venv\Scripts\activate.bat
cd "scripts\Docs"
make html
pause

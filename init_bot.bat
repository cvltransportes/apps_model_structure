REM Verificar versao instalado do python (este projeto foi feito em Python 3.11)
python --version

REM Crie um ambiente virtual em Python 3.11
python -m venv venv

REM Ativar o ambiente virtual
call venv\Scripts\activate.bat

REM Atualizar PIP para última versão
python.exe -m pip install --upgrade pip

REM install packages
python -m pip install -e "C:\Users\06213\OneDrive\GitHub\CARVALIMA\priority_classes"

REM Listar pacotes instalados
pip list
pause
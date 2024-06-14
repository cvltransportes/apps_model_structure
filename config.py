import sys, os
from datetime import datetime
from priority_classes.log_register import log_register
from priority_classes.log_register.log_register import LogTipo

# obtem o camionha completo do diretorio onde o arquivo atual encontra-se
# no caso é o Nome do BOT
PATH_INICIO = os.path.dirname(__file__)

# Obter o nome da pasta (nome do bot, Ex.: Bot_qualidade... para direcionar o log para o diretorio correto)
BOT_NAME = os.path.basename(PATH_INICIO)

LOG: log_register.CustomLogger = log_register.CustomLogger(
    path_init=os.path.join(PATH_INICIO, "logs"), name_bot=BOT_NAME
)

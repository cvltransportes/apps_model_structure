from priority_classes.datahandler.datahandler import Handler
import os
from config import LOG, LogTipo

hd = Handler()


def load_xls_by_name(directory, file_name):
    '''Tenta carregar o arquivo através de seu nome exato'''
    file_path = os.path.join(directory, file_name)
    if os.path.exists(file_path):
        LOG.reg(f'Arquivo "{file_name}" carregado diretamente', LogTipo.INFO)
        return file_path
    else:
        LOG.reg(
            f'Atenção! o arquivo "{file_name}" não pode ser encontrado no diretório com esse nome.',
            LogTipo.WARNING,
        )
        None


def load_first_xlsx(directory):
    '''Tenta carregar o primeiro ar uivo do tipo xlsx na pasta'''
    LOG.reg(
        f'Tentando carregar o primeiro arquivo xlsx do diretório "{directory}"',
        LogTipo.INFO,
    )

    # Verifica se o diretório existe
    if not os.path.isdir(directory):
        raise ValueError(f"O diretório {directory} não existe.")

    # Percorre os arquivos no diretório
    for filename in os.listdir(directory):
        # Verifica se o arquivo tem a extensão .xlsx
        if filename.endswith(".xlsx"):
            # Constrói o caminho completo para o arquivo
            return os.path.join(directory, filename)

    # Se nenhum arquivo .xlsx for encontrado
    LOG.reg(f"Nenhum arquivo foi encontrado!", LogTipo.ERROR)
    return None


def try_load_file_and_process(folder, file_name):
    # primeiro procura pelo arquivo com o nome dele em sí
    if path_file_xls := load_xls_by_name(folder, file_name) == None:
        # caso o nome do arquivo tenha mudado, tenta pegar o primeiro .xlsx da pasta
        path_file_xls = load_first_xlsx(folder)
    table = hd.import_file(path_file_xls)
    table = hd.clear_table(table)
    table = table[table['Código da ocorrência'] == '601.0']
    return table


def load_PA_and_filter():
    folder = "downloads/pa"
    file_name = "Base Pendencias -CARVALIMA.xlsx"
    return try_load_file_and_process(folder, file_name)


def load_PC_and_filter():
    folder = "downloads/pc"
    file_name = "Base Pendencias -CARVALIMA TRANSPORTES LTDA.xlsx"
    return try_load_file_and_process(folder, file_name)


if __name__ == "__main__":
    load_PA_and_filter()
    load_PC_and_filter()

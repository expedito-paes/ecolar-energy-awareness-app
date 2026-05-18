# consumption_repository.py

# from = usado para importar partes específicas de outro arquivo
# import = traz funções/classes/módulos para este arquivo

# Importa função responsável por ler arquivos TXT
# utils = pasta de utilidades auxiliares do sistema
from utils.txt_handler import read_txt_file

# def = usado para criar funções
# get_all_consumption_levels = função responsável por buscar todos os níveis de consumo
def get_all_consumption_levels():
    # Lista vazia onde os níveis serão armazenados
    levels = []
    # Chama função responsável por ler o TXT
    # "./data/consumption_levels.txt" = caminho do arquivo
    # 5 = quantidade esperada de colunas por linha
    data_list = read_txt_file(
        "./data/consumption_levels.txt",
        5
    )
    # for = estrutura de repetição
    # percorre todos os dados do arquivo

    # enumerate() = adiciona contador ao loop
    # line_number = número da linha
    # data = conteúdo da linha
    # start=1 = contador começa em 1
    for line_number, data in enumerate(data_list, start=1):
        # try = tenta executar bloco
        # usado para evitar quebra do sistema
        try:
            # Cria dicionário representando nível de consumo
            # dict = estrutura chave:valor
            level = {
                # data[0] = primeira coluna do TXT
                "id": data[0],
                # Nome do nível
                "level": data[1],
                # Perfil da residência
                "house_profile": data[2],
                # Faixa de consumo
                "range": data[3],
                # Perfil resumido
                "profile": data[4]
            }
            # append() = adiciona item na lista
            levels.append(level)

        # except = executa caso aconteça erro
        # Exception = captura qualquer tipo de erro
        except Exception:
            
            # f"" = f-string
            # permite inserir variáveis dentro do texto
            print(
                # Mostra aviso da linha problemática
                f"[AVISO] Linha {line_number} "
                # Complementa mensagem
                f"ignorada em consumption_levels.txt"
            )
    # return = devolve valor da função
    # retorna lista completa dos níveis de consumo
    return levels
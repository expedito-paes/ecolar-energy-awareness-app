# category_repository.py

# from = usado para importar partes específicas de outro arquivo
# import = traz funções/classes/módulos para este arquivo

# Importa função responsável por ler arquivos TXT
# utils = pasta de utilidades auxiliares do sistema
from utils.txt_handler import read_txt_file

# def = usado para criar funções
# get_all_categories = função responsável por buscar todas as categorias
def get_all_categories():
    # Lista vazia onde as categorias serão armazenadas
    categories = []
    # Chama função que lê arquivo TXT
    # "./data/categories.txt" = caminho do arquivo
    # 3 = quantidade esperada de colunas por linha
    data_list = read_txt_file(
        "./data/categories.txt",
        3
    )

    # for = estrutura de repetição
    # percorre todos os dados do arquivo

    # enumerate() = adiciona contador durante repetição
    # line_number = número da linha
    # data = conteúdo da linha
    # start=1 = contador começa em 1
    for line_number, data in enumerate(data_list, start=1):
        # try = tenta executar bloco
        # usado para evitar quebra do sistema
        try:
            # Cria dicionário da categoria
            # dict = estrutura chave:valor
            category = {
                # data[0] = primeira coluna do TXT
                "id": data[0],
                # Nome da categoria
                "name": data[1],
                # Descrição da categoria
                "description": data[2]
            }
            # append() = adiciona item na lista
            categories.append(category)

        # except = executa caso aconteça erro
        # Exception = captura qualquer tipo de erro
        except Exception:
            
            # f"" = f-string
            # permite inserir variáveis dentro do texto
            print(
                # Mostra aviso da linha problemática
                f"[AVISO] Linha {line_number} "
                # Complementa mensagem
                f"ignorada em categories.txt"
            )
    # return = devolve valor da função
    # retorna lista completa das categorias
    return categories
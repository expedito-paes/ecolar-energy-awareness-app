# tip_repository.py

# from = usado para importar partes específicas de outro arquivo
# import = traz funções/classes/módulos para este arquivo

# Importa função responsável por ler arquivos TXT
# utils = pasta de utilidades auxiliares do sistema
from utils.txt_handler import read_txt_file


# def = usado para criar funções
# get_all_tips = função responsável por buscar todas as dicas

def get_all_tips():

    # Lista vazia onde as dicas serão armazenadas
    tips = []


    # Chama função responsável por ler o arquivo TXT
    # "./data/tips.txt" = caminho do arquivo
    # 3 = quantidade esperada de colunas por linha
    data_list = read_txt_file(
        "./data/tips.txt",
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


            # Cria dicionário representando dica
            # dict = estrutura chave:valor
            tip = {

                # ID da dica
                "id": data[0],

                # Aparelho relacionado à dica
                "appliance": data[1],

                # Texto da dica
                "tip": data[2]
            }


            # append() = adiciona item na lista
            tips.append(tip)


        # except = executa caso aconteça erro
        # Exception = captura qualquer tipo de erro
        except Exception:


            # f"" = f-string
            # permite inserir variáveis dentro do texto
            print(

                # Mostra aviso da linha problemática
                f"[AVISO] Linha {line_number} "

                # Complementa mensagem
                f"ignorada em tips.txt"
            )


    # return = devolve valor da função
    # retorna lista completa das dicas
    return tips
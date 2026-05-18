# history_repository.py

# from = usado para importar partes específicas de outro arquivo
# import = traz funções/classes/módulos para este arquivo

# Importa função responsável por ler arquivos TXT
# utils = pasta de utilidades auxiliares do sistema
from utils.txt_handler import read_txt_file


# def = usado para criar funções
# get_all_history = função responsável por buscar todo o histórico

def get_all_history():

    # Lista vazia onde o histórico será armazenado
    history = []


    # Chama função responsável por ler o arquivo TXT
    # "./data/history.txt" = caminho do arquivo
    # 5 = quantidade esperada de colunas por linha
    data_list = read_txt_file(
        "./data/history.txt",
        5
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


            # Cria dicionário representando item do histórico
            # dict = estrutura chave:valor
            history_item = {

                # Data do registro
                "data": data[0],

                # Usuário relacionado ao histórico
                "user": data[1],

                # Aparelho relacionado
                "appliance": data[2],

                # float() = converte valor para número decimal
                # Consumo energético registrado
                "consumption": float(data[3]),

                # Custo financeiro do consumo
                "cost": float(data[4])
            }


            # append() = adiciona item na lista
            history.append(history_item)


        # except = executa caso aconteça erro
        # ValueError = erro de conversão numérica
        except ValueError:


            # f"" = f-string
            # permite inserir variáveis dentro do texto
            print(

                # Mostra aviso da linha problemática
                f"[AVISO] Linha {line_number} "

                # Complementa mensagem
                f"ignorada em history.txt"
            )


    # return = devolve valor da função
    # retorna lista completa do histórico
    return history
# from = usado para importar partes específicas de outro arquivo
# import = traz funções/classes/módulos para este arquivo

# Importa função responsável por ler arquivos TXT
# utils = pasta de utilidades auxiliares do sistema
from utils.txt_handler import read_txt_file


# def = usado para criar funções
# get_all_users = função responsável por buscar todos os usuários

def get_all_users():

    # Lista vazia onde os usuários serão armazenados
    users = []


    # Chama função responsável por ler o arquivo TXT
    # "./data/users.txt" = caminho do arquivo
    # 5 = quantidade esperada de colunas por linha
    data_list = read_txt_file(
        "./data/users.txt",
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


            # Cria dicionário representando usuário
            # dict = estrutura chave:valor
            user = {

                # ID do usuário
                "id": data[0],

                # Nome do usuário
                "name": data[1],

                # E-mail do usuário
                "email": data[2],

                # Data de aniversário
                "birthday": data[3],

                # Perfil de consumo
                "profile": data[4]
            }


            # append() = adiciona item na lista
            users.append(user)


        # except = executa caso aconteça erro
        # Exception = captura qualquer tipo de erro
        except Exception:


            # f"" = f-string
            # permite inserir variáveis no texto
            print(

                # Mostra aviso da linha problemática
                f"[AVISO] Linha {line_number} "

                # Complementa mensagem
                f"ignorada em users.txt"
            )


    # return = devolve valor da função
    # retorna lista completa de usuários
    return users



# Função responsável por gerar próximo ID do usuário
def get_next_user_id():

    # Busca todos os usuários cadastrados
    users = get_all_users()

    # Verifica se lista de usuário está vazia
    if not users:
        # Retorna primeiro ID do sistema
        return "001"
    
    # max() = retorna maior valor encontrado
    # int() = converte ID texto para inteiro
    # for = percorre usuários
    last_id = max(
        # Obtém ID de cada usuário
        int(user["id"])
        # Percorre lista de usuários
        for user in users
    )

    # len() = retorna quantidade de itens da lista
    # + 1 = gera próximo ID
    # str() = converte número para texto
    # zfill(3) = completa com zeros à esquerda
    # Exemplo:
    # 1 -> 001
    # 15 -> 015
    return str(last_id + 1).zfill(3)



# Função responsável por salvar usuário no TXT
def create_user_repository(user):


    # try = tenta executar bloco
    try:


        # with open() = abre arquivo TXT

        # with = gerencia fechamento automático do arquivo
        # open() = abre arquivo

        # "./data/users.txt" = caminho do arquivo

        # "a" = modo append
        # adiciona conteúdo sem apagar existente

        # encoding="utf-8" = suporta caracteres especiais
        with open(
            "./data/users.txt",
            "a",
            encoding="utf-8"
        ) as file:


            # write() = escreve no arquivo TXT
            file.write(

                # f"" = f-string
                # permite inserir variáveis no texto

                # ID do usuário
                f"{user['id']};"

                # Nome
                f"{user['name']};"

                # E-mail
                f"{user['email']};"

                # Data de aniversário
                f"{user['birthday']};"

                # Perfil de consumo

                # \n = quebra de linha
                f"{user['profile']}\n"
            )


    # except = executa caso erro aconteça
    # Exception = captura qualquer tipo de erro
    except Exception as error:


        # print() = exibe mensagem no terminal
        print(

            # Mostra mensagem de erro
            f"[ERRO] Falha ao salvar usuário: "

            # Mostra detalhe do erro
            f"{error}"
        )



# Função responsável por buscar usuário pelo e-mail
def get_user_by_email(email):


    # Busca todos os usuários cadastrados
    users = get_all_users()


    # for = percorre lista de usuários
    for user in users:


        # Verifica se e-mail encontrado é igual ao digitado
        if user["email"] == email:


            # return = devolve usuário encontrado
            return user


    # Caso não encontre usuário
    # None = ausência de valor
    return None
# user_view.py

# Sem precisar alterar services/repositories

# def = usado para criar funções
# show_user_registration_title = função responsável
# por exibir título do cadastro

def show_user_registration_title():

    # print() = exibe texto no terminal
    # \n = quebra de linha
    print("\n===== CADASTRO DE USUÁRIO =====\n")

# Função responsável por solicitar nome do usuário
def get_user_name():

    # return = devolve valor da função
    # input() = captura texto digitado no terminal
    return input("Digite seu nome: ")

# Função responsável por solicitar e-mail
def get_user_email():

    # Captura e devolve e-mail digitado
    return input("Digite seu e-mail: ")

# Função responsável por solicitar data de aniversário
def get_user_birthday():

    # Captura e devolve data digitada
    return input("Digite sua data de aniversário: ")

# Função responsável por exibir mensagens de erro
def show_error(message):

    # f"" = f-string
    # permite inserir variáveis dentro do texto
    # message = mensagem recebida como parâmetro
    print(f"\n[ERRO] {message}")

# Função responsável por exibir mensagens de sucesso
def show_success(message):

    # Exibe mensagem formatada de sucesso
    print(f"\n[SUCESSO] {message}")

# Função responsável por solicitar perfil de consumo do usuário
def get_profile_option():
    #input() = captura texto digitado no terminal
    #return = devolve valor digitado
    return input("\nEscolha o ID do perfil: ")

# Exibe informações do usuário
def show_user_profile(user):

    print("\n===== MEU PERFIL =====")

    print(f"ID: {user['id']}")
    print(f"Nome: {user['name']}")
    print(f"E-mail: {user['email']}")
    print(f"Nascimento: {user['birthday']}")
    print(f"Perfil de consumo: {user['profile']}")
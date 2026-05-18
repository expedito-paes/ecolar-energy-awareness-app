# menu_view.py

# def = usado para criar funções
# show_main_menu = função responsável por exibir
# o menu principal do sistema
def show_main_menu():

    # print() = exibe texto no terminal
    # \n = quebra de linha
    print("\n==============================")
    print("        SISTEMA ECOLAR")
    print("==============================")

    # Exibe opção de login
    print("1 - Login")
    # Exibe opção de cadastro de usuário
    print("2 - Cadastrar usuário")
    # Exibe opção de saída do sistema
    print("0 - Sair")

# Função responsável por exibir o menu do usuário
def show_user_menu():

    # print() = exibe texto no terminal
    print("\n==============================")
    print("         MENU DO USUÁRIO")
    print("==============================")

    # opções do sistema
    print("1 - Meu Perfil")
    print("2 - Meus aparelhos")
    print("3 - Atualizar cadastro")
    print("4 - Consumo energético")
    print("5 - Relatórios")
    print("6 - Recomendações")
    print("7 - Simular Economia")
    print("8 - Excluir Conta")
    print("0 - Logout")
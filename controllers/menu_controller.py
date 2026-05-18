# menu_controller.py

# from = usado para importar partes específicas de outro arquivo
# import = traz funções/classes/módulos para este arquivo

# Importa função responsável por exibir o menu principal
# views = camada responsável pela interface textual do sistema
from views.menu_view import show_main_menu

# Importa controllers relacionados ao usuário
# controllers = camada responsável por controlar o fluxo do sistema
from controllers.user_controller import (
    # Função responsável pelo cadastro de usuários
    create_user_controller,
    # Função responsável pelo login
    login_user_controller
)
# Importa função de validação do menu
from utils.validators import (
    # Verifica se opção digitada existe no menu
    validate_menu_option
)

# def = usado para criar funções
# start_system = função principal que inicia o sistema
def start_system():

    # while = estrutura de repetição
    # True = cria loop infinito até encontrar break
    while True:
        # exibe menu principal
        show_main_menu()

        # input() = captura texto digitado no terminal
        # \n = quebra de linha
        option = input("\nEscolha uma opção: ")

        # if = estrutura condicional
        # not = inverte resultado lógico
        # Verifica se opção digitada NÃO é válida
        if not validate_menu_option(
            # valor digitado pelo usuário
            option,
            # lista de opções válidas
            ["1", "2", "0"]
        ):
            # print() = exibe texto no terminal
            print("\nOpção inválida.")
            # continue = reinicia loop atual
            # Faz menu aparecer novamente
            continue
        
         # Verifica se usuário escolheu login
        if option == "1":
            # Chama controller de login
            login_user_controller()
        
        # elif = outra condição
        # Verifica se usuário escolheu cadastro
        elif option == "2":
            # Chama controller de cadastro
            create_user_controller()
        # Verifica se usuário deseja sair
        elif option == "0":
            # Exibe mensagem de encerramento
            print("\nSistema encerrado.")
            # break = encerra loop atual
            # Finaliza sistema
            break

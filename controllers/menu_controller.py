from views.menu_view import show_main_menu

from controllers.user_controller import (
    create_user_controller,
    login_user_controller
)

def start_system():

    while True:

        show_main_menu()

        option = input("\nEscolha uma opção: ")

        if option == "1":
            login_user_controller()
        
        elif option == "2":
            create_user_controller()
        
        elif option == "0":
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpção inválida.")
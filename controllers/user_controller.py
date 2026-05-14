from services.user_service import (
    create_user_service,
    login_user_service
)

from services.user_appliance_service import (
    create_user_appliance_service
    )

from repositories.appliance_repository import (
    get_all_appliances
)

from repositories.consumption_repository import (
    get_all_consumption_levels
)

from views.user_view import (
    show_user_registration_title,
    get_user_name,
    get_user_email,
    get_user_birthday,
    show_error,
    show_success
)

from views.appliance_view import show_appliance

from views.consumption_view import show_consumption_levels

#cadastro do usuário
def create_user_controller():

    show_user_registration_title()

    name = get_user_name()
    email = get_user_email()
    birthday = get_user_birthday()

    levels = get_all_consumption_levels()

    show_consumption_levels(levels)

    profile = input("\nEscolha o ID do perfil: ")

    user, error = create_user_service(
        name,
        email,
        birthday,
        profile
    )

    if error:
        show_error(error)
        return


    #cadastro dos aparelhos usados pelo usuário
    appliances = get_all_appliances()

    show_appliance(appliances)

    while True:
        appliance_id = input(
            "\nDigite o ID do aparelho"
            "(ou 0 para finalizar): "
        )

        if appliance_id == "0":
            break

        daily_usage = input(
            "Tempo médio diário de uso (minutos): "
        )

        monthly_days = input(
            "Quantos dias por mês utiliza: "
        )

        create_user_appliance_service(
            user["id"],
            appliance_id,
            daily_usage,
            monthly_days
        )

    show_success("Cadastro concluído!")

def login_user_controller():

    email = input("\nDigite seu e-mail: ")

    user, error = login_user_service(email)

    if error:
        show_error(error)
        return
    
    show_success(
        f"Bem-vindo, {user['name']}!"
    )

    user_menu_controller(user)

def user_menu_controller(user):

     while True:

        print("\n===== MENU DO USUÁRIO =====")
        print("1 - Atualizar cadastro")
        print("2 - Relatórios")
        print("3 - Gerenciar aparelhos")
        print("4 - Excluir conta")
        print("0 - Logout")

        option = input("\nEscolha uma opção: ")

        if option == "1":
            print("Função em desenvolvimento.")
            
        elif option == "2":
            print("Função em desenvolvimento.")
            
        elif option == "3":
            print("Função em desenvolvimento.")

        elif option == "4":
            print("Função em desenvolvimento.")

        elif option == "0":
            print("\nLogout realizado.")
            break

        else:
            print("\nOpção inválida.")
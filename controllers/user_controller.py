# user_controller.py
# Controller responsável pelo fluxo do usuário

# Importa services relacionados ao usuário
from services.user_service import (
    create_user_service,
    login_user_service
)

# Importa service responsável pelos aparelhos do usuário
from services.user_appliance_service import (
    create_user_appliance_service
)

# Importa services auxiliares
from services.appliance_service import (
    get_all_appliances_service
)

from services.consumption_service import (
    get_consumption_levels_service
)

# Importa controllers de relatórios
from controllers.report_controller import (
    show_consumption_report_controller,
    show_recommendations_controller,
    show_simulation_controller
)

# Importa views do usuário
from views.user_view import (
    show_user_registration_title,
    get_user_name,
    get_user_email,
    get_user_birthday,
    get_profile_option,
    show_error,
    show_success,
    show_user_profile
)

# Importa views de aparelhos
from views.appliance_view import (
    show_appliance,
    get_appliance_id,
    get_daily_usage,
    get_monthly_days
)

# Importa view de consumo
from views.consumption_view import (
    show_consumption_levels
)

# Importa menu do usuário
from views.menu_view import (
    show_user_menu
)

# Importa validações
from utils.validators import (
    validate_menu_option,
    validate_existing_id
)

# Controller responsável pelo cadastro de usuários
def create_user_controller():

    # Exibe título da tela
    show_user_registration_title()

    # Captura dados do usuário
    name = get_user_name()
    email = get_user_email()
    birthday = get_user_birthday()

    # Busca perfis disponíveis
    levels = get_consumption_levels_service()

    # Exibe perfis
    show_consumption_levels(levels)

    # Captura perfil escolhido
    profile = get_profile_option()

    # Chama service responsável pela criação
    user, error = create_user_service(
        name,
        email,
        birthday,
        profile
    )

    # Verifica se ocorreu erro
    if error:

        show_error(error)
        return

    # Exibe mensagem de sucesso
    show_success("Usuário cadastrado com sucesso.")

# Controller responsável pelo login
def login_user_controller():

    print("\n===== LOGIN =====")

    # Captura e-mail digitado
    email = get_user_email()

    # Chama service de login
    user, error = login_user_service(email)

    # Verifica erro
    if error:

        show_error(error)
        return

    # Exibe sucesso
    show_success(f"Bem-vindo, {user['name']}.")

    # Abre menu do usuário
    user_menu_controller(user)

# Controller responsável pelo menu do usuário
def user_menu_controller(user):

    # Loop principal do menu
    while True:

        # Exibe menu
        show_user_menu()

        # Captura opção
        option = input("\nEscolha uma opção: ")

        # Valida opção
        if not validate_menu_option(
            option,
            ["1", "2", "3", "4", "5", "6", "7", "0"]
        ):

            show_error("Opção inválida.")
            continue

        # Meu perfil
        if option == "1":

            show_profile_controller(user)

        # Gerenciar aparelhos
        elif option == "2":

            add_user_appliance_controller(user)

        # Consumo energético
        elif option == "3":

            show_consumption_report_controller(user)

        # Relatórios
        elif option == "4":

            show_consumption_report_controller(user)

        # Recomendações
        elif option == "5":

            show_recommendations_controller(user)

        # Simulação
        elif option == "6":

            show_simulation_controller(user)

        # Excluir conta
        elif option == "7":

            delete_user_controller(user)
            break

        # Logout
        elif option == "0":

            print("\nLogout realizado.")
            break

# Controller responsável por exibir perfil
def show_profile_controller(user):

    show_user_profile(user)

# Controller responsável por adicionar aparelhos
def add_user_appliance_controller(user):

    # Busca aparelhos disponíveis
    appliances = get_all_appliances_service()

    # Exibe aparelhos
    show_appliance(appliances)

    # Lista contendo IDs válidos
    valid_ids = []

    # Percorre aparelhos
    for appliance in appliances:

        valid_ids.append(appliance["id"])

    # Loop de cadastro
    while True:

        # Captura ID do aparelho
        appliance_id = get_appliance_id()

        # Finaliza cadastro
        if appliance_id == "0":

            break

        # Valida existência do ID
        if not validate_existing_id(
            appliance_id,
            valid_ids
        ):

            show_error("ID de aparelho inválido.")
            continue

        # Captura uso diário
        daily_usage = get_daily_usage()

        # Captura dias mensais
        monthly_days = get_monthly_days()

        # Chama service
        error = create_user_appliance_service(
            user["id"],
            appliance_id,
            daily_usage,
            monthly_days
        )

        # Verifica erro
        if error:

            show_error(error)

        else:

            show_success(
                "Aparelho cadastrado com sucesso."
            )

# Controller responsável pela exclusão do usuário
def delete_user_controller(user):

    print(
        f"\nUsuário {user['name']} removido do sistema."
    )
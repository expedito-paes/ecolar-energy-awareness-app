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

# Importa controller responsável por listar aparelhos
from controllers.appliance_controller import (
    list_user_appliances_controller
)

# Importa repositórios de usuários
from repositories.user_repository import (
    update_user_repository,
    delete_user_repository
)

# Importa repositories dos aparelhos de usuário
from repositories.user_appliance_repository import (

    # Busca aparelhos do usuário
    get_user_appliances_by_user_id,

    # Atualiza vínculo usuário/aparelho
    update_user_appliance_repository,

    # Remove vínculo específico
    delete_user_appliance_repository,

    # Remove todos os aparelhos do usuário
    delete_user_appliances_by_user_id
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
    validate_existing_id,
    validate_email,
    validate_name,
    validate_positive_number,
    validate_date
)

# Controller responsável pelo cadastro de usuários
def create_user_controller():

    # Exibe título
    show_user_registration_title()

    # Captura dados
    name = get_user_name()

    email = get_user_email()

    birthday = get_user_birthday()

    # Valida data
    if not validate_date(birthday):

        show_error("Data inválida.")
        return

    # Busca níveis de consumo
    levels = get_consumption_levels_service()

    # Exibe perfis
    show_consumption_levels(levels)

    # Captura perfil
    profile = get_profile_option()

    # Lista de perfis válidos
    valid_profiles = [
        "001",
        "002",
        "003",
        "004"
    ]

    # Verifica perfil
    if not validate_existing_id(
        profile,
        valid_profiles
    ):

        show_error("Perfil inválido.")
        return

    # Chama service
    user, error = create_user_service(
        name,
        email,
        birthday,
        profile
    )

    # Verifica erro
    if error:

        show_error(error)
        return

    # Sucesso
    show_success(
        "Usuário cadastrado com sucesso."
    )

# Controller responsável pelo login
def login_user_controller():

    print("\n===== LOGIN =====")

    # Captura e-mail
    email = get_user_email()

    # Realiza login
    user, error = login_user_service(email)

    # Verifica erro
    if error:

        show_error(error)
        return

    # Exibe sucesso
    show_success(
        f"Bem-vindo, {user['name']}."
    )

    # Abre menu
    user_menu_controller(user)

# Controller responsável pelo menu do usuário
def user_menu_controller(user):

    # Loop principal
    while True:

        # Exibe menu
        show_user_menu()

        # Captura opção
        option = input(
            "\nEscolha uma opção: "
        )

        # Valida opção
        if not validate_menu_option(
            option,
            ["1", "2", "3", "4", "5", "6", "7", "8", "0"]
        ):

            show_error("Opção inválida.")
            continue

        # Meu perfil
        if option == "1":

            show_profile_controller(user)

        # Meus aparelhos
        elif option == "2":

            list_user_appliances_controller(user)

        # Atualizar cadastro
        elif option == "3":

            update_user_menu_controller(user)

        # Consumo energético
        elif option == "4":

            show_consumption_report_controller(user)

        # Relatórios
        elif option == "5":

            show_consumption_report_controller(user)

        # Recomendações
        elif option == "6":

            show_recommendations_controller(user)

        # Simulação
        elif option == "7":

            show_simulation_controller(user)

        # Excluir conta
        elif option == "8":

            delete_user_controller(user)
            break

        # Logout
        elif option == "0":

            print("\nLogout realizado.")
            break

# Exibe perfil do usuário
def show_profile_controller(user):

    show_user_profile(user)

# Controller responsável por adicionar aparelhos
def add_user_appliance_controller(user):

    # Busca aparelhos disponíveis
    appliances = get_all_appliances_service()

    # Exibe aparelhos
    show_appliance(appliances)

    # Lista de IDs válidos
    valid_ids = []

    # Percorre aparelhos
    for appliance in appliances:

        valid_ids.append(
            appliance["id"]
        )

    # Busca aparelhos já cadastrados
    existing_appliances = (
        get_user_appliances_by_user_id(
            user["id"]
        )
    )

    # Loop principal
    while True:

        # Captura ID
        appliance_id = get_appliance_id()

        # Finaliza cadastro
        if appliance_id == "0":

            break

        # Verifica se ID existe
        if not validate_existing_id(
            appliance_id,
            valid_ids
        ):

            show_error(
                "ID de aparelho inválido."
            )

            continue

        # Variável de controle
        already_exists = False

        # Percorre aparelhos existentes
        for appliance in existing_appliances:

            # Verifica duplicidade
            if (
                appliance["appliance_id"]
                ==
                appliance_id
            ):

                already_exists = True
                break

        # Verifica duplicidade
        if already_exists:

            show_error(
                "Aparelho já cadastrado."
            )

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

# Menu responsável pelas atualizações
def update_user_menu_controller(user):

    while True:

        print("\n===== ATUALIZAR CADASTRO =====")

        print("1 - Atualizar nome")
        print("2 - Atualizar e-mail")
        print("3 - Atualizar perfil energético")
        print("4 - Adicionar aparelho")
        print("5 - Atualizar uso do aparelho")
        print("6 - Remover aparelho")
        print("0 - Voltar")

        option = input(
            "\nEscolha uma opção: "
        )

        # Atualizar nome
        if option == "1":

            update_user_name_controller(user)

        # Atualizar e-mail
        elif option == "2":

            update_user_email_controller(user)

        # Atualizar perfil
        elif option == "3":

            update_user_profile_controller(user)

        # Adicionar aparelho
        elif option == "4":

            add_user_appliance_controller(user)

        # Atualizar uso
        elif option == "5":

            update_user_appliance_controller(user)

        # Remover aparelho
        elif option == "6":

            remove_user_appliance_controller(user)

        # Voltar
        elif option == "0":

            break

        # Opção inválida
        else:

            show_error("Opção inválida.")

# Atualiza nome do usuário
def update_user_name_controller(user):

    # Captura novo nome
    new_name = input("\nNovo nome: ")

    # Valida nome
    if not validate_name(new_name):

        show_error("Nome inválido.")
        return

    # Atualiza nome
    user["name"] = new_name

    # Salva alteração
    update_user_repository(user)

    # Exibe sucesso
    show_success(
        "Nome atualizado com sucesso."
    )

# Atualiza e-mail
def update_user_email_controller(user):

    # Captura novo e-mail
    new_email = input("\nNovo e-mail: ")

    # Valida e-mail
    if not validate_email(new_email):

        show_error("E-mail inválido.")
        return

    # Atualiza e-mail
    user["email"] = new_email

    # Salva alteração
    update_user_repository(user)

    # Exibe sucesso
    show_success(
        "E-mail atualizado com sucesso."
    )

# Atualiza perfil energético
def update_user_profile_controller(user):

    # Busca perfis
    levels = get_consumption_levels_service()

    # Exibe perfis
    show_consumption_levels(levels)

    # Captura perfil
    new_profile = input(
        "\nNovo perfil de consumo: "
    )

    # Lista válida
    valid_profiles = [
        "001",
        "002",
        "003",
        "004"
    ]

    # Verifica perfil
    if not validate_existing_id(
        new_profile,
        valid_profiles
    ):

        show_error("Perfil inválido.")
        return

    # Atualiza perfil
    user["profile"] = new_profile

    # Salva alteração
    update_user_repository(user)

    # Exibe sucesso
    show_success(
        "Perfil atualizado com sucesso."
    )

# Atualiza uso do aparelho
def update_user_appliance_controller(user):

    # Busca aparelhos do usuário
    user_appliances = (
        get_user_appliances_by_user_id(
            user["id"]
        )
    )

    # Verifica existência
    if not user_appliances:

        show_error(
            "Nenhum aparelho cadastrado."
        )

        return

    print("\n===== ATUALIZAR APARELHO =====")

    # Lista de IDs válidos
    valid_ids = []

    # Exibe aparelhos
    for appliance in user_appliances:

        print(
            f"Aparelho ID: "
            f"{appliance['appliance_id']}"
        )

        valid_ids.append(
            appliance["appliance_id"]
        )

    # Captura ID
    appliance_id = input(
        "\nDigite o ID do aparelho: "
    )

    # Valida ID
    if not validate_existing_id(
        appliance_id,
        valid_ids
    ):

        show_error(
            "Aparelho inválido."
        )

        return

    # Captura uso diário
    daily_usage = input(
        "Novo tempo diário (min): "
    )

    # Captura dias mensais
    monthly_days = input(
        "Novos dias mensais: "
    )

    # Valida uso diário
    if not validate_positive_number(
        daily_usage
    ):

        show_error(
            "Tempo diário inválido."
        )

        return

    # Valida dias mensais
    if not validate_positive_number(
        monthly_days
    ):

        show_error(
            "Dias mensais inválidos."
        )

        return

    # Cria novo vínculo
    updated_appliance = {

        "user_id": user["id"],

        "appliance_id": appliance_id,

        "daily_usage": int(
            daily_usage
        ),

        "monthly_days": int(
            monthly_days
        )
    }

    # Atualiza vínculo
    success = (
        update_user_appliance_repository(
            updated_appliance
        )
    )

    # Verifica resultado
    if success:

        show_success(
            "Uso do aparelho atualizado."
        )

    else:

        show_error(
            "Aparelho não encontrado."
        )

# Remove aparelho do usuário
def remove_user_appliance_controller(user):

    # Busca aparelhos do usuário
    user_appliances = (
        get_user_appliances_by_user_id(
            user["id"]
        )
    )

    # Verifica existência
    if not user_appliances:

        show_error(
            "Nenhum aparelho cadastrado."
        )

        return

    print("\n===== REMOVER APARELHO =====")

    # Lista válida
    valid_ids = []

    # Exibe aparelhos
    for appliance in user_appliances:

        print(
            f"Aparelho ID: "
            f"{appliance['appliance_id']}"
        )

        valid_ids.append(
            appliance["appliance_id"]
        )

    # Captura ID
    appliance_id = input(
        "\nDigite o ID do aparelho: "
    )

    # Valida ID
    if not validate_existing_id(
        appliance_id,
        valid_ids
    ):

        show_error(
            "Aparelho inválido."
        )

        return

    # Remove aparelho
    success = (
        delete_user_appliance_repository(
            user["id"],
            appliance_id
        )
    )

    # Verifica resultado
    if success:

        show_success(
            "Aparelho removido."
        )

    else:

        show_error(
            "Aparelho não encontrado."
        )

# Remove usuário do sistema
def delete_user_controller(user):

    # Remove aparelhos do usuário
    delete_user_appliances_by_user_id(
        user["id"]
    )

    # Remove usuário
    success = delete_user_repository(
        user["id"]
    )

    # Verifica resultado
    if success:

        show_success(
            f"Usuário {user['name']} removido."
        )

    else:

        show_error(
            "Erro ao remover usuário."
        )
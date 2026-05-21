# user_controller.py

from services.user_service import (
    create_user_service,
    login_user_service
)

from services.user_appliance_service import (
    create_user_appliance_service
)

from services.appliance_service import (
    get_all_appliances_service
)

from services.consumption_service import (
    get_consumption_levels_service
)

from controllers.report_controller import (
    show_consumption_report_controller,
    show_recommendations_controller,
    show_simulation_controller
)

from controllers.appliance_controller import (
    list_user_appliances_controller
)

from repositories.user_repository import (
    update_user_repository,
    delete_user_repository
)

from repositories.user_appliance_repository import (
    get_user_appliances_by_user_id,
    update_user_appliance_repository,
    delete_user_appliance_repository,
    delete_user_appliances_by_user_id
)

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

from views.appliance_view import (
    show_appliance,
    get_appliance_id,
    get_daily_usage,
    get_monthly_days
)

from views.consumption_view import (
    show_consumption_levels
)

from views.menu_view import (
    show_user_menu
)

from utils.validators import (
    validate_menu_option,
    validate_existing_id,
    validate_email,
    validate_name,
    validate_positive_number,
    validate_date
)

def create_user_controller():

    show_user_registration_title()

    name = get_user_name()

    email = get_user_email()

    birthday = get_user_birthday()

    if not validate_date(birthday):

        show_error("Data inválida.")
        return

    levels = get_consumption_levels_service()

    show_consumption_levels(levels)

    profile = get_profile_option()

    valid_profiles = [
        "001",
        "002",
        "003",
        "004"
    ]

    if not validate_existing_id(
        profile,
        valid_profiles
    ):

        show_error("Perfil inválido.")
        return

    user, error = create_user_service(
        name,
        email,
        birthday,
        profile
    )

    if error:

        show_error(error)
        return

    show_success(
        "Usuário cadastrado com sucesso."
    )

def login_user_controller():

    print("\n===== LOGIN =====")

    email = get_user_email()

    user, error = login_user_service(email)

    if error:

        show_error(error)
        return

    show_success(
        f"Bem-vindo, {user['name']}."
    )

    user_menu_controller(user)

def user_menu_controller(user):

    while True:

        show_user_menu()

        option = input(
            "\nEscolha uma opção: "
        )

        if not validate_menu_option(
            option,
            ["1", "2", "3", "4", "5", "6", "7", "8", "0"]
        ):

            show_error("Opção inválida.")
            continue

        if option == "1":

            show_profile_controller(user)

        elif option == "2":

            list_user_appliances_controller(user)

        elif option == "3":

            update_user_menu_controller(user)

        elif option == "4":

            show_consumption_report_controller(user)

        elif option == "5":

            show_consumption_report_controller(user)

        elif option == "6":

            show_recommendations_controller(user)

        elif option == "7":

            show_simulation_controller(user)

        elif option == "8":

            delete_user_controller(user)
            break

        elif option == "0":

            print("\nLogout realizado.")
            break

def show_profile_controller(user):

    show_user_profile(user)

def add_user_appliance_controller(user):

    appliances = get_all_appliances_service()

    show_appliance(appliances)

    valid_ids = []

    for appliance in appliances:

        valid_ids.append(
            appliance["id"]
        )

    existing_appliances = (
        get_user_appliances_by_user_id(
            user["id"]
        )
    )

    while True:

        appliance_id = get_appliance_id()

        if appliance_id == "0":

            break

        if not validate_existing_id(
            appliance_id,
            valid_ids
        ):

            show_error(
                "ID de aparelho inválido."
            )

            continue

        already_exists = False

        for appliance in existing_appliances:

            if (
                appliance["appliance_id"]
                ==
                appliance_id
            ):

                already_exists = True
                break

        if already_exists:

            show_error(
                "Aparelho já cadastrado."
            )

            continue

        daily_usage = get_daily_usage()

        monthly_days = get_monthly_days()

        error = create_user_appliance_service(
            user["id"],
            appliance_id,
            daily_usage,
            monthly_days
        )

        if error:

            show_error(error)

        else:

            show_success(
                "Aparelho cadastrado com sucesso."
            )

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

        if option == "1":

            update_user_name_controller(user)

        elif option == "2":

            update_user_email_controller(user)

        elif option == "3":

            update_user_profile_controller(user)

        elif option == "4":

            add_user_appliance_controller(user)

        elif option == "5":

            update_user_appliance_controller(user)

        elif option == "6":

            remove_user_appliance_controller(user)

        elif option == "0":

            break

        else:

            show_error("Opção inválida.")

def update_user_name_controller(user):

    new_name = input("\nNovo nome: ")

    if not validate_name(new_name):

        show_error("Nome inválido.")
        return

    user["name"] = new_name

    update_user_repository(user)

    show_success(
        "Nome atualizado com sucesso."
    )

def update_user_email_controller(user):

    new_email = input("\nNovo e-mail: ")

    if not validate_email(new_email):

        show_error("E-mail inválido.")
        return

    user["email"] = new_email

    update_user_repository(user)

    show_success(
        "E-mail atualizado com sucesso."
    )

def update_user_profile_controller(user):

    levels = get_consumption_levels_service()

    show_consumption_levels(levels)

    new_profile = input(
        "\nNovo perfil de consumo: "
    )

    valid_profiles = [
        "001",
        "002",
        "003",
        "004"
    ]

    if not validate_existing_id(
        new_profile,
        valid_profiles
    ):

        show_error("Perfil inválido.")
        return

    user["profile"] = new_profile

    update_user_repository(user)

    show_success(
        "Perfil atualizado com sucesso."
    )

def update_user_appliance_controller(user):

    user_appliances = (
        get_user_appliances_by_user_id(
            user["id"]
        )
    )

    if not user_appliances:

        show_error(
            "Nenhum aparelho cadastrado."
        )

        return

    print("\n===== ATUALIZAR APARELHO =====")

    valid_ids = []

    for appliance in user_appliances:

        print(
            f"Aparelho ID: "
            f"{appliance['appliance_id']}"
        )

        valid_ids.append(
            appliance["appliance_id"]
        )

    appliance_id = input(
        "\nDigite o ID do aparelho: "
    )

    if not validate_existing_id(
        appliance_id,
        valid_ids
    ):

        show_error(
            "Aparelho inválido."
        )

        return

    daily_usage = input(
        "Novo tempo diário (min): "
    )

    monthly_days = input(
        "Novos dias mensais: "
    )

    if not validate_positive_number(
        daily_usage
    ):

        show_error(
            "Tempo diário inválido."
        )

        return

    if not validate_positive_number(
        monthly_days
    ):

        show_error(
            "Dias mensais inválidos."
        )

        return

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

    success = (
        update_user_appliance_repository(
            updated_appliance
        )
    )

    if success:

        show_success(
            "Uso do aparelho atualizado."
        )

    else:

        show_error(
            "Aparelho não encontrado."
        )

def remove_user_appliance_controller(user):

    user_appliances = (
        get_user_appliances_by_user_id(
            user["id"]
        )
    )

    if not user_appliances:

        show_error(
            "Nenhum aparelho cadastrado."
        )

        return

    print("\n===== REMOVER APARELHO =====")

    valid_ids = []

    for appliance in user_appliances:

        print(
            f"Aparelho ID: "
            f"{appliance['appliance_id']}"
        )

        valid_ids.append(
            appliance["appliance_id"]
        )

    appliance_id = input(
        "\nDigite o ID do aparelho: "
    )

    if not validate_existing_id(
        appliance_id,
        valid_ids
    ):

        show_error(
            "Aparelho inválido."
        )

        return

    success = (
        delete_user_appliance_repository(
            user["id"],
            appliance_id
        )
    )

    if success:

        show_success(
            "Aparelho removido."
        )

    else:

        show_error(
            "Aparelho não encontrado."
        )

def delete_user_controller(user):

    delete_user_appliances_by_user_id(
        user["id"]
    )

    success = delete_user_repository(
        user["id"]
    )

    if success:

        show_success(
            f"Usuário {user['name']} removido."
        )

    else:

        show_error(
            "Erro ao remover usuário."
        )
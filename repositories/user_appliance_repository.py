# user_appliance_repository.py

from utils.txt_handler import read_txt_file


def get_all_user_appliances():
    user_appliances = []

    data_list = read_txt_file(
        "./data/user_appliances.txt",
        4
    )

    for line_number, data in enumerate(data_list, start=1):

        try:

            if not data[0].isdigit():
                continue
            if not data[1].isdigit():
                continue

            daily_usage = int(data[2])

            monthly_days = int(data[3])

            if (
               daily_usage < 0
               or monthly_days < 0
            ):
               continue

            user_appliance = {
                "user_id": data[0],
                "appliance_id": data[1],
                "daily_usage": daily_usage,
                "monthly_days": monthly_days,
            }

            user_appliances.append(user_appliance)

        except ValueError:

            print (
                f"[AVISO] Linha {line_number} "
                f"ignorada em user_appliances.txt"
            )

    return user_appliances


def get_user_appliances_by_user_id(user_id):

    filtered_user_appliances = []

    user_appliances = get_all_user_appliances()

    for user_appliance in user_appliances:

        if user_appliance["user_id"] == user_id:

            filtered_user_appliances.append(user_appliance)

    return filtered_user_appliances


def get_user_appliances_by_appliance_id(appliance_id):

    filtered_user_appliances = []

    user_appliances = get_all_user_appliances()

    for user_appliance in user_appliances:

        if user_appliance["appliance_id"] == appliance_id:

            filtered_user_appliances.append(user_appliance)

    return filtered_user_appliances


def save_all_user_appliances(user_appliances):

    try:

        with open(
            "./data/user_appliances.txt",
            "w",
            encoding="utf-8"
        ) as file:

            for user_appliance in user_appliances:

                file.write(
                    f"{user_appliance['user_id']};"
                    f"{user_appliance['appliance_id']};"
                    f"{user_appliance['daily_usage']};"
                    f"{user_appliance['monthly_days']}\n"
                )

    except Exception as error:

        print(
            f"[ERRO] Falha ao salvar vínculo: "
            f"{error}"
        )


def create_user_appliance_repository(user_appliance):


    try:

        required_keys = [
            "user_id",
            "appliance_id",
            "daily_usage",
            "monthly_days"
        ]

        for key in required_keys:

            if key not in user_appliance:

                print(
                    f"[ERRO] Campo obrigatório ausente: {key}"
                )

                return

        with open(
            "./data/user_appliances.txt",
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                f"{user_appliance['user_id']};"
                f"{user_appliance['appliance_id']};"
                f"{user_appliance['daily_usage']};"
                f"{user_appliance['monthly_days']}\n"
            )

    except Exception as error:

        print(
            f"[ERRO] Falha ao salvar aparelho: "
            f"{error}"
        )


def update_user_appliance_repository(update_user_appliance):

    user_appliances = get_all_user_appliances()

    for index, user_appliance in enumerate(user_appliances):

        if (
            user_appliance["user_id"] == update_user_appliance["user_id"]
            and
            user_appliance["appliance_id"]
            == update_user_appliance["appliance_id"]
        ):
            user_appliances[index] = update_user_appliance

            save_all_user_appliances(user_appliances)

            return True

    return False


def delete_user_appliance_repository(
        user_id,
        appliance_id
):
    user_appliances = get_all_user_appliances()

    filtered_user_appliances = []

    removed = False

    for user_appliance in user_appliances:

        if not (
            user_appliance["user_id"] == user_id
            and
            user_appliance["appliance_id"] == appliance_id
        ):
            filtered_user_appliances.append(user_appliance)

        else:

            removed = True

    save_all_user_appliances(filtered_user_appliances)

    return removed


def delete_user_appliances_by_user_id(user_id):

    user_appliances = get_all_user_appliances()

    filtered_user_appliances = []

    for user_appliance in user_appliances:

        if user_appliance["user_id"] != user_id:

            filtered_user_appliances.append(
                user_appliance
            )

    save_all_user_appliances(
        filtered_user_appliances
    )

    return True
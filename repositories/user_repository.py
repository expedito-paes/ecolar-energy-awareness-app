from utils.txt_handler import read_txt_file

def get_all_users():

    users = []

    data_list = read_txt_file(
        "./data/users.txt",
        5
    )

    for line_number, data in enumerate(data_list, start=1):

        try:

            user = {

                "id": data[0],
                "name": data[1],
                "email": data[2],
                "birthday": data[3],
                "profile": data[4]
            }

            users.append(user)

        except Exception:

            print(
                f"[AVISO] Linha {line_number} "
                f"ignorada em users.txt"
            )

    return users

def get_next_user_id():

    users = get_all_users()

    return str(len(users) + 1).zfill(3)

def create_user_repository(user):

    try:
        with open(
            "./data/users.txt",
            "a",
            encoding="utf-8"
        ) as file:
            
            file.write(
                f"{user['id']};"
                f"{user['name']};"
                f"{user['email']};"
                f"{user['birthday']};"
                f"{user['profile']}\n"
            )
    
    except Exception as error:
        print(
            f"[ERRO] Falha ao salvar usuário: "
            f"{error}"
        )

def get_user_by_email(email):

    users = get_all_users()

    for user in users:
        if user["email"] == email:
            return user
        
    return None
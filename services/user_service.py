# user_service.py

from repositories.user_repository import (
    get_next_user_id,
    create_user_repository,
    get_user_by_email
)

from utils.validators import (
    validate_name,
    validate_email,
    validate_id,
    validate_not_empty,
    validate_date
)


def create_user_service(name, email, birthday, profile):

    if not validate_name(name):
        return None, "Nome inválido."

    if not validate_not_empty(email):
        return None, "E-mail obrigatório."

    if not validate_email(email):
        return None, "E-mail inválido."

    if not validate_id(profile):
        return None, "Perfil inválido."

    if not validate_not_empty(birthday):
        return None, "Data de aniversário obrigatória."

    if not validate_date(birthday):
        return None, "Data inválida. Use o formato: DD/MM/AAAA"

    existing_user = get_user_by_email(email)

    if existing_user:
        return None, "E-mail já cadastrado"

    new_id = get_next_user_id()

    user = {
        "id": new_id,
        "name": name,
        "email": email,
        "birthday": birthday,
        "profile": profile
    }

    create_user_repository(user)

    return user, None


def login_user_service(email):

    if not validate_not_empty(email):
        return None, "E-mail obrigatório."

    if not validate_email(email):
        return None, "E-mail inválido."

    user = get_user_by_email(email)

    if not user:
        return None, "Usuário não encontrado."

    return user, None
#Validação, criação de regras e organização de lógica em /service

#importação de dados
from repositories.user_repository import (
    get_next_user_id,
    create_user_repository
)

from utils.validators import (
    validate_name,
    validate_email
)

#criação do perfil de usuário
def create_user_service(name, email, birthday, profile):
   
   #validação de dados e tratamento de exceções
    if not validate_name(name):
        return None, "Nome inválido."
    if not validate_email(email):
        return None, "E-mail inválido."

    #geração de nova ID
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

from repositories.user_repository import (
    get_user_by_email
)

def login_user_service(email):
    
    user = get_user_by_email(email)

    if not user:
        return None, "Usuário não encontrado."
    
    return user, None
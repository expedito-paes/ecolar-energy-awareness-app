# appliance_service.py
# Service responsável pelos aparelhos do sistema

# Importa repositories
from repositories.appliance_repository import (
    get_all_appliances
)

from repositories.user_appliance_repository import (
    get_user_appliances_by_user_id
)

# Retorna todos os aparelhos disponíveis
def get_all_appliances_service():

    return get_all_appliances()

# Retorna aparelhos vinculados ao usuário
def get_user_appliances_by_user_service(user_id):

    return get_user_appliances_by_user_id(user_id)
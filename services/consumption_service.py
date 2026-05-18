# consumption_service.py
# Service responsável pelos níveis de consumo

from repositories.consumption_repository import (
    get_all_consumption_levels
)

# Retorna níveis de consumo
def get_consumption_levels_service():

    return get_all_consumption_levels()
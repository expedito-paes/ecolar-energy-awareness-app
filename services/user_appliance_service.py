# user_appliance_service.py

# from = usado para importar partes específicas de outro arquivo
# import = traz funções/classes/módulos para este arquivo

# Importa função responsável por salvar aparelhos do usuário
# repositories = camada responsável por acessar arquivos TXT/dados
from repositories.user_appliance_repository import (

    # Função que salva aparelho associado ao usuário
    create_user_appliance_repository
)

# Importa as funções de validação
from utils.validators import (
    # Valida números positivos
    validate_positive_number,
    # Valida IDs
    validate_id
)

# def = usado para criar funções

# create_user_appliance_service = função responsável por organizar
# dados antes de enviar ao repository

def create_user_appliance_service(

        # ID do usuário
        user_id,

        # ID do aparelho
        appliance_id,

        # Tempo médio diário de uso
        daily_usage,

        # Quantidade de dias no mês
        monthly_days
):

    # Verifica se ID do aparelho é válido
    if not validate_id(appliance_id):
        # retorna mensagem de erro
        return "ID inválido."
    # Verifica se tempo diário é positivo
    if not validate_positive_number(daily_usage):
        # retorna erro
        return "Uso diário inválido."
    # Verifica se dias mensais são positivos
    if not validate_positive_number(monthly_days):
        # retorna erro
        return "Dias inválidos."
        
    # Cria dicionário com dados do aparelho do usuário
    # dict = estrutura chave:valor
    user_appliance = {

        # ID do usuário
        "user_id": user_id,

        # ID do aparelho
        "appliance_id": appliance_id,

        # Tempo diário de uso
        "daily_usage": daily_usage,

        # Dias utilizados no mês
        "monthly_days": monthly_days
    }


    # Chama repository responsável por salvar no TXT
    create_user_appliance_repository(user_appliance)
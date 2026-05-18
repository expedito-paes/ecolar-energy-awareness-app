# user_service.py

# Services = camada responsável pela lógica do sistema
# Aqui ficam:
# - validações
# - regras de negócio
# - organização dos dados
# from = usado para importar partes específicas de outro arquivo
# import = traz funções/classes/módulos para este arquivo

# Importação de funções do repository de usuários
# repositories = camada responsável por acessar arquivos TXT/dados
from repositories.user_repository import (

    # Função responsável por gerar próximo ID
    get_next_user_id,

    # Função responsável por salvar usuário no TXT
    create_user_repository,

    # Função responsável por buscar usuário pelo e-mail
    get_user_by_email
)


# Importação das funções de validação
# utils = pasta de utilidades auxiliares
from utils.validators import (

    # Valida nome
    validate_name,

    # Valida formato do e-mail
    validate_email,

    # Valida IDs
    validate_id,

    # Verifica se campo está vazio
    validate_not_empty
)



# def = usado para criar funções

# create_user_service = função responsável pela lógica
# de criação do usuário

def create_user_service(

    # Nome digitado pelo usuário
    name,

    # E-mail digitado
    email,

    # Data de aniversário
    birthday,

    # Perfil de consumo
    profile
):


    # if = estrutura condicional
    # not = inverte resultado lógico
    # Verifica se nome é inválido
    if not validate_name(name):

        # return = devolve valor da função
        # None = ausência de valor
        return None, "Nome inválido."

    # Verifica se e-mail está vazio
    if not validate_not_empty(email):

        return None, "E-mail obrigatório."

    # Verifica se e-mail possui formato válido
    if not validate_email(email):

        return None, "E-mail inválido."

    # Verifica se ID do perfil é válido
    if not validate_id(profile):

        return None, "Perfil inválido."

    # Verifica se e-mail já está cadastrado
    existing_user = get_user_by_email(email)

    if existing_user:
        return None, "E-mail já cadastrado"

    # Geração automática do novo ID
    new_id = get_next_user_id()


    # Cria dicionário representando usuário
    # dict = estrutura chave:valor
    user = {

        # ID gerado automaticamente
        "id": new_id,

        # Nome
        "name": name,

        # E-mail
        "email": email,

        # Data de aniversário
        "birthday": birthday,

        # Perfil de consumo
        "profile": profile
    }


    # Envia usuário para repository salvar no TXT
    create_user_repository(user)


    # Retorna usuário criado
    # None indica ausência de erro
    return user, None



# Serviço responsável pelo login do usuário
def login_user_service(email):

   # Verifica se e-mail está vazio
    if not validate_not_empty(email):

        return None, "E-mail obrigatório."
    
    # Verifica validade do formato de e-mail
    if not validate_email(email):
    
        return None, "E-mail inválido."
    
    # Busca usuário pelo e-mail
    user = get_user_by_email(email)


    # Verifica se usuário NÃO foi encontrado
    if not user:

        return None, "Usuário não encontrado."

    # Retorna usuário encontrado
    return user, None
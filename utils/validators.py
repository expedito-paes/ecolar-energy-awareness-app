# validators.py
# Arquivo responsável por centralizar validações do sistema

# centralizado = todas as validações ficam em um único lugar
# reutilizável = mesmas funções podem ser usadas em vários arquivos

# def = usado para criar funções

# validate_name = função responsável por validar nomes
def validate_name(name):

    # return = devolve resultado da função

    # strip() = remove espaços vazios do começo/fim

    # != = diferente de

    # "" = texto vazio

    # Verifica se nome NÃO está vazio
    return name.strip() != ""


# Função responsável por validar e-mails
def validate_email(email):

    # in = verifica se algo existe dentro do texto

    # Verifica se e-mail possui:
    # @ e .
    return "@" in email and "." in email


# Função responsável por validar valores vazios
def validate_not_empty(value):

    # Verifica se valor NÃO está vazio
    return value.strip() != ""


# Função responsável por validar valores numéricos
def validate_numeric(value):

    # isdigit() = verifica se texto contém apenas números

    # Exemplo válido:
    # "123"

    # Exemplo inválido:
    # "abc"
    # "12a"
    return value.isdigit()


# Função responsável por validar números positivos
def validate_positive_number(value):

    # value.isdigit()
    # verifica se possui apenas números

    # int() = converte texto para número inteiro

    # > 0 = verifica se valor é positivo

    # Exemplo válido:
    # "10"

    # Exemplo inválido:
    # "-5"
    # "abc"
    # "0"
    return value.isdigit() and int(value) > 0


# Função responsável por validar IDs
def validate_id(id):

    # return = devolve True ou False

    return (

        # strip() remove espaços

        # Verifica se NÃO está vazio
        id.strip() != ""

        # and = todas condições precisam ser verdadeiras

        # Verifica se contém apenas números
        and id.isdigit()

        # Verifica se ID NÃO é "000"
        and id != "000"
    )

# Função responsável por validar se ID existe na lista de IDs válidos
def validate_existing_id(
        # ID digitado
        id,
        # Lista de IDs existentes
        valid_ids
    ):
    # in = verifica se valor existe na lista
    # returna True se ID existir
    return id in valid_ids

# Função responsável por validar opções do menu
def validate_menu_option(

    # option = valor digitado pelo usuário
    option,

    # valid_options = lista de opções permitidas
    valid_options
):

    # in = verifica se item existe dentro da lista

    # Retorna True se opção existir
    return option in valid_options

# Valida datas simples no formato DD/MM/AAAA
def validate_date(date):

    # Divide a data utilizando "/"
    parts = date.split("/")

    # Verifica se existem 3 partes
    if len(parts) != 3:
        return False
    
    # Verifica se todos os camps possuem apenas números
    return (
        parts[0].isdigit()
        and parts[1].isdigit()
        and parts[2].isdigit()
    )

# Valida números decimais positivos
def validate_float(value):

    # try = tenta converter valor para float
    try:
        # Verifica se valor é maior que zero
        return float(value) > 0
    
    # Caso valor seja inválido
    except ValueError:
        return False
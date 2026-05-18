# appliance_view.py

# def = usado para criar funções

# show_appliance = função responsável por exibir
# aparelhos disponíveis no terminal

def show_appliance(appliances):

    # print() = exibe texto no terminal

    # \n = quebra de linha
    print("\n===== APARELHOS DISPONÍVEIS =====\n")

    # for = estrutura de repetição
    # percorre todos os aparelhos da lista

    # appliance = representa cada aparelho individualmente
    for appliance in appliances:

        # Exibe informações do aparelho
        print(

            # f"" = f-string
            # permite inserir variáveis dentro do texto

            # appliance['id']
            # acessa ID do aparelho no dicionário
            f"{appliance['id']} - "

            # appliance['name']
            # acessa nome do aparelho
            f"{appliance['name']}"
        )

# Função responsável por solicitar ID do aparelho
def get_appliance_id():
    # input() = captura texto digitado
    return input(
        #\n = quebra de linha
        "\nDigite o ID do aparelho (ou 0 para finalizar): "
    )

# Função responsável por solicitar tempo diário de uso do aparelho
def get_daily_usage():
    # Captura tempo em minutos
    return input(
        "Tempo médio diário de uso (minutos): "
    )

# Função responsável por solicitar quantidade de dias de uso mensal
def get_monthly_days():
    #captura quantidade de dias
    return input(
        "Quantos dias por mês utiliza: "
    )

# consumption_view.py

# def = usado para criar funções

# show_consumption_levels = função responsável por exibir
# os níveis/perfis de consumo disponíveis

def show_consumption_levels(levels):

    # print() = exibe texto no terminal

    # \n = quebra de linha
    print("\n===== PERFIS DISPONÍVEIS =====\n")

    # for = estrutura de repetição
    # percorre todos os níveis de consumo da lista

    # level = representa cada perfil individualmente
    for level in levels:

        # Exibe informações do perfil de consumo
        print(

            # f"" = f-string
            # permite inserir variáveis dentro do texto

            # level['id']
            # acessa ID do perfil
            f"{level['id']} - "

            # level['level']
            # acessa nome do nível de consumo
            f"{level['level']} "

            # level['profile']
            # acessa descrição resumida do perfil

            # () = usado apenas para organização visual do texto
            f"({level['profile']})"
        )
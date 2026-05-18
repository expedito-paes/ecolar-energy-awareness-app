# from = usado para importar partes especificas de outra arquivo
# import = traz funções/classes/módulos para este arquivos
# importa função responsável por ler arquivo txt
# utils = pasta de utilidades auxiliares do sistemas
from utils.txt_handler import read_txt_file

# def = usado para criar funções
# get_all_user_appliances = função responsável por buscar todos os vínculos 
# entre usuários e aparelhos
def get_all_user_appliances():
    # lista vazia onde os vínculos serão armazenados
    user_appliances = []

    # chama função responsável por ler o arquivo txt
    # "./data/user_appliances.txt" = caminho do arquivo
    # 4 = quantidade esperada de colunas por linha
    data_list = read_txt_file(
        "./data/user_appliances.txt", 
        4
    )

    # for = estrutura de repetição
    # percorre todos os dados do arquivo
    # enumerate() = adiciona contador ao loop
    # line_number = número da linha
    # data = conteúdo da linha
    # start=1 = contador começa em 1
    for line_number, data in enumerate(data_list, start=1):

        # try = tenta executar bloco
        # usado para evitar quebra do sistema
        try:

            # verifica se IDs possuem apenas números
            # isdigit() = verifica se texto possui apenas caracteres numéricos
            if not data[0].isdigit():
                continue
            if not data[1].isdigit():
                continue

            # int() = converte valor para numero inteiro
            daily_usage = int(data[2])

            # int() = converte valor para numero inteiro
            monthly_days = int(data[3])

            # verifica se os valores são positivos
            if (
               daily_usage < 0
               or monthly_days < 0
            ):
               continue

            # cria dicionário representando vínculo
            # dict = estrutura chave:valor
            user_appliance = {
                # ID do usuário
                "user_id": data[0],
                # ID do aparelho
                "appliance_id": data[1],
                # Tempo médio diário de uso
                "daily_usage": daily_usage,
                # Quantidade de dias utilizados no mês
                "monthly_days": monthly_days,
            }
            
            # append() = adiciona item na lista
            user_appliances.append(user_appliance)

        # except = executa caso aconteça erro 
        # ValueError = erro de conversão numérica
        except ValueError:

            # print() = exibe aviso no terminal
            print (
                #mostra linha problemática
                f"[AVISO] Linha {line_number} " 
                # Complementa mensagem
                f"ignorada em user_appliances.txt"
            )

    # retorn = devolve valor da função
    # retorna lista completa de vínculos válidos 
    return user_appliances                   

# Função responsável por buscar os aparelhos cadastrados de um usuário
def get_user_appliances_by_user_id(user_id):

    # Lista que armazenará os vínculos encontrados entre usuário e aparelhos
    filtered_user_aplliances = []

    # Busca todos os vínculos cadastrados
    user_appliances = get_all_user_appliances()

    # for = percorre lista de vínculos
    for user_appliance in user_appliances:

        # Verifica se a ID do usuário é igual ao informado
        if user_appliance["user_id"] == user_id:

            # append() = adiciona vínculo na lista
            filtered_user_aplliances.append(user_appliance)
    
    # return = devolve lista filtrada
    return filtered_user_aplliances

# Função responsável por buscar usuários vinculados a um aparelho
def get_user_appliances_by_appliance_id(appliance_id):

    # Lista que armazenará vínculos encontrados
    filtered_user_appliances = []

    # Busca todos os vínculos cadastrados
    user_appliances = get_all_user_appliances()

    # for = percorre lista de vínculos
    for user_appliance in user_appliances:

        # Verifica se o ID do aparelho é igual ao informado
        if user_appliance["appliance_id"] == appliance_id:

            # append() = adiciona vínculo na lista
            filtered_user_appliances.append(user_appliance)

    # return = devolve lista filtrada
    return filtered_user_appliances

# Função responsável por salvar lista completa de vínculos
def save_all_user_appliances(user_appliances):

    # try = tenta executar o bloco da função
    try:

        # with open() = abre arquivo TXT
        # "w" = modo write
        # sobrescreve conteúdo existente
        # encoding="utf-8" = suporta caracteres especiais
        with open(
            "./data/user_appliances.txt",
            "w",
            encoding="utf-8"
        ) as file:
            
            # for = percorre lista de vínculos
            for user_appliance in user_appliances:

                # write() = escreve conteúdo no arquivo
                file.write(
                    # ID do usuário
                    f"{user_appliance['user_id']};"
                    # ID do aparelho
                    f"{user_appliance['appliance_id']};"
                    # Tempo médio de uso diário
                    f"{user_appliance['daily_usage']};"
                    # Quantidade de dias mensais
                    # \n = quebra de linha
                    f"{user_appliance['monthly_days']}\n"
                )

    # except = executa caso aconteça erro
    except Exception as error:

        # print() = exibe mensagem de erro
        print(
            # Mostra mensagem principal
            f"[ERRO] Falha ao salvar vínculo: "
            # Mostra detalhe do erro
            f"{error}"
        )

# def = usado para criar funções
# create_user_appliance_repository = função responsável por salvar
# aparelhos associados ao usuário

def create_user_appliance_repository(user_appliance):


    # try = tenta executar bloco
    # usado para evitar quebra do sistema em caso de erro
    try:

        # Lista contendo campos obrigatórios
        required_keys = [
            # ID do usuário
            "user_id",
            # ID do aparelho
            "appliance_id",
            # Tempo médio diário de uso
            "daily_usage",
            # Quantidade de dias mensais
            "monthly_days"
        ]

        # for = percorre lista de campos obrigatórios
        for key in required_keys:

            # Verifica se campo não existe no dicionário
            if key not in user_appliance:
                
                # print() = exibe mensagem de erro
                print(
                    # Mostra campo ausente
                    f"[ERRO] Campo obrigatório ausente: {key}"
                )

                # return = encerra função
                return

        # with open() = abre arquivo TXT
        # with = gerencia abertura/fechamento automático do arquivo
        # open() = função que abre arquivos
        # "./data/user_appliances.txt" = caminho do arquivo
        # "a" = modo append
        # adiciona conteúdo sem apagar o existente
        # encoding="utf-8" = permite caracteres especiais
        with open(
            "./data/user_appliances.txt",
            "a",
            encoding="utf-8"
        ) as file:

            # write() = escreve conteúdo no arquivo TXT
            file.write(
                # f"" = f-string
                # permite inserir variáveis dentro do texto
                # user_appliance['user_id']
                # ID do usuário
                f"{user_appliance['user_id']};"
                # ID do aparelho
                f"{user_appliance['appliance_id']};"
                # Tempo médio diário de uso
                f"{user_appliance['daily_usage']};"
                # Quantidade de dias no mês
                # \n = quebra de linha
                # faz próximo registro ir para linha seguinte
                f"{user_appliance['monthly_days']}\n"
            )

    # except = executa caso aconteça erro
    # Exception = captura qualquer tipo de erro
    except Exception as error:

        # print() = exibe mensagem no terminal
        print(
            # f"" = texto com variável
            f"[ERRO] Falha ao salvar aparelho: "
            # Mostra detalhe do erro ocorrido
            f"{error}"
        )

# Função responsável por atualizar vínculo existente
def update_user_appliance_repository(update_user_appliance):

    # Busca todos os vínculos cadastrados
    user_appliances = get_all_user_appliances()

    # enumerate() = adiciona contador ao loop
    for index, user_appliance in enumerate(user_appliances):

        # Verifica se usuário e aparelho correspondem
        if (
            user_appliance["user_id"] == update_user_appliance["user_id"]
            and
            user_appliance["appliance_id"]
            == update_user_appliance["appliance_id"]
        ):
            # Atualiza vínculo na lista
            user_appliances[index] = update_user_appliance

            # Salva lista atualizada
            save_all_user_appliances(user_appliances)

            # return True = atualização realizada
            return True
    
    # return False = vínculo não encontrado
    return False

# Função responsável por remover vínculo do sistema
def delete_user_appliance_repository(
        user_id,
        appliance_id
):
    # Busca todos os vínculos cadastrados
    user_appliances = get_all_user_appliances()

    # Lista que armezenará vínculos restantes
    filtered_user_appliances = []

    # Variável de controle
    removed = False

    # for = percorre lista de vínculos
    for user_appliance in user_appliances:

        # Verifica se o vínculo atual não é o removido
        if not (
            user_appliance["user_id"] == user_id
            and
            user_appliance["appliance_id"] == appliance_id
        ):
            # append() = adiciona vínculo na nova lista
            filtered_user_appliances.append(user_appliance)

        else:

            # Marca remoção como realizada
            removed = True

    # Salva nova lista sem vínculo removido
    save_all_user_appliances(filtered_user_appliances)

    # return = devolve resultado da remoção
    return removed
# appliance_repository.py

# from = usado para importar partes específicas de outro arquivo
# import = traz funções/classes/módulos para este arquivo
# Importa função responsável por ler arquivos TXT
# utils = pasta de utilidades auxiliares do sistema
from utils.txt_handler import read_txt_file

# def = usado para criar funções
# get_all_appliances = função responsável por buscar todos os aparelhos
def get_all_appliances():
    # Lista vazia onde os aparelhos serão armazenados
    appliances = []
    # Chama função que lê o arquivo TXT
    # "./data/appliances.txt" = caminho do arquivo
    # 8 = quantidade esperada de colunas por linha
    data_list = read_txt_file(
        "./data/appliances.txt",
        8
    )

    # for = estrutura de repetição
    # percorre todos os itens da lista
    # enumerate() = adiciona contador durante repetição
    # line_number = número da linha
    # data = conteúdo da linha
    # start=1 = contador começa em 1
    for line_number, data in enumerate(data_list, start=1):

        # try = tenta executar bloco
        # usado para evitar quebra do sistema
        try:

            # Verifica se ID contém apenas números
            # isdigit() = verifica se texto possui
            # apenas caracteres numéricos
            if not data[0].isdigit():
                # continue = ignora linha inválida
                continue

            # Verifica se nome NÃO está vazio
            # strip() remove espaços vazios
            if data[2].strip() == "":
                # ignora linha inválida
                continue

            # float() = converte valor para número decimal
            power = float(data[3])

            # int() = converte valor para número inteiro
            usage_time = int(data[4])

            # int() = converte valor para número inteiro
            days = int(data[5])

            # float() = converte valor para número decimal
            consumption = float(data[6])

            # Verifica se valores numéricos são positivos
            if (
                power < 0
                or usage_time < 0
                or days < 0
                or consumption < 0
            ):

                # ignora linha inválida
                continue

            # Cria dicionário representando aparelho
            # dict = estrutura chave:valor
            appliance = {
                # data[0] = primeira coluna do TXT
                "id": data[0],   
                # Categoria do aparelho      
                "category": data[1],  
                # Nome do aparelho    
                "name": data[2],  
                # float() = converte valor para número decimal
                # Potência elétrica do aparelho      
                "power": power,
                # int() = converte valor para número inteiro
                # Tempo médio de uso
                "usage_time": usage_time,
                # Quantidade de dias de uso
                "days": days,
                # Consumo energético
                "consumption": consumption,
                # Nível de consumo
                "level": data[7]
            }
            # append() = adiciona item na lista
            appliances.append(appliance)

        # except = executa caso erro aconteça
        # ValueError = erro de conversão numérica
        except ValueError:

            # f"" = f-string
            # permite inserir variáveis dentro do texto
            print(
                # Exibe aviso no terminal
                f"[AVISO] Linha {line_number} "
                # Mensagem complementar
                f"ignorada em appliances.txt"
            )
        
    # return = devolve valor da função
    # retorna lista completa de aparelhos
    return appliances

# Função responsável por buscar aparelho pelo ID
def get_appliance_by_id(appliance_id):

    # Busca todos os aparelhos cadastrados
    appliances = get_all_appliances()

    # for = percorre lista de aparelhos
    for appliance in appliances:

        # Verifica se ID encontrado é igual ao ID informado
        if appliance["id"] == appliance_id:

            # return = devolve aparelho encontrado
            return appliance

    # Caso aparelho não seja encontrado
    # None = ausência de valor
    return None

# Função responsável por buscar aparelhos por categoria
def get_appliances_by_category(category):

    # Lista que armazenará aparelhos encontrados
    filtered_appliances = []

    # Busca todos os aparelhos cadastrados
    appliances = get_all_appliances()

    # for = percorre lista de aparelhos
    for appliance in appliances:

        # Verifica se categoria encontrada é igual à informada
        if appliance["category"] == category:

            # append() = adiciona aparelho na lista
            filtered_appliances.append(appliance)

    # return = devolve lista de aparelhos filtrados
    return filtered_appliances

# Função responsável por salvar lista completa de aparelhos
def save_all_appliances(appliances):

    # try = tenta executar bloco
    try:

        # with open() = abre arquivo TXT
        # "w" = modo write
        # sobrescreve conteúdo existente
        # encoding="utf-8" = suporta caracteres especiais
        with open(
            "./data/appliances.txt",
            "w",
            encoding="utf-8"
        ) as file:

            # for = percorre lista de aparelhos
            for appliance in appliances:

                # write() = escreve conteúdo no arquivo
                file.write(
                    # ID do aparelho
                    f"{appliance['id']};"
                    # Categoria
                    f"{appliance['category']};"
                    # Nome
                    f"{appliance['name']};"
                    # Potência
                    f"{appliance['power']};"
                    # Tempo médio de uso
                    f"{appliance['usage_time']};"
                    # Dias de uso
                    f"{appliance['days']};"
                    # Consumo energético
                    f"{appliance['consumption']};"
                    # Nível de consumo
                    # \n = quebra de linha
                    f"{appliance['level']}\n"
                )

    # except = executa caso erro aconteça
    except Exception as error:

        # print() = exibe mensagem de erro
        print(
            # Mostra mensagem principal
            f"[ERRO] Falha ao salvar aparelhos: "
            # Mostra detalhe do erro
            f"{error}"
        )

# Função responsável por salvar aparelho no TXT
def create_appliance_repository(appliance):

    # try = tenta executar bloco
    try:

        # with open() = abre arquivo TXT
        # "a" = modo append
        # adiciona conteúdo sem apagar existente
        # encoding="utf-8" = suporta caracteres especiais
        with open(
            "./data/appliances.txt",
            "a",
            encoding="utf-8"
        ) as file:

            # write() = escreve conteúdo no arquivo
            file.write(
                # ID do aparelho
                f"{appliance['id']};"
                # Categoria
                f"{appliance['category']};"
                # Nome
                f"{appliance['name']};"
                # Potência
                f"{appliance['power']};"
                # Tempo médio de uso
                f"{appliance['usage_time']};"
                # Dias de uso
                f"{appliance['days']};"
                # Consumo energético
                f"{appliance['consumption']};"
                # Nível de consumo
                # \n = quebra de linha
                f"{appliance['level']}\n"
            )

    # except = executa caso erro aconteça
    except Exception as error:

        # print() = exibe mensagem de erro
        print(
            # Mostra mensagem principal
            f"[ERRO] Falha ao salvar aparelho: "
            # Mostra detalhe do erro
            f"{error}"
        )

# Função responsável por atualizar aparelho existente
def update_appliance_repository(updated_appliance):

    # Busca todos os aparelhos cadastrados
    appliances = get_all_appliances()

    # enumerate() = adiciona contador ao loop
    for index, appliance in enumerate(appliances):

        # Verifica se ID encontrado é igual ao ID atualizado
        if appliance["id"] == updated_appliance["id"]:

            # Atualiza aparelho na lista
            appliances[index] = updated_appliance

            # Salva lista atualizada
            save_all_appliances(appliances)

            # return True = atualização realizada
            return True

    # return False = aparelho não encontrado
    return False

# Função responsável por remover aparelho do sistema
def delete_appliance_repository(appliance_id):

    # Busca todos os aparelhos cadastrados
    appliances = get_all_appliances()

    # Lista que armazenará aparelhos restantes
    filtered_appliances = []

    # Variável de controle
    removed = False

    # for = percorre lista de aparelhos
    for appliance in appliances:

        # Verifica se ID atual é diferente do removido
        if appliance["id"] != appliance_id:

            # append() = adiciona aparelho na nova lista
            filtered_appliances.append(appliance)

        else:

            # Marca remoção como realizada
            removed = True

    # Salva nova lista sem aparelho removido
    save_all_appliances(filtered_appliances)

    # return = devolve resultado da remoção
    return removed
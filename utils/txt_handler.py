# txt_handler.py

# Funções reutilizáveis para leitura de arquivos TXT
# Todos os repositories utilizam este arquivo

# def = usado para criar funções
# read_txt_file = função responsável por ler arquivos TXT
def read_txt_file(

    # path = caminho do arquivo TXT
    path,

    # expected_fields = quantidade esperada de colunas
    expected_fields
):


    # Lista vazia onde os dados serão armazenados
    data_list = []


    # try = tenta executar bloco
    # usado para evitar quebra do sistema
    try:

        # with open() = abre arquivo TXT
        # with = gerencia fechamento automático do arquivo
        # open() = função usada para abrir arquivos
        # path = caminho recebido como parâmetro
        # "r" = modo leitura (read)
        # encoding="utf-8" = suporta caracteres especiais
        with open(path, "r", encoding="utf-8") as file:

            # for = estrutura de repetição
            # percorre linhas do arquivo
            # enumerate() = adiciona contador ao loop
            # line_number = número da linha
            # line = conteúdo da linha
            # start=1 = contador começa em 1
            for line_number, line in enumerate(file, start=1):

                # strip() = remove espaços vazios
                # remove também quebra de linha invisível
                line = line.strip()

                # if = estrutura condicional
                # Verifica se linha está vazia
                if not line:

                    # continue = reinicia loop atual
                    # ignora linha vazia
                    continue

                # split() = divide texto em partes
                # ";" = separador dos dados no TXT
                data = line.split(";")

                # len() = retorna quantidade de itens da lista
                # Verifica se quantidade de colunas está correta
                if len(data) != expected_fields:

                    # print() = exibe mensagem no terminal
                    # f"" = f-string
                    # permite inserir variáveis dentro do texto
                    print(
                        # Mostra aviso da linha inválida
                        f"[AVISO] Linha {line_number} ignorada "
                        # Mostra nome do arquivo
                        f"em {path}: quantidade inválida."
                    )

                    # Ignora linha inválida
                    continue

                # append() = adiciona item na lista
                data_list.append(data)

    # except = executa caso erro aconteça
    # FileNotFoundError = erro quando arquivo não existe
    except FileNotFoundError:
        # Mostra erro no terminal
        print(f"[ERRO] Arquivo não encontrado: {path}")

    # Captura qualquer outro erro
    except Exception as error:

        # Mostra erro no terminal
        print(
            # Mostra mensagem de erro
            f"[ERRO] Falha ao ler arquivo {path}: "
            # Mostra detalhe do erro
            f"{error}"
        )

    # return = devolve valor da função
    # Retorna lista contendo dados do TXT
    return data_list
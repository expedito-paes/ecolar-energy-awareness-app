# txt_handler.py

def read_txt_file(
    path,
    expected_fields
):

    data_list = []

    try:

        with open(path, "r", encoding="utf-8") as file:

            for line_number, line in enumerate(file, start=1):

                line = line.strip()

                if not line:

                    continue

                data = line.split(";")

                data = [field.strip() for field in data]

                if len(data) != expected_fields:

                    print(
                        f"[AVISO] Linha {line_number} ignorada "
                        f"em {path}: quantidade inválida."
                    )

                    continue

                data_list.append(data)

    except FileNotFoundError:
        print(f"[ERRO] Arquivo não encontrado: {path}")

    except Exception as error:

        print(
            f"[ERRO] Falha ao ler arquivo {path}: "
            f"{error}"
        )

    return data_list
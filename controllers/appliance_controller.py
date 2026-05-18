# appliance_controller.py
# Controller responsável pelos aparelhos do sistema

# Importa repositories dos aparelhos
from repositories.appliance_repository import (
    get_all_appliances
)

# Importa repositories de vínculos usuário/aparelho
from repositories.user_appliance_repository import (

    # Busca aparelhos vinculados ao usuário
    get_user_appliances_by_user_id,

    # Busca todos os vínculos cadastrados
    get_all_user_appliances,

    # Salva lista completa atualizada
    save_all_user_appliances
)

# Exibe aparelhos cadastrados pelo usuário
def list_user_appliances_controller(user):

    print("\n===== MEUS APARELHOS =====")

    # Busca vínculos do usuário
    user_appliances = (
        get_user_appliances_by_user_id(
            user["id"]
        )
    )

    # Verifica se usuário possui aparelhos
    if not user_appliances:

        print(
            "\nNenhum aparelho cadastrado."
        )

        return

    # Busca aparelhos disponíveis
    appliances = get_all_appliances()

    # Percorre vínculos
    for user_appliance in user_appliances:

        # Procura aparelho correspondente
        for appliance in appliances:

            if (
                appliance["id"]
                ==
                user_appliance["appliance_id"]
            ):

                print(
                    f"\n{appliance['name']}"
                )

                print(
                    f"Tempo diário: "
                    f"{user_appliance['daily_usage']} min"
                )

                print(
                    f"Dias mensais: "
                    f"{user_appliance['monthly_days']}"
                )

# Função responsável por remover
# todos os aparelhos vinculados
# a um usuário específico

def delete_user_appliances_by_user_id(user_id):

    # Busca todos os vínculos cadastrados
    user_appliances = (
        get_all_user_appliances()
    )

    # Lista que armazenará apenas
    # vínculos que NÃO pertencem
    # ao usuário removido
    filtered_user_appliances = []

    # for = percorre todos os vínculos
    for user_appliance in user_appliances:

        # Verifica se vínculo atual
        # pertence a outro usuário
        if (
            user_appliance["user_id"]
            !=
            user_id
        ):

            # append() = adiciona vínculo
            # na nova lista filtrada
            filtered_user_appliances.append(
                user_appliance
            )

    # Salva lista atualizada
    # sem os vínculos removidos
    save_all_user_appliances(
        filtered_user_appliances
    )
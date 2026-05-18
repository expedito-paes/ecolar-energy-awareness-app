# report_service.py
# Service responsável pelos relatórios do sistema

# Importa repositories
from repositories.user_appliance_repository import (
    get_user_appliances_by_user_id
)

from repositories.appliance_repository import (
    get_all_appliances
)

from repositories.tip_repository import (
    get_all_tips
)

# Busca relatório de consumo do usuário
def get_consumption_report_service(user_id):

    # Busca aparelhos do usuário
    user_appliances = (
        get_user_appliances_by_user_id(user_id)
    )

    # Busca aparelhos cadastrados
    appliances = get_all_appliances()

    # Lista do relatório
    report = []

    # Variável acumuladora
    total_consumption = 0

    # Percorre vínculos
    for user_appliance in user_appliances:

        # Procura aparelho correspondente
        for appliance in appliances:

            if (
                appliance["id"]
                ==
                user_appliance["appliance_id"]
            ):

                # Soma consumo
                total_consumption += (
                    appliance["consumption"]
                )

                # Adiciona ao relatório
                report.append({
                    "name": appliance["name"],
                    "consumption": appliance["consumption"]
                })

    # Retorna dados organizados
    return {
        "appliances": report,
        "total_consumption": total_consumption
    }

# Busca recomendações energéticas
def get_recommendations_service(user_id):

    # Busca vínculos
    user_appliances = (
        get_user_appliances_by_user_id(user_id)
    )

    # Busca aparelhos
    appliances = get_all_appliances()

    # Busca dicas
    tips = get_all_tips()

    # Lista de recomendações
    recommendations = []

    # Percorre aparelhos do usuário
    for user_appliance in user_appliances:

        # Procura aparelho correspondente
        for appliance in appliances:

            if (
                appliance["id"]
                ==
                user_appliance["appliance_id"]
            ):

                # Lista de dicas do aparelho
                appliance_tips = []

                # Busca dicas
                for tip in tips:

                    if (
                        tip["appliance"]
                        ==
                        appliance["name"]
                    ):

                        appliance_tips.append(
                            tip["tip"]
                        )

                # Adiciona recomendações
                recommendations.append({
                    "name": appliance["name"],
                    "tips": appliance_tips
                })

    return recommendations

# Simulação simples de economia
def get_simulation_service():

    return {
        "message": (
            "Reduzindo 30 minutos diários "
            "de uso em aparelhos de alto consumo."
        ),
        "economy": (
            "Economia estimada: "
            "5% a 15% ao mês."
        )
    }
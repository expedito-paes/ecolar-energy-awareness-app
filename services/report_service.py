# report_service.py
# Service responsável pelos relatórios do sistema

# Importa repository responsável
# pelos aparelhos vinculados ao usuário
from repositories.user_appliance_repository import (
    get_user_appliances_by_user_id
)

# Importa repository responsável
# pelos aparelhos do sistema
from repositories.appliance_repository import (
    get_all_appliances
)

# Importa repository responsável
# pelas dicas energéticas
from repositories.tip_repository import (
    get_all_tips
)

# Função responsável por gerar
# relatório energético do usuário
def get_consumption_report_service(user_id):

    # Busca aparelhos vinculados ao usuário
    user_appliances = (
        get_user_appliances_by_user_id(user_id)
    )

    # Busca aparelhos disponíveis no sistema
    appliances = get_all_appliances()

    # Lista que armazenará
    # relatório final
    report = []

    # Variável acumuladora
    # do consumo total
    total_consumption = 0

    # for = percorre aparelhos do usuário
    for user_appliance in user_appliances:

        # for = percorre aparelhos do sistema
        for appliance in appliances:

            # Verifica se IDs correspondem
            if (
                appliance["id"]
                ==
                user_appliance["appliance_id"]
            ):

                # Calcula consumo energético REAL
                #
                # Fórmula:
                #
                # potência(W)
                # x tempo(min)
                # x dias
                #
                # /1000 -> converte W para kW
                # /60 -> converte minutos para horas
                consumption = (
                    (
                        appliance["power"]
                        *
                        user_appliance["daily_usage"]
                        *
                        user_appliance["monthly_days"]
                    )
                    / 1000
                    / 60
                )

                # Soma consumo total
                total_consumption += consumption

                # append() = adiciona aparelho
                # ao relatório final
                report.append({

                    # Nome do aparelho
                    "name": appliance["name"],

                    # round() = arredonda valor
                    # para 2 casas decimais
                    "consumption": round(
                        consumption,
                        2
                    )
                })

    # return = devolve relatório organizado
    return {

        # Lista de aparelhos
        "appliances": report,

        # Consumo total do usuário
        "total_consumption": round(
            total_consumption,
            2
        )
    }

# Função responsável por buscar
# recomendações energéticas
def get_recommendations_service(user_id):

    # Busca vínculos do usuário
    user_appliances = (
        get_user_appliances_by_user_id(
            user_id
        )
    )

    # Busca aparelhos disponíveis
    appliances = get_all_appliances()

    # Busca todas as dicas
    tips = get_all_tips()

    # Lista final de recomendações
    recommendations = []

    # Percorre aparelhos do usuário
    for user_appliance in user_appliances:

        # Percorre aparelhos do sistema
        for appliance in appliances:

            # Verifica correspondência do aparelho
            if (
                appliance["id"]
                ==
                user_appliance["appliance_id"]
            ):

                # Lista de dicas do aparelho
                appliance_tips = []

                # Percorre todas as dicas
                for tip in tips:

                    # Verifica se dica pertence
                    # ao aparelho atual
                    if (
                        tip["appliance"]
                        ==
                        appliance["name"]
                    ):

                        # Adiciona dica encontrada
                        appliance_tips.append(
                            tip["tip"]
                        )

                # Adiciona recomendações finais
                recommendations.append({

                    # Nome do aparelho
                    "name": appliance["name"],

                    # Lista de dicas
                    "tips": appliance_tips
                })

    # Retorna recomendações
    return recommendations

# Função responsável pela
# simulação energética simples
def get_simulation_service():

    # Retorna dados simulados
    return {

        # Mensagem explicativa
        "message": (
            "Reduzindo 30 minutos diários "
            "de uso em aparelhos de alto consumo."
        ),

        # Resultado estimado
        "economy": (
            "Economia estimada: "
            "5% a 15% ao mês."
        )
    }
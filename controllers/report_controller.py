# report_controller.py
# Controller responsável pelos relatórios do sistema

from services.report_service import (
    get_consumption_report_service,
    get_recommendations_service,
    get_simulation_service
)

# Exibe relatório simples de consumo
def show_consumption_report_controller(user):

    print("\n===== RELATÓRIO ENERGÉTICO =====")

    # Busca dados do relatório
    report = get_consumption_report_service(
        user["id"]
    )

    # Percorre aparelhos
    for appliance in report["appliances"]:

        print(f"\n{appliance['name']}")

        print(
            f"Consumo base: "
            f"{appliance['consumption']} kWh"
        )

    # Exibe total
    print(
        f"\nConsumo total estimado: "
        f"{report['total_consumption']} kWh"
    )

# Exibe recomendações energéticas
def show_recommendations_controller(user):

    print("\n===== RECOMENDAÇÕES =====")

    # Busca recomendações
    recommendations = (
        get_recommendations_service(
            user["id"]
        )
    )

    # Percorre recomendações
    for recommendation in recommendations:

        print(f"\n{recommendation['name']}")

        for tip in recommendation["tips"]:

            print(f"- {tip}")

# Simulação simples de economia
def show_simulation_controller(user):

    print("\n===== SIMULAÇÃO DE ECONOMIA =====")

    # Busca dados da simulação
    simulation = get_simulation_service()

    print(f"\n{simulation['message']}")

    print(f"\n{simulation['economy']}")
# report_controller.py

from services.report_service import (
    get_consumption_report_service,
    get_recommendations_service,
    get_simulation_service
)

def show_consumption_report_controller(user):

    print("\n===== RELATÓRIO ENERGÉTICO =====")

    report = get_consumption_report_service(
        user["id"]
    )

    for appliance in report["appliances"]:

        print(f"\n{appliance['name']}")

        print(
            f"Consumo base: "
            f"{appliance['consumption']} kWh"
        )

    print(
        f"\nConsumo total estimado: "
        f"{report['total_consumption']} kWh"
    )

def show_recommendations_controller(user):

    print("\n===== RECOMENDAÇÕES =====")

    recommendations = (
        get_recommendations_service(
            user["id"]
        )
    )

    for recommendation in recommendations:

        print(f"\n{recommendation['name']}")

        for tip in recommendation["tips"]:

            print(f"- {tip}")

def show_simulation_controller(user):

    print("\n===== SIMULAÇÃO DE ECONOMIA =====")

    simulation = get_simulation_service()

    print(f"\n{simulation['message']}")

    print(f"\n{simulation['economy']}")
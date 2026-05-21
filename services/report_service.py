# report_service.py

from repositories.user_appliance_repository import (
    get_user_appliances_by_user_id
)

from repositories.appliance_repository import (
    get_all_appliances
)

from repositories.tip_repository import (
    get_all_tips
)

def get_consumption_report_service(user_id):

    user_appliances = (
        get_user_appliances_by_user_id(user_id)
    )

    appliances = get_all_appliances()

    report = []

    total_consumption = 0

    for user_appliance in user_appliances:

        for appliance in appliances:

            if (
                appliance["id"]
                ==
                user_appliance["appliance_id"]
            ):

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

                total_consumption += consumption

                report.append({
                    "name": appliance["name"],
                    "consumption": round(
                        consumption,
                        2
                    )
                })

    return {
        "appliances": report,
        "total_consumption": round(
            total_consumption,
            2
        )
    }

def get_recommendations_service(user_id):

    user_appliances = (
        get_user_appliances_by_user_id(
            user_id
        )
    )

    appliances = get_all_appliances()

    tips = get_all_tips()

    recommendations = []

    for user_appliance in user_appliances:

        for appliance in appliances:

            if (
                appliance["id"]
                ==
                user_appliance["appliance_id"]
            ):

                appliance_tips = []

                for tip in tips:

                    if (
                        tip["appliance"]
                        ==
                        appliance["name"]
                    ):

                        appliance_tips.append(
                            tip["tip"]
                        )

                recommendations.append({
                    "name": appliance["name"],
                    "tips": appliance_tips
                })

    return recommendations

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
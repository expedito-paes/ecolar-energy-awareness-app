# simulation_service.py

from services.consumption_service import (
    calculate_user_consumption,
    calculate_cost
)


def simulate_savings(user_id, reduction_percentage):

    current_consumption = calculate_user_consumption(user_id)

    current_cost = calculate_cost(current_consumption)

    reduction_kwh = current_consumption * reduction_percentage / 100
    new_consumption = current_consumption - reduction_kwh

    new_cost = calculate_cost(new_consumption)

    savings_reais = current_cost - new_cost

    savings_year = savings_reais * 12

    return {
        "current_consumption_kwh": current_consumption,
        "current_cost_reais": current_cost,
        "reduction_percentage": reduction_percentage,
        "new_consumption_kwh": round(new_consumption, 2),
        "new_cost_reais": new_cost,
        "monthly_savings_reais": round(savings_reais, 2),
        "annual_savings_reais": round(savings_year, 2)
    }


def simulate_multiple_reductions(user_id):

    current_consumption = calculate_user_consumption(user_id)
    current_cost = calculate_cost(current_consumption)

    reduction_10 = current_consumption * 10 / 100
    consumption_10 = current_consumption - reduction_10
    cost_10 = calculate_cost(consumption_10)
    savings_10 = current_cost - cost_10

    reduction_20 = current_consumption * 20 / 100
    consumption_20 = current_consumption - reduction_20
    cost_20 = calculate_cost(consumption_20)
    savings_20 = current_cost - cost_20

    reduction_30 = current_consumption * 30 / 100
    consumption_30 = current_consumption - reduction_30
    cost_30 = calculate_cost(consumption_30)
    savings_30 = current_cost - cost_30

    return {
        "current_consumption": current_consumption,
        "current_cost": current_cost,
        "option_10_percent": {
            "percentage": 10,
            "new_consumption": round(consumption_10, 2),
            "new_cost": cost_10,
            "monthly_savings": round(savings_10, 2),
            "annual_savings": round(savings_10 * 12, 2)
        },
        "option_20_percent": {
            "percentage": 20,
            "new_consumption": round(consumption_20, 2),
            "new_cost": cost_20,
            "monthly_savings": round(savings_20, 2),
            "annual_savings": round(savings_20 * 12, 2)
        },
        "option_30_percent": {
            "percentage": 30,
            "new_consumption": round(consumption_30, 2),
            "new_cost": cost_30,
            "monthly_savings": round(savings_30, 2),
            "annual_savings": round(savings_30 * 12, 2)
        }
    }

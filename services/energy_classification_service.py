# energy_classification_service.py

from services.consumption_service import (
    calculate_user_consumption,
    calculate_cost
)


def classify_consumption(user_id):

    consumption = calculate_user_consumption(user_id)

    classification = ""

    if consumption <= 50:

        classification = "MUITO BAIXO"

    elif consumption <= 100:

        classification = "BAIXO"

    elif consumption <= 150:

        classification = "MEDIO"

    elif consumption <= 250:

        classification = "ALTO"

    else:

        classification = "MUITO ALTO"

    return {
        "consumption_kwh": consumption,
        "classification": classification
    }


def compare_with_average(user_id):

    user_consumption = calculate_user_consumption(user_id)

    national_average = 150

    status = ""

    if user_consumption > national_average:

        status = "ACIMA"

    elif user_consumption == national_average:

        status = "IGUAL"

    else:

        status = "ABAIXO"

    return {
        "user_consumption_kwh": user_consumption,
        "national_average_kwh": national_average,
        "status": status
    }


def classify_by_range(user_id):

    consumption = calculate_user_consumption(user_id)

    range_class = ""

    if consumption < 30:

        range_class = "FAIXA 1: Minimo (0-30 kWh)"

    elif consumption < 60:

        range_class = "FAIXA 2: Baixo (30-60 kWh)"

    elif consumption < 100:

        range_class = "FAIXA 3: Medio (60-100 kWh)"

    elif consumption < 150:

        range_class = "FAIXA 4: Alto (100-150 kWh)"

    else:

        range_class = "FAIXA 5: Muito Alto (150+ kWh)"

    return range_class

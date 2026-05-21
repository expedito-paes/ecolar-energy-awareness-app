# consumption_service.py

from repositories.user_appliance_repository import (
    get_user_appliances_by_user_id
)

from repositories.appliance_repository import (
    get_all_appliances
)

from repositories.consumption_repository import (
    get_all_consumption_levels
)


def calculate_consumption_kwh(power, daily_usage_minutes, monthly_days):

    kw = power / 1000

    daily_hours = daily_usage_minutes / 60

    monthly_hours = daily_hours * monthly_days

    consumption = kw * monthly_hours

    return round(consumption, 2)


def calculate_user_consumption(user_id):

    user_appliances = get_user_appliances_by_user_id(user_id)

    all_appliances = get_all_appliances()

    total_consumption = 0

    for user_appliance in user_appliances:

        for appliance in all_appliances:

            if appliance["id"] == user_appliance["appliance_id"]:

                consumption = calculate_consumption_kwh(
                    appliance["power"],
                    user_appliance["daily_usage"],
                    user_appliance["monthly_days"]
                )

                total_consumption = total_consumption + consumption

                break

    return total_consumption


def get_consumption_levels_service():
    return get_all_consumption_levels()


def calculate_cost(consumption_kwh):

    price = 0.95

    cost = consumption_kwh * price

    return round(cost, 2)

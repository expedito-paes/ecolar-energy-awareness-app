# validators.py

def validate_name(name):
    return name.strip() != ""


def validate_email(email):
    return "@" in email and "." in email


def validate_not_empty(value):
    return value.strip() != ""


def validate_numeric(value):
    return value.isdigit()


def validate_positive_number(value):
    return value.isdigit() and int(value) > 0


def validate_id(id):
    return (
        id.strip() != ""
        and id.isdigit()
        and id != "000"
    )

def validate_existing_id(id, valid_ids):
    return id in valid_ids

def validate_menu_option(option, valid_options):
    return option in valid_options

def validate_date(date):
    parts = date.split("/")

    if len(parts) != 3:
        return False

    return (
        parts[0].isdigit()
        and parts[1].isdigit()
        and parts[2].isdigit()
    )

def validate_float(value):
    try:
        return float(value) > 0

    except ValueError:
        return False
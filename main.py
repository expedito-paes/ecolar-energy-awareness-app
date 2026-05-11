from utils.file_handler import read_appliances

print("Sistema EcoLar iniciado\n")

appliances = read_appliances()

for appliance in appliances:

    print("----------------------------")
    print(f"ID: {appliance['id']}")
    print(f"Categoria: {appliance['category']}")
    print(f"Aparelho: {appliance['name']}")
    print(f"Potência: {appliance['power']} W")
    print(f"Tempo de uso: {appliance['usage_time']} min")
    print(f"Dias de uso: {appliance['days']}")
    print(f"Consumo: {appliance['consumption']} kWh")
    print(f"Nível: {appliance['level']}")
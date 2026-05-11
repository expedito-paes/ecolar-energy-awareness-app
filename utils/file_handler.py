def read_appliances():

    appliances = []

    print("Lendo appliances...\n")

    with open("data/appliances.txt", "r", encoding="utf-8") as file:

        for line in file:

            line = line.strip()

            parts = line.split(";")

            appliance = {
                "id": parts[0],
                "category": parts[1],
                "name": parts[2],
                "power": parts[3],
                "usage_time": parts[4],
                "days": parts[5],
                "consumption": parts[6],
                "level": parts[7]
            }

            appliances.append(appliance)

    return appliances
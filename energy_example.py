from controllers.energy_controller import (
    show_consumption,
    show_classification,
    show_savings,
    show_savings_options
)

print("\n" + "="*70)
print("EXEMPLO - SISTEMA DE CONSUMO DE ENERGIA")
print("="*70)

user_test = {
    "id": "001",
    "name": "Expedito"
}

print("\n>>> OPCAO 1: Consumo")
show_consumption(user_test)

print("\n>>> OPCAO 2: Classificacao")
show_classification(user_test)

print("\n>>> OPCAO 3: Economia")
show_savings(user_test)

print("\n>>> OPCAO 4: Opcoes de economia")
show_savings_options(user_test)

print("\n" + "="*70)
print("FIM DO EXEMPLO")
print("="*70 + "\n")

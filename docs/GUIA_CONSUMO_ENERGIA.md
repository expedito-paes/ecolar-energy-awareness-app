# GUIA SIMPLES - CONSUMO DE ENERGIA

## O QUE FOI CRIADO:

### 1. SERVICE (services/consumption_energy_service.py)
Services sao arquivos que fazem os CALCULOS do sistema.

**Funcoes criadas:**

#### calcular_consumo_aparelho()
Calcula quanto UM aparelho consome por mes.

```python
# Exemplo:
potencia = 90  # watts do aparelho
minutos_dia = 1440  # usa 24 horas por dia
dias_mes = 30  # usa todos os dias

consumo = calcular_consumo_aparelho(potencia, minutos_dia, dias_mes)
print(consumo)  # Resultado: 64.8 kWh
```

**Como funciona:**
1. Divide potencia por 1000 (converte watts para kilowatts)
2. Divide minutos por 60 (converte em horas)
3. Multiplica horas por dias
4. Multiplica resultado pela potencia em kilowatts

**Resultado:** kWh (kilowatts-hora)

---

#### calcular_consumo_total_usuario()
Calcula consumo de TODOS os aparelhos de um usuario.

```python
# Exemplo:
dados = calcular_consumo_total_usuario("001")

print(dados["consumo_total_kwh"])  # Total consumido
print(dados["quantidade_aparelhos"])  # Quantos aparelhos
print(dados["aparelhos"])  # Lista com detalhes
```

**Retorna um dicionario com:**
- id_usuario: ID do usuario
- aparelhos: Lista com nome, potencia, consumo de cada um
- consumo_total_kwh: Soma de tudo
- quantidade_aparelhos: Quantos aparelhos tem

---

#### calcular_custo_energia()
Converte kWh em REAIS.

```python
# Exemplo:
consumo = 121.5  # kWh
preco = 0.95  # R$ por kWh (padrao brasileiro)

custo = calcular_custo_energia(consumo, preco)
print(custo)  # Resultado: R$ 115.42
```

---

#### encontrar_aparelho_maior_consumo()
Descobre qual aparelho MAIS consome.

```python
# Exemplo:
maior = encontrar_aparelho_maior_consumo("001")
print(maior["nome"])  # Geladeira 1 Porta
print(maior["consumo_kwh"])  # 64.8 kWh
```

---

#### calcular_economia_potencial()
Mostra quanto economiza se reduzir uso.

```python
# Exemplo:
economia = calcular_economia_potencial("001", 30)

print(economia["consumo_atual_kwh"])  # 121.5
print(economia["economia_mensal"])  # R$ 34.62
print(economia["economia_anual"])  # R$ 415.44
```

---

### 2. CONTROLLER (controllers/energy_report_controller.py)
Controllers sao arquivos que EXIBEM as informacoes na tela.

**Funcoes criadas:**

#### relatorio_consumo_simples()
Mostra consumo total de forma simples.

```python
usuario = {"id": "001", "name": "Expedito"}
relatorio_consumo_simples(usuario)

# Exibe:
# Total de aparelhos: 4
# Consumo total: 121.5 kWh
# Custo estimado: R$ 115.42
```

---

#### relatorio_detalhes_aparelhos()
Mostra cada aparelho com seus dados.

```python
relatorio_detalhes_aparelhos(usuario)

# Exibe:
# Nome: Geladeira 1 Porta
# Categoria: Cozinha
# Potencia: 90W
# Consumo: 64.8 kWh
# Nivel: Medio
```

---

#### relatorio_maior_consumo()
Mostra qual aparelho mais consome.

```python
relatorio_maior_consumo(usuario)

# Exibe:
# Nome: Geladeira 1 Porta
# Potencia: 90W
# Consumo: 64.8 kWh
```

---

#### relatorio_economia()
Mostra simulacao de economia.

```python
relatorio_economia(usuario)

# Exibe:
# Consumo atual: 121.5 kWh (R$ 115.42)
# Se reduzir 30%:
# Novo consumo: 85.05 kWh (R$ 80.80)
# Economia por mes: R$ 34.62
# Economia por ano: R$ 415.44
```

---

## COMO USAR:

### Passo 1: Importar as funcoes
```python
from services.consumption_energy_service import (
    calcular_consumo_total_usuario,
    calcular_custo_energia
)

from controllers.energy_report_controller import (
    relatorio_consumo_simples,
    relatorio_detalhes_aparelhos
)
```

### Passo 2: Usar em uma funcao
```python
def mostrar_consumo_usuario(usuario):
    # Mostra consumo simples
    relatorio_consumo_simples(usuario)
    
    # Mostra detalhes
    relatorio_detalhes_aparelhos(usuario)
```

### Passo 3: Chamar no menu
```python
# No menu do usuario adicionar:
elif opcao == "3":
    mostrar_consumo_usuario(usuario)
```

---

## ESTRUTURA DOS DADOS:

### Usuario (vem de users.txt):
```python
usuario = {
    "id": "001",
    "name": "Expedito Paes",
    "email": "efgp@cesar.school",
    "birthday": "26/03/1984",
    "profile": "003"
}
```

### Aparelho (vem de appliances.txt):
```python
aparelho = {
    "id": "001",
    "category": "Cozinha",
    "name": "Geladeira 1 Porta",
    "power": 90,  # Watts
    "usage_time": 1440,  # minutos
    "days": 30,
    "consumption": 30,  # kWh
    "level": "Medio"
}
```

### Vínculo Usuario-Aparelho (vem de user_appliances.txt):
```python
vinculo = {
    "user_id": "001",
    "appliance_id": "001",
    "daily_usage": 1440,  # minutos por dia
    "monthly_days": 30  # dias por mes
}
```

---

## FORMULAS USADAS:

### Consumo de um aparelho:
```
kilowatts = potencia / 1000
horas_diarias = minutos_diarios / 60
total_horas_mes = horas_diarias * dias_mes
consumo_kwh = kilowatts * total_horas_mes
```

### Custo em reais:
```
custo = consumo_kwh * 0.95
```

### Economia com reducao:
```
novo_consumo = consumo_atual * (100 - percentual_reducao) / 100
economia = (consumo_atual - novo_consumo) * 0.95
```

---

## EXEMPLOS REAIS:

### Usuario 001 - Expedito Paes:
- Geladeira: 64.8 kWh
- Ventilador: 15.6 kWh
- TV: 21.6 kWh
- Notebook: 19.5 kWh
- **TOTAL: 121.5 kWh (R$ 115.42)**

### Usuario 002 - Amanda:
- Geladeira: 64.8 kWh
- Secador: 21.0 kWh
- Notebook: 3.9 kWh
- **TOTAL: 89.7 kWh (R$ 85.22)**

### Usuario 003 - Sofia:
- Geladeira: 64.8 kWh
- TV: 8.1 kWh
- **TOTAL: 72.9 kWh (R$ 69.25)**

---

## DICAS PARA INICIANTES:

1. **Leia o codigo linha por linha**
   - Cada funcao faz UMA coisa

2. **Teste as funcoes isoladas**
   - Use o Python interativo para testar

3. **Entenda os dados que entram**
   - Potencia em watts, tempo em minutos

4. **Entenda os dados que saem**
   - Consumo em kWh, custo em reais

5. **Use print() para debugar**
   - Mostra valores intermediarios

6. **Documente seu codigo**
   - Comenta o QUE faz e POR QUE faz

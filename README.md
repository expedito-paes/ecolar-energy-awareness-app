# EcoLar

Sistema acadêmico desenvolvido em Python com foco no monitoramento e conscientização sobre consumo energético residencial.

## Equipe 4

- Expedito Ferraz Gominho Paes - Gestor do Projeto, Pesquisa e Documentação

- Lucas Veiga De Aquino Souza Leite - Desenvolvedor de software

- Mario Sergio Fernandes Mendonça - Analista Técnico e Modelagem de Dados

- Raquel Moura Lins Acioli - Designer de Experiência (UX)


## Objetivo do Projeto

O EcoLar tem como objetivo auxiliar usuários no acompanhamento do consumo energético de aparelhos elétricos, promovendo maior conscientização sobre hábitos de consumo e incentivando práticas mais sustentáveis através de cálculos de consumo, estimativas de custo e classificação energética.


## Funcionalidades do Sistema

- Cadastro de usuários
- Cadastro de aparelhos elétricos
- Leitura e manipulação de arquivos TXT
- Atualização de dados
- Remoção de registros
- Cálculo de consumo energético (kWh)
- Estimativa de custo mensal
- Classificação energética (A+ até E)
- Simulação simples de economia
- Tratamento de erros e exceções


## Tecnologias Utilizadas

- Python
- Git
- GitHub
- Visual Studio Code
- Arquivos TXT para persistência de dados


## Estrutura do Projeto

```plaintext
EcoLar/
│
├── main.py
├── README.md
│
├── data/
│   ├── appliances.txt
│   ├── history.txt
│   ├── users.txt
│
├── models/
│   ├── __init__.py
│   ├── appliance.py
│   ├── user.py
│
├── services/
│   ├── __init__.py
│   ├── consumption_service.py
│   ├── crud_service.py
│
├── utils/
│   ├── __init__.py
│   ├── file_handler.py
│   ├── validators.py
# 🌱 EcoLar

> **Aplicação desenvolvida em Python para monitoramento e análise do consumo energético residencial, promovendo a conscientização sobre o uso eficiente da energia elétrica por meio de estimativas de consumo, simulações de economia e recomendações voltadas à sustentabilidade.**

---

# 📌 Visão Geral

O **EcoLar** é um projeto desenvolvido durante a disciplina **Projeto 1** do curso de **Graduação em Gestão da Tecnologia da Informação (GTI)** da **CESAR School**, tendo como tema central a **Transição Energética**.

O projeto surgiu a partir da necessidade de incentivar o consumo consciente de energia elétrica nas residências, oferecendo aos usuários uma ferramenta simples e intuitiva capaz de estimar o consumo dos aparelhos domésticos, calcular custos aproximados e fornecer recomendações que auxiliem na redução do desperdício energético.

Além do desenvolvimento da solução, o projeto proporcionou a aplicação prática de conceitos de engenharia de software, arquitetura de sistemas, gestão de projetos, colaboração em equipe e desenvolvimento orientado à resolução de problemas reais.

---

# 🎯 Objetivos do Projeto

Desenvolver uma aplicação capaz de:

* Monitorar o consumo energético de aparelhos residenciais;
* Estimar gastos financeiros relacionados ao consumo de energia elétrica;
* Gerar relatórios para acompanhamento do consumo;
* Simular cenários de economia energética;
* Incentivar hábitos sustentáveis por meio de recomendações educativas;
* Promover a conscientização sobre o uso eficiente da energia.

---

# 🏆 Principais Resultados Alcançados

Ao final do projeto foram alcançados os seguintes resultados:

* Desenvolvimento de uma aplicação funcional em Python utilizando arquitetura modular em camadas;
* Implementação de um sistema completo para gerenciamento de usuários e aparelhos elétricos;
* Automatização do cálculo de consumo energético (kWh) e estimativa de custos mensais;
* Geração de relatórios individuais de consumo;
* Implementação de simulações de economia energética;
* Disponibilização de recomendações para redução do consumo de energia;
* Organização do projeto seguindo princípios de separação de responsabilidades;
* Utilização de Git e GitHub durante todo o desenvolvimento colaborativo;
* Documentação técnica estruturada do projeto;
* Aplicação de práticas de gestão de projetos durante todas as etapas de desenvolvimento.

O projeto demonstrou a viabilidade de uma solução tecnológica voltada à educação energética, reunindo informações de consumo em uma única plataforma e incentivando mudanças de comportamento que contribuem para a sustentabilidade.

---

# ✨ Destaques

* 🔋 Monitoramento do consumo energético residencial
* 💰 Estimativa de gastos com energia elétrica
* 📊 Relatórios personalizados de consumo
* 📉 Simulação de economia energética
* 🌱 Incentivo ao consumo consciente
* 🏗️ Arquitetura modular em camadas
* 🔄 Controle de versão utilizando Git e GitHub
* 👥 Desenvolvimento colaborativo
* 🎓 Projeto acadêmico baseado em um problema real

---

# 📊 Informações do Projeto

| Item                | Descrição                                |
| ------------------- | ---------------------------------------- |
| Projeto             | EcoLar                                   |
| Tipo                | Projeto Acadêmico                        |
| Curso               | Gestão da Tecnologia da Informação (GTI) |
| Instituição         | CESAR School                             |
| Disciplina          | Projeto 1                                |
| Tema                | Transição Energética                     |
| Linguagem Principal | Python                                   |
| Arquitetura         | Modular em Camadas                       |
| Persistência        | Arquivos TXT                             |
| IDE                 | Visual Studio Code                       |
| Controle de Versão  | Git e GitHub                             |
| Status              | Concluído                                |

---

# 🚀 Principais Funcionalidades

## 👤 Gestão de Usuários

* Cadastro de usuários;
* Autenticação simplificada;
* Atualização de dados cadastrais;
* Exclusão de contas.

## 🔌 Gestão de Aparelhos

* Cadastro de aparelhos por usuário;
* Organização por categorias;
* Atualização das informações cadastradas;
* Exclusão de aparelhos.

## ⚡ Monitoramento Energético

* Cálculo automático do consumo em kWh;
* Estimativa do custo mensal;
* Classificação energética;
* Comparação de consumo;
* Identificação de padrões de utilização.

## 📈 Relatórios e Simulações

* Relatórios individuais por aparelho;
* Simulações de economia energética;
* Estimativa de redução de gastos;
* Recomendações para uso consciente;
* Dicas educativas sobre eficiência energética.

## 🛡️ Qualidade da Aplicação

* Persistência dos dados em arquivos TXT;
* Validação centralizada das entradas;
* Tratamento de exceções;
* Organização estrutural do código;
* Separação das responsabilidades entre os módulos.

---

# 🏗️ Arquitetura do Sistema

O EcoLar foi desenvolvido utilizando uma arquitetura modular em camadas, favorecendo a organização do código, manutenção, reutilização de componentes e escalabilidade.

```
Views
│
├── Controllers
│
├── Services
│
├── Repositories
│
└── Utils
```

### Views

Responsáveis pela interação com o usuário através da interface textual.

### Controllers

Coordenam o fluxo da aplicação e realizam a comunicação entre as camadas.

### Services

Implementam as regras de negócio e os cálculos relacionados ao consumo energético.

### Repositories

Gerenciam a persistência e recuperação das informações.

### Utils

Disponibilizam funções auxiliares, validações, formatações e utilidades compartilhadas.

---

# 📂 Estrutura do Projeto

```text
EcoLar/
│
├── main.py
├── README.md
├── requirements.txt
│
├── controllers/
├── services/
├── repositories/
├── views/
├── utils/
├── data/
└── docs/
```

---

# 🛠️ Tecnologias Utilizadas

* Python 3
* Git
* GitHub
* Visual Studio Code
* Arquivos TXT para persistência de dados

---

# ▶️ Como Executar o Projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/expedito-paes/ecolar-energy-awareness-app.git
```

## 2. Acessar a pasta

```bash
cd ecolar-energy-awareness-app
```

## 3. Executar a aplicação

```bash
python main.py
```

---

# 👥 Equipe

## Expedito Ferraz Gominho Paes

**Gerente do Projeto**

* Planejamento e gestão das atividades;
* Organização do cronograma;
* Definição da arquitetura da aplicação;
* Estruturação do fluxo de versionamento;
* Integração dos módulos;
* Documentação técnica e acadêmica;
* Apoio aos testes e validação da solução.

## Lucas Veiga de Aquino Souza Leite

**Desenvolvedor**

* Implementação das funcionalidades;
* Desenvolvimento das regras de negócio;
* Construção dos módulos da aplicação.

## Raquel Moura Lins Acioli

**UX e Organização da Interface**

* Estruturação da experiência do usuário;
* Organização da interface textual;
* Apoio à usabilidade da aplicação.

---

# 💡 Competências Desenvolvidas

Durante o desenvolvimento do projeto foram aplicados conhecimentos relacionados a:

* Gestão de Projetos;
* Engenharia de Software;
* Arquitetura de Sistemas;
* Programação em Python;
* Controle de Versão com Git e GitHub;
* Organização modular de aplicações;
* Trabalho colaborativo;
* Comunicação entre equipes;
* Planejamento e acompanhamento de entregas;
* Documentação técnica;
* Resolução de problemas reais por meio da tecnologia.

---

# 🔮 Evoluções Futuras

O EcoLar possui potencial para evolução por meio da implementação de novas funcionalidades, como:

* Banco de dados relacional;
* Interface gráfica;
* Aplicação Web;
* Aplicação Mobile;
* Dashboard analítico;
* Exportação de relatórios em PDF;
* Integração com APIs de tarifas energéticas;
* Cadastro automatizado de aparelhos;
* Indicadores personalizados de consumo.

---

# ✅ Status do Projeto

**Projeto concluído com sucesso** no contexto da disciplina **Projeto 1** da **CESAR School**.

O EcoLar representa a aplicação prática de conceitos de desenvolvimento de software, arquitetura de sistemas, gestão de projetos, controle de versão e trabalho colaborativo, além de demonstrar como soluções tecnológicas podem contribuir para a conscientização sobre o consumo sustentável de energia elétrica.

---

# 🎓 Instituição

**CESAR School**

Graduação em Gestão da Tecnologia da Informação (GTI)

Disciplina: Projeto 1

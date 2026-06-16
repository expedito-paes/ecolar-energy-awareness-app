# 🌱 EcoLar

> Aplicação desenvolvida em Python para monitoramento e análise do consumo energético residencial, incentivando hábitos mais sustentáveis por meio de estimativas de gasto, simulações de economia e recomendações de uso consciente da energia.

---

## 📌 Visão Geral

O **EcoLar** é um projeto acadêmico desenvolvido na disciplina **Projeto 1** do curso de **Graduação em Gestão da Tecnologia da Informação (GTI) da CESAR School**.

A proposta surgiu a partir do desafio de **Transição Energética**, buscando criar uma solução simples, acessível e educativa para ajudar usuários a compreenderem como seus hábitos influenciam o consumo de energia elétrica em suas residências.

Por meio do cadastro de aparelhos, cálculos automáticos de consumo e relatórios personalizados, o sistema promove maior conscientização sobre o uso eficiente da energia, incentivando mudanças de comportamento que contribuam para a sustentabilidade.

---

## 🎯 Objetivo do Projeto

Desenvolver uma aplicação capaz de:

* Monitorar o consumo energético de aparelhos residenciais;
* Estimar gastos financeiros relacionados ao uso da energia elétrica;
* Apresentar relatórios e comparativos de consumo;
* Simular cenários de economia energética;
* Incentivar práticas mais sustentáveis através de recomendações e orientações educativas.

---

## 📊 Informações do Projeto

| Item                        | Detalhes                                 |
| --------------------------- | ---------------------------------------- |
| Tipo                        | Projeto Acadêmico                        |
| Curso                       | Gestão da Tecnologia da Informação (GTI) |
| Instituição                 | CESAR School                             |
| Disciplina                  | Projeto 1                                |
| Tema                        | Transição Energética                     |
| Linguagem Principal         | Python                                   |
| Arquitetura                 | Modular em Camadas                       |
| Persistência                | Arquivos TXT                             |
| Ambiente de Desenvolvimento | Visual Studio Code                       |
| Controle de Versão          | Git e GitHub                             |
| Status                      | Concluído                                |

---

## 🚀 Principais Funcionalidades

### 👤 Gestão de Usuários

* Cadastro de usuários;
* Login simplificado;
* Atualização de dados cadastrais;
* Exclusão de conta.

### 🔌 Gestão de Aparelhos

* Cadastro de aparelhos vinculados ao usuário;
* Organização por categorias;
* Atualização do tempo de uso;
* Remoção de aparelhos cadastrados.

### ⚡ Monitoramento Energético

* Cálculo do consumo energético em kWh;
* Estimativa de custo mensal;
* Classificação energética;
* Comparação com médias de consumo;
* Identificação de padrões de uso.

### 📈 Relatórios e Simulações

* Relatórios individuais por aparelho;
* Simulações de redução de consumo;
* Estimativas de economia financeira;
* Recomendações para uso mais eficiente da energia;
* Dicas educativas voltadas à conscientização energética.

### 🛡️ Robustez e Qualidade

* Persistência de dados em arquivos TXT;
* Tratamento de erros e inconsistências;
* Validação centralizada das entradas;
* Organização estrutural dos dados;
* Separação de responsabilidades entre os módulos.

---

## 🏗️ Arquitetura do Sistema

O EcoLar foi desenvolvido utilizando uma **arquitetura modular baseada em camadas**, visando facilitar manutenção, reutilização de código e escalabilidade futura.

### Estrutura Arquitetural

* **Views**

  * Responsáveis pela interface textual e interação com o usuário.

* **Controllers**

  * Coordenam o fluxo da aplicação e integram os módulos.

* **Services**

  * Implementam as regras de negócio e os cálculos do sistema.

* **Repositories**

  * Gerenciam a persistência e recuperação dos dados.

* **Utils**

  * Disponibilizam funções auxiliares, validações e formatações.

Essa organização promove maior clareza estrutural e reduz o acoplamento entre componentes.

---

## 📂 Estrutura do Projeto

```text
EcoLar/
│
├── main.py
├── README.md
├── requirements.txt
│
├── data/
├── repositories/
├── services/
├── controllers/
├── utils/
├── views/
└── docs/
```

---

## 🛠️ Tecnologias Utilizadas

* Python 3;
* Git;
* GitHub;
* Visual Studio Code;
* Arquivos TXT para persistência de dados.

---

## ▶️ Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/expedito-paes/ecolar-energy-awareness-app.git
```

### 2. Acesse a pasta do projeto

```bash
cd ecolar-energy-awareness-app
```

### 3. Execute a aplicação

```bash
python main.py
```

---

## 👥 Equipe do Projeto

Projeto desenvolvido pela **Equipe 4** da disciplina Projeto 1.

### Expedito Ferraz Gominho Paes

* Gestão do projeto;
* Planejamento e organização das atividades;
* Definição da arquitetura do sistema;
* Integração dos módulos desenvolvidos;
* Estruturação do fluxo de versionamento com Git;
* Documentação técnica e acadêmica;
* Apoio nos testes e estabilização da solução.

### Lucas Veiga de Aquino Souza Leite

* Desenvolvimento de software;
* Implementação das regras de negócio;
* Construção das funcionalidades do sistema.

### Raquel Moura Lins Acioli

* Experiência do usuário (UX);
* Organização visual;
* Estruturação da interface textual;
* Apoio à usabilidade da aplicação.

---

## 💡 Aprendizados Obtidos

O desenvolvimento do EcoLar proporcionou experiências práticas relacionadas a:

* Trabalho colaborativo em equipes multidisciplinares;
* Gestão de projetos de tecnologia;
* Planejamento e acompanhamento de entregas;
* Controle de versão utilizando Git e GitHub;
* Aplicação de arquitetura modular;
* Separação de responsabilidades;
* Desenvolvimento orientado à resolução de problemas reais;
* Comunicação e integração entre áreas técnicas e de gestão.

---

## 🔮 Possíveis Evoluções Futuras

Embora o projeto tenha sido concluído para fins acadêmicos, algumas melhorias podem expandir seu potencial:

* Persistência em banco de dados relacional;
* Interface gráfica ou aplicação web;
* Dashboards analíticos de consumo;
* Exportação de relatórios em PDF;
* Integração com APIs de tarifas energéticas;
* Cadastro automatizado de aparelhos;
* Geração de indicadores personalizados;
* Aplicação mobile.

---

## ✅ Status do Projeto

**Projeto concluído para fins acadêmicos, com funcionalidades implementadas, integração realizada e documentação estruturada.**

O EcoLar representa a aplicação prática de conceitos de desenvolvimento de software, arquitetura, gestão de projetos e trabalho em equipe, contribuindo para a formação técnica e profissional dos integrantes envolvidos.

---

## 🎓 Instituição

**CESAR School**
Graduação em Gestão da Tecnologia da Informação (GTI)
Disciplina: Projeto 1

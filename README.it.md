# 🌱 EcoLar

> **Applicazione sviluppata in Python per il monitoraggio e l'analisi dei consumi energetici domestici, promuovendo un utilizzo più consapevole dell'energia attraverso stime dei consumi, simulazioni di risparmio e raccomandazioni orientate alla sostenibilità.**

---

# 📌 Panoramica

**EcoLar** è un progetto accademico sviluppato nell'ambito del corso **Progetto 1** del **Corso di Laurea in Gestione delle Tecnologie dell'Informazione (GTI)** presso la **CESAR School**.

Il progetto nasce dalla sfida dedicata alla **Transizione Energetica**, con l'obiettivo di realizzare una soluzione semplice, accessibile ed educativa che aiuti gli utenti a comprendere come le proprie abitudini influenzino il consumo di energia elettrica nelle abitazioni.

Attraverso il monitoraggio dei consumi, la stima dei costi, simulazioni e suggerimenti personalizzati, EcoLar favorisce una maggiore consapevolezza energetica e incoraggia comportamenti più sostenibili.

Oltre allo sviluppo dell'applicazione, il progetto ha permesso di applicare concretamente concetti di ingegneria del software, architettura dei sistemi, gestione dei progetti, lavoro di squadra e problem solving.

---

# 🎯 Obiettivi del Progetto

L'obiettivo del progetto è sviluppare un'applicazione in grado di:

* Monitorare il consumo energetico degli elettrodomestici;
* Stimare il costo dell'energia elettrica consumata;
* Generare report dettagliati sui consumi;
* Simulare scenari di risparmio energetico;
* Incentivare comportamenti sostenibili attraverso suggerimenti educativi;
* Promuovere un utilizzo più efficiente dell'energia.

---

# 🏆 Principali Risultati Raggiunti

Al termine del progetto sono stati raggiunti i seguenti risultati:

* Sviluppo di un'applicazione completa in Python basata su un'architettura modulare a livelli;
* Implementazione di un sistema di gestione degli utenti;
* Gestione degli elettrodomestici associati a ciascun utente;
* Calcolo automatico del consumo energetico (kWh) e della spesa mensile stimata;
* Generazione di report personalizzati sui consumi;
* Simulazione di scenari di risparmio energetico;
* Suggerimenti per ridurre gli sprechi di energia;
* Organizzazione del software secondo il principio della separazione delle responsabilità;
* Sviluppo collaborativo utilizzando Git e GitHub durante tutto il ciclo di vita del progetto;
* Produzione di documentazione tecnica strutturata;
* Applicazione di metodologie di Project Management durante tutte le fasi dello sviluppo.

EcoLar dimostra come una soluzione tecnologica possa contribuire alla sensibilizzazione sull'efficienza energetica, integrando sostenibilità e sviluppo software.

---

# ✨ Punti di Forza

* 🔋 Monitoraggio dei consumi energetici domestici
* 💰 Stima dei costi dell'energia elettrica
* 📊 Report personalizzati sui consumi
* 📉 Simulazioni di risparmio energetico
* 🌱 Raccomandazioni orientate alla sostenibilità
* 🏗️ Architettura modulare a livelli
* 🔄 Controllo di versione con Git e GitHub
* 👥 Sviluppo collaborativo
* 🎓 Progetto accademico basato su una problematica reale

---

# 📊 Informazioni sul Progetto

| Voce                  | Descrizione                                       |
| --------------------- | ------------------------------------------------- |
| Progetto              | EcoLar                                            |
| Tipologia             | Progetto Accademico                               |
| Corso di Laurea       | Gestione delle Tecnologie dell'Informazione (GTI) |
| Istituzione           | CESAR School                                      |
| Insegnamento          | Progetto 1                                        |
| Tema                  | Transizione Energetica                            |
| Linguaggio Principale | Python                                            |
| Architettura          | Architettura Modulare a Livelli                   |
| Persistenza dei Dati  | File TXT                                          |
| IDE                   | Visual Studio Code                                |
| Controllo di Versione | Git e GitHub                                      |
| Stato                 | Completato                                        |

---

# 🚀 Funzionalità Principali

## 👤 Gestione Utenti

* Registrazione degli utenti;
* Autenticazione;
* Aggiornamento dei dati personali;
* Eliminazione dell'account.

## 🔌 Gestione degli Elettrodomestici

* Registrazione degli elettrodomestici;
* Organizzazione per categorie;
* Aggiornamento delle informazioni;
* Eliminazione degli apparecchi.

## ⚡ Monitoraggio Energetico

* Calcolo automatico del consumo in kWh;
* Stima della spesa mensile;
* Classificazione energetica;
* Confronto dei consumi;
* Analisi delle abitudini di utilizzo.

## 📈 Report e Simulazioni

* Report individuali per ogni apparecchio;
* Simulazioni di risparmio energetico;
* Stima del risparmio economico;
* Suggerimenti personalizzati;
* Consigli educativi per un consumo più efficiente.

## 🛡️ Qualità del Software

* Persistenza dei dati tramite file TXT;
* Validazione centralizzata degli input;
* Gestione delle eccezioni;
* Organizzazione modulare del codice;
* Separazione delle responsabilità tra i componenti.

---

# 🏗️ Architettura del Sistema

EcoLar è stato sviluppato seguendo un'architettura modulare a livelli, progettata per favorire manutenibilità, riutilizzo del codice ed evoluzione futura.

```text
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

Gestiscono l'interazione con l'utente tramite interfaccia testuale.

### Controllers

Coordinano il flusso dell'applicazione e la comunicazione tra i vari livelli.

### Services

Implementano la logica di business e i calcoli energetici.

### Repositories

Gestiscono il salvataggio e il recupero dei dati.

### Utils

Contengono funzioni di supporto, validazioni e formattazioni.

---

# 📂 Struttura del Progetto

```text
EcoLar/
│
├── main.py
├── README.md
├── README.en.md
├── README.it.md
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

# 🛠️ Tecnologie Utilizzate

* Python 3
* Git
* GitHub
* Visual Studio Code
* File TXT per la persistenza dei dati

---

# ▶️ Come Eseguire il Progetto

## 1. Clonare il repository

```bash
git clone https://github.com/expedito-paes/ecolar-energy-awareness-app.git
```

## 2. Accedere alla cartella del progetto

```bash
cd ecolar-energy-awareness-app
```

## 3. Avviare l'applicazione

```bash
python main.py
```

---

# 👥 Team di Sviluppo

## Expedito Ferraz Gominho Paes

**Project Manager**

* Pianificazione e coordinamento del progetto;
* Gestione del cronoprogramma;
* Definizione dell'architettura del software;
* Organizzazione del flusso di versionamento con Git;
* Integrazione dei moduli;
* Documentazione tecnica;
* Supporto ai test e validazione della soluzione.

## Lucas Veiga de Aquino Souza Leite

**Software Developer**

* Sviluppo delle funzionalità;
* Implementazione della logica di business;
* Realizzazione dei moduli principali.

## Raquel Moura Lins Acioli

**UX Designer**

* Progettazione dell'esperienza utente;
* Organizzazione dell'interfaccia testuale;
* Miglioramento dell'usabilità.

---

# 💡 Competenze Acquisite

Durante il progetto sono state sviluppate competenze in:

* Project Management;
* Ingegneria del Software;
* Architettura dei Sistemi;
* Programmazione in Python;
* Git e GitHub;
* Progettazione di applicazioni modulari;
* Collaborazione in team;
* Comunicazione tecnica;
* Documentazione software;
* Problem Solving;
* Soluzioni tecnologiche orientate alla sostenibilità.

---

# 🔮 Sviluppi Futuri

Possibili evoluzioni del progetto includono:

* Integrazione con database relazionali;
* Interfaccia grafica (GUI);
* Applicazione Web;
* Applicazione Mobile;
* Dashboard interattive;
* Esportazione dei report in PDF;
* Integrazione con API delle tariffe energetiche;
* Catalogo automatico degli elettrodomestici;
* Indicatori personalizzati delle prestazioni energetiche.

---

# ✅ Stato del Progetto

**Progetto completato con successo** nell'ambito dell'insegnamento **Progetto 1** della **CESAR School**.

EcoLar rappresenta l'applicazione pratica di concetti di ingegneria del software, architettura dei sistemi, gestione dei progetti, controllo di versione e sviluppo collaborativo, dimostrando come la tecnologia possa contribuire alla promozione di un consumo energetico più sostenibile.

---

# 🎓 Istituzione

**CESAR School**

Corso di Laurea in Gestione delle Tecnologie dell'Informazione (GTI)

Insegnamento: Progetto 1

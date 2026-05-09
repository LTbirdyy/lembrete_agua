# 💧 Lembrete de Água Inteligente

[![Build](https://github.com/LTbirdyy/lembrete_agua/actions/workflows/python.yml/badge.svg)](https://github.com/LTbirdyy/lembrete_agua/actions)

Aplicação web desenvolvida em Python com o objetivo de ajudar usuários a manterem uma rotina saudável de hidratação ao longo do dia.

---

## 🚀 Aplicação Online

Acesse aqui: *(adicione o link após o deploy)*

---

## 🎯 Descrição do Problema

Muitas pessoas esquecem de beber água durante o dia, o que pode causar problemas como desidratação, fadiga e baixa concentração.

---

## ✅ Proposta de Solução

Este projeto oferece um sistema interativo que:

* Define uma meta diária de consumo de água
* Permite registrar o consumo ao longo do dia
* Exibe progresso em tempo real
* Integra dados de clima para recomendações
* Armazena histórico em arquivo JSON

---

## 👥 Público-alvo

Pessoas que passam muito tempo no computador (trabalho, estudo, jogos) e acabam esquecendo de se hidratar.

---

## ⚙️ Funcionalidades principais

* 📊 Definir meta diária de água (ml)
* ➕ Registrar consumo
* 📈 Barra de progresso dinâmica
* 🌡️ Integração com API de clima
* 💾 Histórico salvo em JSON
* 🎨 Interface web interativa (dashboard)

---

## 🛠️ Tecnologias utilizadas

* Python 3.13
* Streamlit (interface web)
* Requests (consumo de API)
* JSON (armazenamento)
* Pytest (testes automatizados)
* GitHub Actions (CI)

---

## 🌐 API utilizada

* OpenWeatherMap API
  Utilizada para obter a temperatura atual e sugerir aumento no consumo de água em dias quentes.

---

## 📁 Estrutura do projeto

```
lembrete_agua/
├── src/
│   ├── interface/
│   │   └── app.py
│   ├── logic/
│   ├── services/
├── data/
│   └── historico.json
├── tests/
├── .streamlit/
│   └── config.toml
├── .github/workflows/
├── requirements.txt
└── README.md
```

---

## ▶️ Como executar o projeto

### 🔹 1. Clonar o repositório

```bash
git clone https://github.com/LTbirdyy/lembrete_agua.git
cd lembrete_agua
```

---

### 🔹 2. Criar ambiente virtual

#### Windows:

```bash
py -m venv .venv
.venv\Scripts\activate
```

#### Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 🔹 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 🔹 4. Executar a aplicação

```bash
python -m streamlit run src/interface/app.py
```

---

## 🧪 Testes automatizados

```bash
python -m pytest
```

---

## 🧹 Linting

```bash
python -m flake8
```

---

## ⚙️ Integração Contínua (CI)

O projeto utiliza GitHub Actions para:

* Executar testes automaticamente
* Validar qualidade do código

---

## 🏗️ Arquitetura

O projeto foi estruturado seguindo separação de responsabilidades:

* Interface → Streamlit (`interface/`)
* Regras de negócio → (`logic/`)
* Integrações externas (API) → (`services/`)

---

## 🔢 Versionamento

Versão atual:

```
v2.0.0
```

---

## 👨‍💻 Autor

Gabriel Rosa

---

## 📄 Repositório

https://github.com/LTbirdyy/lembrete_agua

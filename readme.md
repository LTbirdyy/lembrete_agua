# 💧 Lembrete de Água Inteligente

[![Build](https://github.com/LTbirdyy/lembrete_agua/actions/workflows/python.yml/badge.svg)](https://github.com/LTbirdyy/lembrete_agua/actions)

Aplicação web desenvolvida em Python com o objetivo de ajudar usuários a manterem uma rotina saudável de hidratação ao longo do dia.

---

## 🚀 Aplicação Online

Acesse aqui: https://lembreteagua-tfnfzda6zs9notewgwq3v2.streamlit.app

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
* Armazena histórico em banco de dados na nuvem

---

## 👥 Público-alvo

Pessoas que passam muito tempo no computador (trabalho, estudo ou lazer) e acabam esquecendo de se hidratar.

---

## ⚙️ Funcionalidades principais

* 📊 Definir meta diária de água (ml)
* ➕ Registrar consumo
* 📈 Barra de progresso dinâmica
* 🌡️ Integração com API de clima
* 💧 Recomendações de hidratação com base nas condições climáticas
* ☁️ Histórico salvo em banco de dados Supabase
* 🎨 Interface web interativa (dashboard)
* 🚀 Aplicação disponível online

---

## 🛠️ Tecnologias utilizadas

* Python 3.13
* Streamlit (interface web)
* Supabase (banco de dados)
* Requests (consumo de API)
* OpenWeatherMap API
* Pytest (testes automatizados)
* Flake8 (análise estática)
* GitHub Actions (CI/CD)

---

## 🌐 API utilizada

### OpenWeatherMap API

Utilizada para obter informações climáticas em tempo real:

* Temperatura
* Umidade
* Sensação térmica
* Velocidade do vento
* Condição climática

Esses dados são utilizados para fornecer recomendações personalizadas de hidratação.

---

## 🗄️ Banco de Dados

O projeto utiliza o Supabase para armazenamento persistente dos dados.

Tabela utilizada:

| Campo      | Tipo    |
| ---------- | ------- |
| id         | bigint  |
| data       | text    |
| consumo    | integer |
| meta       | integer |
| bateu_meta | boolean |

---

## 📁 Estrutura do projeto

```text
lembrete_agua/
├── src/
│   ├── interface/
│   │   ├── services/
│   │   │   ├── clima.py
│   │   │   └── db.py
│   │   └── app.py
│   ├── logic/
│   │   ├── consumo.py
│   │   └── historico.py
│
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

#### Windows

```bash
py -m venv .venv
.venv\Scripts\activate
```

#### Linux/macOS

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

### 🔹 4. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
API_KEY=sua_chave_openweathermap

SUPABASE_URL=sua_url_supabase
SUPABASE_KEY=sua_chave_supabase
```

---

### 🔹 5. Executar a aplicação

```bash
streamlit run src/interface/app.py
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
* Garantir a integridade antes do merge na branch principal

---

## 🏗️ Arquitetura

O projeto foi estruturado seguindo separação de responsabilidades:

* Interface → Streamlit (`interface/`)
* Regras de negócio → (`logic/`)
* Serviços externos → (`services/`)
* Banco de dados → Supabase

---

## 🔀 Fluxo de Desenvolvimento

O projeto utiliza Git e GitHub Flow:

* Criação de Issues para planejamento
* Desenvolvimento em branches separadas
* Pull Requests para integração
* Code Review entre integrantes
* Merge apenas após aprovação e testes automatizados

---

## 🔢 Versionamento

Versão atual:

```text
v3.0.0
```

---

## 👨‍💻 Integrantes

* Gabriel Rosa
* José Gabriel

---

## 📄 Repositório

https://github.com/LTbirdyy/lembrete_agua

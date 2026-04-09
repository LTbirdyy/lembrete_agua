# 💧 Lembrete de Água

Aplicação desktop desenvolvida em Python com o objetivo de ajudar usuários a manterem uma rotina saudável de hidratação ao longo do dia.

---

## 🎯 Problema

Muitas pessoas esquecem de beber água durante o dia, o que pode causar problemas de saúde como desidratação, fadiga e baixa concentração.

---

## ✅ Solução

Este projeto oferece um sistema simples que:

* Define uma meta diária de consumo de água
* Envia lembretes periódicos
* Registra o consumo ao longo do dia
* Armazena histórico em arquivo JSON

---

## 🖥️ Interface

Aplicação com interface gráfica utilizando Tkinter, permitindo interação simples e intuitiva com o usuário.

---

## ⚙️ Funcionalidades

* 📊 Definir meta diária de água (ml)
* ⏰ Configurar intervalo de lembretes
* 🔔 Alertas sonoros
* ➕ Registrar consumo
* 📈 Barra de progresso
* 🛑 Parar e salvar dados
* 💾 Histórico salvo em JSON

---

## 🛠️ Tecnologias utilizadas

* Python 3.x
* Tkinter (interface gráfica)
* JSON (armazenamento de dados)

---

## 📦 Bibliotecas utilizadas

### 🔹 Bibliotecas padrão do Python (não precisam instalar)

* `tkinter` → interface gráfica
* `json` → manipulação de arquivos JSON
* `os` → manipulação de caminhos
* `datetime` → controle de datas
* `winsound` → reprodução de som (Windows)

### 🔹 Bibliotecas externas

* `pytest` → testes automatizados
* `flake8` → linting (análise estática)

---

## 📁 Estrutura do projeto

```
lembrete_agua/
├── src/
│   ├── interface/
│   ├── logic/
│   └── main.py
├── data/
│   └── historico.json
├── tests/
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

### 🔹 2. Criar ambiente virtual (opcional, recomendado)

```bash
py -m venv .venv
.venv\Scripts\activate
```

---

### 🔹 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 🔹 4. Executar o projeto

⚠️ Importante:

O projeto deve ser executado como módulo, para evitar erro de importação.

```bash
py -m src.main
```

---

## 🧪 Testes automatizados

Para rodar os testes:

```bash
py -m pytest
```

---

## 🧹 Linting (qualidade de código)

Para verificar o código:

```bash
py -m flake8
```

---

## ⚙️ Integração Contínua (CI)

O projeto utiliza GitHub Actions para:

* Executar testes automaticamente
* Validar padrão de código com flake8

A cada push, o sistema verifica se o projeto está funcionando corretamente.

---

## 🔢 Versionamento

O projeto segue versionamento semântico:

```
v1.0.0
```

---

## 👨‍💻 Autor

Gabriel Rosa

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos.

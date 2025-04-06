# 🏆 Golden Raspberry Awards API

[![CI](https://github.com/seu-usuario/golden-raspberry-awards/actions/workflows/ci.yml/badge.svg)](https://github.com/GilJSantana/golden-raspberry-awards/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)

API construída com **FastAPI** e **SQLite in-memory** para análise dos dados históricos do prêmio Golden Raspberry Awards.

---

## 📁 Estrutura

- `dados/Movielist.csv` — Fonte de dados
- `csv_loader.py` — Carrega os dados do CSV na base SQLite em memória
- `database.py` — Inicializa e mantém a conexão com o banco
- `service.py` — Lógica de negócio e manipulação de dados
- `api.py` — Define os endpoints da API
- `main.py` — Ponto de entrada para execução da API com Uvicorn
- `tests/` — Testes automatizados com `pytest` e `httpx`

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/golden-raspberry-awards.git
cd golden-raspberry-awards
```

### 2. Instale o Poetry (se ainda não tiver)

```bash
pip install poetry
```

### 3. Instale as dependências

```bash
poetry install
```

### 4. Ative o shell do Poetry

```bash
poetry shell
```

---

## 🧪 Como rodar os testes

Antes de rodar os testes, defina o `PYTHONPATH` apontando para o diretório raiz do projeto:

Linux/macOS:

```bash
export PYTHONPATH=$(pwd)
```

Windows (CMD):

```cmd
set PYTHONPATH=%cd%
```

Execute os testes com:

```bash
pytest
```

---

## 🌐 Como executar a API



Execute o modulo main.py :

```bash
poetry run python main.py
```

Acesse em:  
📍 `http://127.0.0.1:8000`  
📄 Documentação Swagger: `http://127.0.0.1:8000/docs`

---

## 🔗 Como consumir a API

### ✅ `GET /producers/intervals`

Retorna os produtores com os maiores e menores intervalos entre vitórias.

```bash
curl http://127.0.0.1:8000/producers/intervals
```

---

### ✅ `GET /winners?year=1986`

Retorna os filmes vencedores de um determinado ano.

```bash
curl "http://127.0.0.1:8000/winners?year=1986"
```

---

### ✅ `GET /studios-ranking`

Retorna os estúdios com maior número de vitórias.

---

### ✅ `GET /years-with-multiple-winners`

Retorna os anos com mais de um filme vencedor.

---

## ✅ Integração Contínua (CI)

Este projeto utiliza **GitHub Actions** para executar os testes automaticamente a cada push ou pull request para o ramo `main`.

O pipeline realiza as seguintes etapas:

1. Clona o repositório
2. Instala o Python 3.10
3. Instala as dependências via Poetry
4. Configura `PYTHONPATH`
5. Executa os testes com `pytest`

Badge de status:  
[![CI](https://github.com/seu-usuario/golden-raspberry-awards/actions/workflows/ci.yml/badge.svg)](https://github.com/GilJSantana/golden-raspberry-awards/actions/workflows/ci.yml)

---

## 📌 Requisitos

- Python 3.10+
- [Poetry](https://python-poetry.org/)

---





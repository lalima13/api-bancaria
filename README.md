<<<<<<< HEAD
# API Bancária

API de exemplo construída com FastAPI para gerenciar contas e transações.

## Pré-requisitos

- Python 3.11+
- PostgreSQL local ou em container
- Virtualenv ou Poetry instalado

## Instalação

```bash
git clone https://github.com/lalima13/api-bancaria.git
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> Se você usa Poetry, rode `poetry install`.

## Configuração do banco de dados

O arquivo `src/config.py` já define uma URL padrão para PostgreSQL:

```python
postgresql://devlucas:teste123@localhost:5432/api_bancaria
```

Altere os valores se precisar, ou crie um arquivo `.env` com:

```env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/api_bancaria
ENVIRONMENT=production
```

## Como executar

```bash
uvicorn src.main:app --reload
```

A API ficará disponível em:

- `http://127.0.0.1:8000`
- Swagger: `http://127.0.0.1:8000/docs`

## Endpoints principais

### 1) Autenticação

**POST** `/auth/login`

Body JSON:

```json
{
  "user_id": 1
}
```

Resposta:

```json
{
  "access_token": "eyJ..."
}
```

Use o token retornado em todas as chamadas protegidas:

Header:

```
Authorization: Bearer <access_token>
```

### 2) Criar conta

**POST** `/accounts`

Header:

```
Authorization: Bearer <token>
```

Body JSON:

```json
{
  "user_id": 1,
  "balance": 0
}
```

### 3) Listar contas

**GET** `/accounts`

Header:

```
Authorization: Bearer <token>
```

Query params:

- `limit` = `10`
- `skip` = `0`

URL de exemplo:

```
http://127.0.0.1:8000/accounts?limit=10&skip=0
```

### 4) Listar transações de uma conta

**GET** `/accounts/{id}/transactions`

Header:

```
Authorization: Bearer <token>
```

Query params:

- `limit` = `10`
- `skip` = `0`

URL de exemplo:

```
http://127.0.0.1:8000/accounts/1/transactions?limit=10&skip=0
```

### 5) Criar transação (depósito)

**POST** `/transactions`

Header:

```
Authorization: Bearer <token>
```

Body JSON:

```json
{
  "account_id": 1,
  "type": "deposit",
  "amount": 100
}
```

### 6) Criar transação (saque)

**POST** `/transactions`

Header:

```
Authorization: Bearer <token>
```

Body JSON:

```json
{
  "account_id": 1,
  "type": "withdrawal",
  "amount": 50
}
```

## Dicas para Insomnia

- Sempre use o token do login no cabeçalho `Authorization: Bearer ...`.
- Para GETs, não use body JSON, apenas query params.
- No Insomnia, crie dois parâmetros separados:
  - `limit` = `10`
  - `skip` = `0`
- Nunca coloque `limit=10` como nome de parâmetro.

## Observações

- O endpoint `/accounts` e `/transactions` são protegidos por JWT.
- Para testar o fluxo completo:
  1. Faça login em `/auth/login`.
  2. Crie uma conta em `/accounts`.
  3. Liste contas em `/accounts`.
  4. Faça depósitos/saques em `/transactions`.
  5. Veja transações em `/accounts/1/transactions`.
=======
# 🏦 API Bancária

API REST construída com **FastAPI** e **PostgreSQL** para gerenciar usuários, contas e transações bancárias. Projeto desenvolvido para demonstrar boas práticas de desenvolvimento com Python, autenticação JWT e modelagem de banco de dados relacional.

---

## 🛠️ Tecnologias utilizadas

- **Python 3.11+**
- **FastAPI** — framework web moderno e de alta performance
- **PostgreSQL** — banco de dados relacional
- **SQLAlchemy** — ORM para mapeamento objeto-relacional
- **JWT** — autenticação via token
- **Uvicorn** — servidor ASGI
>>>>>>> fa9139aa6fc6d1151b4fcf1b2f163c08b89cc8c0

---

## ✅ Pré-requisitos

Antes de começar, você precisa ter instalado na sua máquina:

- [Python 3.11+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/) (versão 13 ou superior)
- [Git](https://git-scm.com/)

---

## 🚀 Instalação e configuração

### 1. Clone o repositório

```bash
git clone https://github.com/lalima13/api-bancaria.git
cd api-bancaria
```

### 2. Crie e ative o ambiente virtual

```bash
# Criar o ambiente virtual
python -m venv .venv

# Ativar no Linux/macOS
source .venv/bin/activate

# Ativar no Windows (CMD)
.venv\Scripts\activate

# Ativar no Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 🗄️ Configuração do PostgreSQL

Esta é a etapa mais importante. Você precisa criar um banco de dados local antes de rodar a API.

### Passo 1 — Acesse o PostgreSQL pelo terminal

```bash
# Linux/macOS
psql -U postgres

# Windows (pelo CMD, com PostgreSQL no PATH)
psql -U postgres
```

> Caso não tenha o `psql` no PATH no Windows, abra o **pgAdmin** (instalado junto com o PostgreSQL) e use o Query Tool para executar os comandos abaixo.

### Passo 2 — Crie o usuário e o banco de dados

Execute os comandos abaixo **dentro do psql** (ou no Query Tool do pgAdmin):

```sql
-- Criar o usuário
CREATE USER devlucas WITH PASSWORD 'teste123';

-- Criar o banco de dados
CREATE DATABASE api_bancaria OWNER devlucas;

-- Conceder todos os privilégios
GRANT ALL PRIVILEGES ON DATABASE api_bancaria TO devlucas;
```

Para sair do psql:

```bash
\q
```

### Passo 3 — Configure a variável de ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
DATABASE_URL=postgresql://devlucas:teste123@localhost:5432/api_bancaria
```

> O arquivo `.env` já é lido automaticamente pela aplicação. Não é necessário alterar nenhum outro arquivo.

---

## ▶️ Executando a aplicação

Com o banco configurado e o ambiente virtual ativo, rode:

```bash
uvicorn src.main:app --reload
```

A API estará disponível em:

| Interface | URL |
|---|---|
| API Base | http://127.0.0.1:8000 |
| Documentação interativa (Swagger) | http://127.0.0.1:8000/docs |
| Documentação alternativa (Redoc) | http://127.0.0.1:8000/redoc |

> 💡 Recomendo usar o **Swagger** (`/docs`) para testar todos os endpoints diretamente pelo navegador, sem precisar de nenhuma ferramenta externa.

---

## 🔁 Fluxo de uso recomendado

Para testar o funcionamento completo da API, siga esta ordem:

```
1. POST /auth/login        → Obter o token JWT
2. POST /accounts          → Criar uma conta bancária
3. GET  /accounts          → Listar contas existentes
4. POST /transactions      → Realizar depósito ou saque
5. GET  /accounts/{id}/transactions → Ver extrato da conta
```

---

## 📋 Endpoints

### 🔐 Autenticação

#### `POST /auth/login`

Gera um token JWT para autenticar nas demais rotas.

**Body:**
```json
{
  "user_id": 1
}
```

**Resposta:**
```json
{
  "access_token": "eyJ..."
}
```

> ⚠️ Copie o valor de `access_token`. Ele será necessário em todas as chamadas protegidas.

**Como usar o token:**

Em todas as rotas protegidas, adicione o seguinte cabeçalho HTTP:

```
Authorization: Bearer <access_token>
```

---

### 🏦 Contas

#### `POST /accounts` — Criar conta

**Header:**
```
Authorization: Bearer <token>
```

**Body:**
```json
{
  "user_id": 1,
  "balance": 0
}
```

---

#### `GET /accounts` — Listar contas

**Header:**
```
Authorization: Bearer <token>
```

**Query params (opcionais):**

| Parâmetro | Padrão | Descrição |
|---|---|---|
| `limit` | `10` | Quantidade de resultados |
| `skip` | `0` | Quantidade a pular (paginação) |

**Exemplo:**
```
GET http://127.0.0.1:8000/accounts?limit=10&skip=0
```

---

### 💸 Transações

#### `POST /transactions` — Criar transação

**Header:**
```
Authorization: Bearer <token>
```

**Depósito:**
```json
{
  "account_id": 1,
  "type": "deposit",
  "amount": 100
}
```

**Saque:**
```json
{
  "account_id": 1,
  "type": "withdrawal",
  "amount": 50
}
```

---

#### `GET /accounts/{id}/transactions` — Listar transações de uma conta

**Header:**
```
Authorization: Bearer <token>
```

**Query params (opcionais):**

| Parâmetro | Padrão | Descrição |
|---|---|---|
| `limit` | `10` | Quantidade de resultados |
| `skip` | `0` | Quantidade a pular (paginação) |

**Exemplo:**
```
GET http://127.0.0.1:8000/accounts/1/transactions?limit=10&skip=0
```

---

## 🧪 Testando com Insomnia ou Postman

Se preferir testar com Insomnia ou Postman ao invés do Swagger:

1. Faça a requisição de login e copie o `access_token` da resposta.
2. Em todas as outras requisições, vá em **Headers** e adicione:
   - **Key:** `Authorization`
   - **Value:** `Bearer <cole_o_token_aqui>`
3. Para requisições GET, use **Query Params** (não Body):
   - Adicione `limit` = `10` e `skip` = `0` como parâmetros separados.

---

## ❗ Solução de problemas comuns

**Erro: `connection refused` ou `could not connect to server`**
> O PostgreSQL não está rodando. Inicie o serviço:
> - Windows: Abra o **Services** (`services.msc`) e inicie o `postgresql-x64-XX`
> - Linux: `sudo systemctl start postgresql`
> - macOS: `brew services start postgresql`

**Erro: `role "devlucas" does not exist`**
> O usuário do banco não foi criado. Repita o Passo 2 da seção de configuração do PostgreSQL.

**Erro: `database "api_bancaria" does not exist`**
> O banco de dados não foi criado. Repita o Passo 2 da seção de configuração do PostgreSQL.

**Erro: `ModuleNotFoundError`**
> O ambiente virtual não está ativo. Execute `source .venv/bin/activate` (Linux/macOS) ou `.venv\Scripts\activate` (Windows) e tente novamente.

---

## 👨‍💻 Autor

Desenvolvido por **Lucas Lima**

[![GitHub](https://img.shields.io/badge/GitHub-lalima13-181717?style=flat&logo=github)](https://github.com/lalima13)

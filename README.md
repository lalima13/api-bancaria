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



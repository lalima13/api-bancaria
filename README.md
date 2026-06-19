## Criação de uma API utilizando FastAPI

### Como usar localmente

1. Instale dependências com Poetry ou pip.
2. Configure o banco Postgres em `src/config.py` ou via `.env`.
3. Inicie a API:
   - `uvicorn src.main:app --reload`
4. Acesse o Swagger em `http://127.0.0.1:8000/docs`.

### Fluxo de uso

- `POST /auth/login`
  - Body: `{ "user_id": 1 }`
  - Retorna `access_token`.
- Copie o token e use como cabeçalho `Authorization: Bearer <token>`.
- `POST /accounts`
  - Body: `{ "user_id": 1, "balance": 0 }`
- `GET /accounts?limit=10&skip=0`
- `POST /transactions`
  - Body: `{ "account_id": 1, "type": "deposit", "amount": 100 }`



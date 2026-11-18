# Catálogo de Livros

Integrante: **Luis Felipe Andrade Dias**.

API em FastAPI para listar livros, buscar um livro por ID e consultar o total de títulos. Os dados ficam em memória.

## Como rodar

No Windows, abra o Git Bash na pasta do projeto. É preciso ter Python 3.11 ou superior.

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
export TOKEN_API="token-local"
python -m uvicorn main:app --reload
```

Abra o [Swagger UI](http://127.0.0.1:8000/docs) para consultar e testar as rotas. Para acessar `GET /resumo`, clique em **Authorize** e digite o valor de `TOKEN_API` (`token-local` no exemplo).

## Como rodar os testes

Com o ambiente virtual ativado no Git Bash, execute os testes. O servidor pode ficar desligado.

```bash
python -m pytest -q
```

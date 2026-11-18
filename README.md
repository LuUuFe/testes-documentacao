# Catálogo de Livros

Projeto de **Luis Felipe Andrade Dias**.

API em FastAPI para listar livros, buscar um livro por ID e consultar o total de títulos. Os dados ficam em memória.

## Como rodar

Com Python 3.11 ou superior, abra um terminal na pasta do projeto.

**Windows (PowerShell)**

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:TOKEN_API = "token-local"
.\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

**Linux ou macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
export TOKEN_API="token-local"
python -m uvicorn main:app --reload
```

Abra o [Swagger UI](http://127.0.0.1:8000/docs) para consultar e testar as rotas. Para acessar `GET /resumo`, clique em **Authorize** e digite o valor de `TOKEN_API` (`token-local` no exemplo).

## Como rodar os testes

O servidor pode ficar desligado durante os testes.

```powershell
# Windows (PowerShell)
.\.venv\Scripts\python.exe -m pytest -q
```

```bash
# Linux ou macOS, com o ambiente virtual ativado
python -m pytest -q
```

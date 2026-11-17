import os

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel

app = FastAPI()
bearer = HTTPBearer(auto_error=False)


class Livro(BaseModel):
    id: int
    titulo: str
    autor: str


livros = [
    Livro(id=1, titulo="Dom Casmurro", autor="Machado de Assis"),
    Livro(id=2, titulo="O Cortiço", autor="Aluísio Azevedo"),
]


@app.get("/livros")
def listar_livros() -> list[Livro]:
    return livros


@app.get("/livros/{livro_id}")
def buscar_livro(livro_id: int) -> Livro:
    for livro in livros:
        if livro.id == livro_id:
            return livro

    raise HTTPException(status_code=404, detail="Livro não encontrado.")


@app.get("/resumo")
def ver_resumo(
    credenciais: HTTPAuthorizationCredentials | None = Depends(bearer),
) -> dict[str, int]:
    token = os.getenv("TOKEN_API")
    if not token or not credenciais or credenciais.credentials != token:
        raise HTTPException(
            status_code=401,
            detail="Token ausente ou inválido.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {"total_livros": len(livros)}

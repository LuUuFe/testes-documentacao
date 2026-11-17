import os

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel

app = FastAPI(
    title="Catálogo de Livros",
    description="API para consultar os livros do catálogo e o total de títulos disponíveis.",
    openapi_tags=[
        {"name": "Livros", "description": "Consultas ao catálogo."},
        {"name": "Resumo", "description": "Informações do catálogo que exigem token."},
    ],
)
bearer = HTTPBearer(auto_error=False)


class Livro(BaseModel):
    id: int
    titulo: str
    autor: str


livros = [
    Livro(id=1, titulo="Dom Casmurro", autor="Machado de Assis"),
    Livro(id=2, titulo="O Cortiço", autor="Aluísio Azevedo"),
]


@app.get(
    "/livros",
    tags=["Livros"],
    summary="Listar livros",
    response_description="Lista com o ID, o título e o autor de cada livro.",
)
def listar_livros() -> list[Livro]:
    """Retorna todos os livros cadastrados no catálogo."""
    return livros


@app.get(
    "/livros/{livro_id}",
    tags=["Livros"],
    summary="Buscar livro por ID",
    response_description="Dados do livro encontrado.",
    responses={404: {"description": "Livro não encontrado."}},
)
def buscar_livro(livro_id: int) -> Livro:
    """Consulta um livro pelo ID retornado na listagem do catálogo."""
    for livro in livros:
        if livro.id == livro_id:
            return livro

    raise HTTPException(status_code=404, detail="Livro não encontrado.")


@app.get(
    "/resumo",
    tags=["Resumo"],
    summary="Consultar total de livros",
    response_description="Quantidade de livros cadastrados.",
    responses={401: {"description": "Token ausente ou inválido."}},
)
def ver_resumo(
    credenciais: HTTPAuthorizationCredentials | None = Depends(bearer),
) -> dict[str, int]:
    """Retorna o total de livros. Use o token configurado em `TOKEN_API`."""
    token = os.getenv("TOKEN_API")
    if not token or not credenciais or credenciais.credentials != token:
        raise HTTPException(
            status_code=401,
            detail="Token ausente ou inválido.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {"total_livros": len(livros)}

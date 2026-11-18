from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_listar_livros():
    resposta = client.get("/livros")

    assert resposta.status_code == 200
    assert [livro["id"] for livro in resposta.json()] == [1, 2]


def test_buscar_livro():
    resposta = client.get("/livros/1")

    assert resposta.status_code == 200
    assert resposta.json() == {
        "id": 1,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
    }


def test_livro_nao_encontrado():
    resposta = client.get("/livros/999")

    assert resposta.status_code == 404
    assert resposta.json() == {"detail": "Livro não encontrado."}


def test_id_invalido():
    resposta = client.get("/livros/abc")

    assert resposta.status_code == 422


def test_resumo_sem_token(monkeypatch):
    monkeypatch.setenv("TOKEN_API", "token-teste")

    resposta = client.get("/resumo")

    assert resposta.status_code == 401
    assert resposta.headers["WWW-Authenticate"] == "Bearer"


def test_resumo_com_token_invalido(monkeypatch):
    monkeypatch.setenv("TOKEN_API", "token-teste")

    resposta = client.get("/resumo", headers={"Authorization": "Bearer errado"})

    assert resposta.status_code == 401
    assert resposta.json() == {"detail": "Token ausente ou inválido."}


def test_resumo_com_token_valido(monkeypatch):
    monkeypatch.setenv("TOKEN_API", "token-teste")

    resposta = client.get("/resumo", headers={"Authorization": "Bearer token-teste"})

    assert resposta.status_code == 200
    assert resposta.json() == {"total_livros": 2}

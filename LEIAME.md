# Home Movies Collection (Coleção de Filmes Pessoais) [#5](https://github.com/gilvandovieira/meta/issues/5)

[In english](README.md)

Esse projeto tinha/tem como objetivo de aprendizado de python usando Django Django-rest-framework e pytest. É dado como completo com a API mínima, + usar o django-admin para gerenciar as entidades, com usuários que podem criar e outros que podem só visualizar.

Esse projeto contém 2 entidades principais, Filme e Ator.

- Um **ator** tem um nome e pode (ou não) estar em algum Filme.
- Um **filme** tem um nome, um ano de publicação e atores no elenco.

![Caso de uso 1](docs/usecase1.png)

```python
# Model do Ator
class Ator(models.Model):
    nome = models.CharField(max_length=255, null=False)
    def __str__(self):
        return self.nome
```

```python
# Model do Filme
class Filme(models.Model):
    nome = models.CharField(max_length=255, null=False)
    atores = models.ManyToManyField(Ator, related_name='filmes', related_query_name='filme')
    ano = models.IntegerField(null=False)

    def __str__(self):
        return '%s (%d)' % (self.nome, self.ano)
```

### Usando o [httpie](https://httpie.org/) nós temos

Fazendo uma requisição GET sem passar dados de autorização retorna status 403

```json
$ http http://localhost:8000/resources/atores/

HTTP/1.1 403 Forbidden
Allow: GET, POST, HEAD, OPTIONS
Content-Length: 58
Content-Type: application/json
Date: Tue, 18 Feb 2020 21:05:05 GMT
Server: WSGIServer/0.2 CPython/3.8.1
Vary: Accept, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "detail": "Authentication credentials were not provided."
}
```

Passando um usuário e senha válidos no recurso de Atores

```json
$ http -a user:password http://localhost:8000/resources/atores/

HTTP/1.1 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Length: 69
Content-Type: application/json
Date: Tue, 18 Feb 2020 21:10:04 GMT
Server: WSGIServer/0.2 CPython/3.8.1
Vary: Accept, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

[
    {
        "filmes": [
            1,
            2
        ],
        "id": 1,
        "nome": "L"
    },
    {
        "filmes": [
            2
        ],
        "id": 2,
        "nome": "K"
    }
]

```

O recurso de Filmes

```json
$ http -a username:password http://localhost:8000/resources/filmes/

HTTP/1.1 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Length: 193
Content-Type: application/json
Date: Tue, 18 Feb 2020 21:56:30 GMT
Server: WSGIServer/0.2 CPython/3.8.1
Vary: Accept, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

[
    {
        "ano": 2001,
        "atores": [
            1
        ],
        "id": 1,
        "nome": "G"
    },
    {
        "ano": 2002,
        "atores": [
            2
        ],
        "id": 2,
        "nome": "I"
    },
    {
        "ano": 2003,
        "atores": [
            3,
            4
        ],
        "id": 3,
        "nome": "Movie 1"
    },
    {
        "ano": 1999,
        "atores": [
            3,
            5
        ],
        "id": 4,
        "nome": "Movie 2"
    }
]

```

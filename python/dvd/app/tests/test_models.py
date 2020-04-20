import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestAtor:

    def test_model(self):

        """
        Um ator pode existir sem estar em nenhum filme
        """
        obj = mixer.blend('app.Ator')
        assert obj.pk == 1, 'Deve criar uma instancia de Ator'

        ator = mixer.blend('app.Ator', nome='João Silva')
        assert ator.nome == 'João Silva', 'Ator deve ter um nome'

class TestFilme:

    def test_model(self):
        obj = mixer.blend('app.Filme', ano=2001)
        assert obj.pk == 1, 'Filme deve existir'
        assert obj.ano == 2001, 'Filme deve ter um ano de lançamento'

    def test_filme_should_contain_actors(self):
        joao = mixer.blend('app.Ator', nome='João')
        maria = mixer.blend('app.Ator', nome='Maria')
        filme = mixer.blend('app.Filme', atores=[joao, maria], ano=1999)

        assert joao in filme.atores.all(), 'Filme deve conter João'
        assert filme in joao.filmes.all(), 'João deve estar no filme'

from django.db import models

# Retirado do IMDB
# Genero = {
#     "ACTION": 'Açao',
#     "ADVENTURE": 'Aventura',
#     "ANIMATION": 'Animação',
#     "BIOGRAPHY": 'Biografia',
#     "COMEDY": 'Comédia',
#     "CRIME": 'Crime',
#     "DOCUMENTARY": 'Documentário',
#     "DRAMA": 'Drama',
#     "FAMILY": 'Família',
#     "FANTASY": 'Fantasia',
#     "FILM_NOIR": 'Filme Noir',
#     "HISTORY": 'História',
#     "HORROR": 'Horror',
#     "MUSIC": 'Música',
#     "MUSICAL": 'Musical',
#     "MYSTERY": 'Mistério',
#     "ROMANCE": 'Romance',
#     "SCI_FI": 'Sci-fi',
#     "SHORT_FILM": 'Curta-metragem',
#     "SPORT": 'Esporte',
#     "SUPERHERO": 'Super-herói',
#     "THRILLER": 'Suspense',
#     "WAR": 'Guerra',
#     "WESTERN": 'Faroeste',
# }


class Ator(models.Model):
    nome = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nome


class Filme(models.Model):

    # class Meta:
    #     constraints = [
    #         models.CheckConstraint(check=models.Q(
    #             ano__gte=1900), name='ano_gte_1900'),
    #         models.CheckConstraint(check=models.Q(
    #             ano__lt=2100), name='ano_lt_2100'),
    #     ]
    nome = models.CharField(max_length=255, null=False)
    atores = models.ManyToManyField(
        Ator, related_name='filmes', related_query_name='filme')
    ano = models.IntegerField(null=False)

    def __str__(self):
        return '%s (%d)' % (self.nome, self.ano)

from django.db import models


class Midias(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    director = models.TextField()
    description = models.TextField()
    created_at = models.DateField()

    # email = models.EmailField()
    # telefone = models.IntegerField()
    # altura = models.DecimalField(max_digits=3, decimal_places=2)
    # descricao = models.TextField()
    # data_nascimento = models.DateField()
    # ativo = models.BooleanField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Midias'
from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User



class Midias(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
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
    #blank=True define como não obrigatorio, opcional

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Midias'
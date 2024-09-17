from django.db import models

# Create your models here.
class Companhia(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Voo(models.Model):
    origem = models.CharField(max_length=200)
    destino = models.TextField()
    data_voo = models.DateField()
    valor_passagem = models.IntegerField()
    companhia = models.ForeignKey(Companhia,on_delete=models.CASCADE)

    def __str__(self):
        return self.origem
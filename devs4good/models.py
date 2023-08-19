from django.db import models


class Cargo(models.Model):
    nome = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


class LinguagemProgramacao(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    linguagens = models.ManyToManyField(LinguagemProgramacao)

    def __str__(self):
        return self.nome


class InformacoesFuncionario(models.Model):
    funcionario = models.OneToOneField(Funcionario, on_delete=models.CASCADE)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    idade = models.IntegerField()
    frase_preferida = models.TextField()
    pokemon_preferido = models.CharField(max_length=20)

    def __str__(self):
        return f"Informações de {self.funcionario.nome}"

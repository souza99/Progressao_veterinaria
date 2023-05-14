from django.db import models

class Fazenda(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100, verbose_name='Localização')
    cpfcnpj = models.CharField(max_length=100, verbose_name='CPF/CNPJ')
    numero = models.IntegerField(verbose_name='Número')

    def __str__(self):
        return self.nome


class Animal(models.Model):
    nome = models.CharField(max_length=100)
    lote = models.CharField(max_length=100)
    nomePai = models.CharField(max_length=100)
    numeroPai = models.CharField(max_length=100)
    nomeMae = models.CharField(max_length=100)
    numeroMae = models.CharField(max_length=100)
    motivoBaixa = models.CharField(max_length=100)
    partosNaoLancados = models.IntegerField()
    dataNascimento = models.DateField()
    dataBaixa = models.DateField()
    fazenda = models.ForeignKey(Fazenda, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class QualidadeLeite(models.Model):
    nt = models.IntegerField(verbose_name='Número de Lactação')
    dias = models.IntegerField()
    estado = models.CharField(max_length=100)
    kgLeite = models.FloatField(verbose_name='Kg de Leite')
    porcentagemGordura = models.FloatField(verbose_name='Porcentagem de Gordura')
    porcentagemProteinas = models.FloatField(verbose_name='Porcentagem de Proteínas')
    lactose = models.FloatField()
    gp = models.FloatField(verbose_name='GP')
    ccs = models.FloatField(verbose_name='CCS')
    ureia = models.FloatField()
    cetose = models.FloatField()
    pps = models.FloatField(verbose_name='PPS')
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    diaRetirado = models.DateField(verbose_name='Dia Retirado')

    def __str__(self):
        return f"Qualidade do leite de {self.animal.nome}"

from django.db import models
from app1.models import *
# Create your models here.

class TesteCampos(models.Model):
    
    class Status(models.TextChoices):
        CONCLUIDO = "CONCLUIDO", "Concluido"
        PENDENTE =  "PENDENTE", "Pendente"
        CANCELADO = "CANCELADO", "Cancelado"
    
    nome = models.TextField(
        "Texto",
        blank=False,
    )
    
    decimal = models.DecimalField(
        "Decimal",
        max_digits=10,
        decimal_places=2,
        blank=False,
    )
    
    fk = models.ForeignKey(
        RickAndMorty, 
        on_delete=models.CASCADE,
        related_name="fk"    
    ) # Cascade: Deleta tudo/ # .Null = Coloca null onde ele for referenciado. E protect impede de excluir
    
    many = models.ManyToManyField(
        RickAndMorty,
        related_name="many"
    )
    
    date = models.DateField(
        "Data",
        blank=False,
    )
    
    datetime = models.DateTimeField(
        "Data e Hora",
        blank=True,
        auto_now_add=True
    )
    
    bool = models.BooleanField(
        "Booleano",
        default=False,
    )
    
    situacao = models.CharField(
        "Situação",
        max_length=20,
        choices = Status.choices,
        default = Status.PENDENTE
    )
    
    class Meta:
        verbose_name = "Teste"
        verbose_name_plural = "Teste Campos"
    
    def save(self, *args, **kwargs):
        if self.nome:
            self.nome = self.nome.capitalize()
        
        if self.decimal is not None:
            self.decimal += 2
        
        if self.situacao == self.Status.CONCLUIDO:
            self.bool = True
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.nome} - {self.situacao}"
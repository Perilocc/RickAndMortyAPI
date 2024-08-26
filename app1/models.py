from django.db import models

# Create your models here

class  RickAndMorty(models.Model):
    
    nome = models.CharField(
        "Nome do Personagem",
        max_length=100,
        blank=False,
    )
    
    genero = models.CharField(
        "Gênero do Personagem",
        max_length=10,
    )
    
    status = models.CharField(
        "Vivo ou Morto",
        blank=True,
        max_length=10,
    )
    
    especie = models.CharField(
        "Especie do Personagem",
        max_length=50,
        blank=True,        
    )
    
    origem = models.CharField(
        "Origem do Personagem",
        max_length=50,
        blank=True,   
    )
    
    localizacao = models.CharField(
        "Localizacao do Personagem",
        max_length=100,
        blank=True,   
    )
    class Meta:
        verbose_name = "Personagem"
        verbose_name_plural = "Personagens"
    
    # Data de Criação - Sugestão
    def __str__(self):
        return self.nome
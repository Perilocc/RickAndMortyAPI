from rest_framework.viewsets import ModelViewSet
from .serializers import RickAndMortySerializer, RickAndMorty
import requests
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from urllib.parse import quote

class RickAndMortyViewSet(ModelViewSet):
    
    serializer_class = RickAndMortySerializer
    queryset = RickAndMorty.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'status', 'especie', 'genero']

    def create(self, request):
        
        nome_personagem = request.data.get("nome", "")
        nome_codificado = quote(nome_personagem.lower()) # o quote codifica o nome composto dos personagens para ficar: rick%20sanchez
        
        try:
            requisicao = requests.get(f"https://rickandmortyapi.com/api/character/?name={nome_codificado}") # forçar erro do requests para request
        except requests.RequestException as e:
            return Response({"aviso": f"Erro ao acessar a API externa: {str(e)}"}, status=500)
        
        json = requisicao.json()
        print(json)
        
        if 'results' in json and len(json['results']) > 0: # Verifica se há results no Json e pega apenas o primeiro id do json, pois podem haver vários ricks/mortys
            personagem_data = json['results'][0]
        else:
            return Response({"aviso": "Personagem não encontrado no universo de Rick and Morty"}, status=404) # Validação de caso o personagem não seja encontrado
            
        print(f"personagem: {personagem_data}")
        # Coleta de Dados no Json
        nome = personagem_data.get("name", '')
        genero = personagem_data.get("gender", '')
        status = personagem_data.get("status", '')
        especie = personagem_data.get("species", '')
        origin = personagem_data.get("origin", {}).get("name", '') # Colocar os imersionistas para responder o porque de pegar assim no json
        localizacao = personagem_data.get("location", {}).get("name", '')
        
        personagem = {
            "nome": nome,
            "genero": genero,
            "status": status,
            "especie": especie,
            "origem": origin,
            "localizacao": localizacao
        }
        
        print(personagem)
        meuserializador = RickAndMortySerializer(data=personagem)
        
        if meuserializador.is_valid():
            
            personagem_validation = RickAndMorty.objects.filter(nome=nome)
            personagem_existe = personagem_validation.exists()
            
            if personagem_existe:
                return Response({"aviso": "Esse Personagem já foi Registrado na API"}, status=400)
                    
            meuserializador.save()
            
            return Response(meuserializador.data)

        else:
            return Response({"aviso": "Esse Personagem não existe ou é inválido"}, status=400)
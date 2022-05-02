import requests
from Interfaz import *

class PokeApi(Api):
    def buscar_pokemon(self, pokemon_name: str) -> Pokemon:
        payload = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}').json()
        id = payload.get('id')
        nom = payload.get('name')
        tipo = payload.get('types')
        list_moves = [i['move']['name'] for i in payload.get('moves')[:4]]
        base = payload.get('base_experience')
        
        return Pokemon(id, nom, tipo[0].get("type").get("name"), list_moves, base)
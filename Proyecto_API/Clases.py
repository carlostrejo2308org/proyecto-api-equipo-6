class Pokemon():
    def __init__(self, id:int, name:str, type:str, moves:list[str], base_experience:int ):
        self.id = id
        self.name = name
        self.type = type
        self.moves = moves
        self.base_experience = base_experience
    
    def __str__(self):
        return f'{self.id}, {self.name}, {self.type}, {self.moves}, {self.base_experience}'


class Equipo():
    def __init__(self, id_team:int, team_name:str, trainer_name:str, pokemons:list[Pokemon] = []):
        self.id_team = id_team
        self.team_name = team_name
        self.trainer_name = trainer_name
        self.pokemons = pokemons
    
    def add_pokemon(self, pokemon: Pokemon):
        self.pokemons.append(pokemon)
    
    def __str__(self):
        return f'{self.id_team}, {self.team_name}, {self.trainer_name}, {self.pokemons}'

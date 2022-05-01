import pyodbc
from Interfaz import *

class ConexionBD(Storage):
    def __init__(self):
        self.cnx = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                   'Server=localhost;'
                   'Database=PokemonDB;'
                   'Trusted_Connection=yes;')
        self.cursor = self.cnx.cursor()
    
    def guardar_pokemon(self, pokemon:Pokemon, id_team:int) -> bool:
        movimientos = ', '.join([i for i in pokemon.moves])
        sql = self.cursor.execute(f'''INSERT INTO Pokemon_id_name_type_moves_base_experience_id_team
		                                VALUES ('{pokemon.id}', '{pokemon.name}', '{pokemon.type}', '{movimientos}', '{pokemon.base_experience}', '{id_team}')''')
        self.cnx.commit()
        return True
    
    def mostrar_pokemons(self) -> list[Pokemon]:
        sql = 'SELECT id, name, type, moves, base_experience, id_team FROM Pokemon'
        self.cursor.execute(sql)
        pokemons = []
        for i in self.cursor:
            dict = {"id":i[0] ,"name": i[1], 'type':i[2], 'moves':i[3], 'base_experience':i[4], 'id_team':i[5]}
            pokemons.append(dict)
        return pokemons
    
    def eliminar_pokemon(self, id_pokemon: int) -> bool:
        slq = self.cursor.execute(f'DELETE FROM Pokemon WHERE id={id_pokemon}')
        self.cnx.commit()
        return True
    
    def guardar_equipo(self, equipo:Equipo) -> bool:
        pokemon_list = ', '.join([i.name for i in equipo.pokemons])
        sql = self.cursor.execute(f'''INSERT INTO Team
		                                VALUES ('{equipo.id_team}', '{equipo.team_name}', '{equipo.trainer_name}', '{pokemon_list}')''')
        self.cnx.commit()
        return True
    
    def mostrar_equipos(self) -> list[Equipo]:
        sql = 'SELECT id_team, team_name, trainer_name, pokemons FROM Team'
        self.cursor.execute(sql)
        equipos = []
        for i in self.cursor:
            equipo = Equipo(i[0], i[1], i[2], i[3])
            equipos.append(equipo)
        return equipos
    
    def buscar_equipo(self, id_team) -> Equipo:
        sql = f'SELECT id_team, team_name, trainer_name, pokemons FROM Team WHERE id_team = {id_team}'
        self.cursor.execute(sql)
        for i in self.cursor:
            equipo = Equipo(i[0], i[1], i[2], i[3])
        return equipo
    
    def eliminar_equipo(self, id_team: int) -> bool:
        slq = self.cursor.execute(f'DELETE FROM Team WHERE id_team={id_team}')
        self.cnx.commit()
        return True
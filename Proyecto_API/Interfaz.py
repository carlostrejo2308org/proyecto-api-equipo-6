from abc import ABC, abstractmethod
from Clases import *

class Api(ABC):
    @abstractmethod
    def buscar_pokemon(self, name_pokemon: str)-> Pokemon:
        pass

#interfaz DB
class Storage(ABC):
    @abstractmethod
    def guardar_pokemon(self, pokemon: Pokemon, id_team:int) -> bool:
        pass
    
    @abstractmethod
    def mostrar_pokemons(self) ->list[Pokemon]:
        pass
    
    @abstractmethod
    def eliminar_pokemon(self, id_pokemon: int) -> bool:
        pass
    
    @abstractmethod
    def guardar_equipo(self, equipo: Equipo) -> bool:
        pass
    
    @abstractmethod
    def mostrar_equipos(self) -> list[Equipo]:
        pass
    
    @abstractmethod
    def buscar_equipo(self, id_team: int) -> Equipo:
        pass
    
    @abstractmethod
    def eliminar_equipo(self, id_team: int) -> bool:
        pass
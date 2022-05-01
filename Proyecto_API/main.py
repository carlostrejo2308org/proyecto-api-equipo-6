from API import * 
from DB import *

def menu():
    print()
    print("1. Buscar Pokemon\n2. Mostrar Pokemons\n3. Guardar Pokemon\n4. Eliminar Pokemon")
    print("5. Buscar Equipo\n6. Mostrar Equipos\n7. Guardar Equipo\n8. Eliminar Equipo\n0. Salir.")


def opciones():
    while True:
        menu()
        try:
            entrada_usuario = int(input("\nSeleccione una opcion: "))
            if entrada_usuario in range(9):
                if entrada_usuario == 0:
                    print("\nAdios! Vuelva pronto")
                    break
                
                if entrada_usuario == 1:
                    pokemon_name = input("\nNombre del pokemon a buscar? ")
                    pokemon = PokeApi().buscar_pokemon(pokemon_name)
                    print(f'\n✪ ID-{pokemon.id}\n✪ Name-{pokemon.name}\n✪ Type-{pokemon.type}\n✪ Moves:{pokemon.moves}\n✪ Base_experience-{pokemon.base_experience}\n')
                
                if entrada_usuario == 2:
                    print()
                    pokemones = ConexionBD().mostrar_pokemons()
                    for pokemon in pokemones:
                        print(pokemon)
                
                if entrada_usuario == 3:
                    pokemon_name = input("\nNombre del pokemon? ")
                    id_team = int(input("ID del equipo? "))
                    mi_pokemon = PokeApi().buscar_pokemon(pokemon_name)
                    conexion = ConexionBD().guardar_pokemon(mi_pokemon, id_team)
                    print("\nSe ha guardado el pokemon.\n")
                
                if entrada_usuario == 4:
                    id_pokemon = int(input("\nID del pokemon que quiere eliminar? "))
                    conexion = ConexionBD().eliminar_pokemon(id_pokemon)
                    print('\nSe ha eliminado el pokemon.')
                
                if entrada_usuario == 5: 
                    id_team = int(input("\nID del equipo a buscar? "))
                    team = ConexionBD().buscar_equipo(id_team)
                    print(f'\n✪ ID-{team.id_team}\n✪ Equipo-{team.team_name}\n✪ Entrenador-{team.trainer_name}\n✪ Pokemons:[{team.pokemons}]')
                
                if entrada_usuario == 6:
                    print()
                    conexion = ConexionBD().mostrar_equipos()
                    for i in conexion:
                        print(f'✪ ID-{i.id_team} ✪ Equipo-{i.team_name} ✪ Entrenador-{i.trainer_name} ✪ Pokemons:[{i.pokemons}]')
                
                if entrada_usuario == 7:
                    id_team = int(input("\nID del Equipo? "))
                    team_name = input("Nombre del equipo? ")
                    trainer_name = input("Nombre del entrenador? ")
                    team = Equipo(id_team, team_name, trainer_name)
                    for i in range(1,7):
                        pokemon_name = input("Nombre del pokemon {}: ".format(i))
                        mi_pokemon = PokeApi().buscar_pokemon(pokemon_name)
                        team.add_pokemon(mi_pokemon)
                    conexion = ConexionBD().guardar_equipo(team)
                    print('\nse ha guardado el equipo.')
                
                if entrada_usuario == 8:
                    id_team = int(input("\nID del equipo que quiere eliminar? "))
                    conexion = ConexionBD().eliminar_equipo(id_team)
                    print('\nSe ha eliminado el equipo.')
                
            else:
                print('Error, solo se aceptan opciones del 0 al 8')
        except ValueError:
            print("Error verifique que sus entradas sean correctas!!!")

opciones()
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
                
                #Opción para salir del menú de acciones
                if entrada_usuario == 0:
                    print("\nAdios! Vuelva pronto")
                    break
                
                #Para buscar un pokemon se solicita el nombre de este y se procede a realizar la petición
                if entrada_usuario == 1:
                    pokemon_name = input("\nNombre del pokemon a buscar? ")
                    pokemon = PokeApi().buscar_pokemon(pokemon_name)
                    print(f'\n✪ ID-{pokemon.id}\n✪ Name-{pokemon.name}\n✪ Type-{pokemon.type}\n✪ Moves:{pokemon.moves}\n✪ Base_experience-{pokemon.base_experience}\n')
                
                #En esta opción se muestran los pokemons que se encuentran en la base de datos
                if entrada_usuario == 2:
                    print()
                    pokemones = ConexionBD().mostrar_pokemons()
                    for pokemon in pokemones:
                        print(pokemon)
                
                #Para guardar un pokemon se solicita el nombre del pokemon y el ID del equipo para hacer la petición a la API, una vez encontrado, se guardará en la base de datos como mi pokemon favorito
                if entrada_usuario == 3:
                    pokemon_name = input("\nNombre del pokemon? ")
                    id_team = int(input("ID del equipo? "))
                    mi_pokemon = PokeApi().buscar_pokemon(pokemon_name)
                    conexion = ConexionBD().guardar_pokemon(mi_pokemon, id_team)
                    print("\nSe ha guardado el pokemon.\n")
                
                #Para esta opción se solicita el ID del pokemon a eliminar, luego se busca dentro de la DB y se elimina
                if entrada_usuario == 4:
                    id_pokemon = int(input("\nID del pokemon que quiere eliminar? "))
                    conexion = ConexionBD().eliminar_pokemon(id_pokemon)
                    print('\nSe ha eliminado el pokemon.')
                
                #Un apartado extra es cuando se tiene un equipo de pokemons determinados, con un entrenador pokemon, para ello tenemos las mismas opciones, en el caso de la búsqueda, se solicita solo el ID del equipo para realizar la búsqueda en la DB
                if entrada_usuario == 5: 
                    id_team = int(input("\nID del equipo a buscar? "))
                    team = ConexionBD().buscar_equipo(id_team)
                    print(f'\n✪ ID-{team.id_team}\n✪ Equipo-{team.team_name}\n✪ Entrenador-{team.trainer_name}\n✪ Pokemons:[{team.pokemons}]')
                
                #Esta opción muestra todos los equipos guardados en la DB
                if entrada_usuario == 6:
                    print()
                    conexion = ConexionBD().mostrar_equipos()
                    for i in conexion:
                        print(f'✪ ID-{i.id_team} ✪ Equipo-{i.team_name} ✪ Entrenador-{i.trainer_name} ✪ Pokemons:[{i.pokemons}]')
                
                
                #En este caso, para guardar un nuevo equipo se solicitan los datos de éste y posteriormente los de cada pokemon, luego se realiza una petición a la API para traer la ficha del pokemon y asignarla al equipo, luego se guardará en la DB
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
                
                #Para eliminar un equipo se solicita el ID de éste y se elimina de la DB
                if entrada_usuario == 8:
                    id_team = int(input("\nID del equipo que quiere eliminar? "))
                    conexion = ConexionBD().eliminar_equipo(id_team)
                    print('\nSe ha eliminado el equipo.')
                
            else: #Error en la entrada a alguna opción del menú
                print('Error, solo se aceptan opciones del 0 al 8')
        except ValueError: #Error de entrada de datos
            print("Error verifique que sus entradas sean correctas!!!")

opciones()
from Pokedex import pokedex_dictionary
from Pokedex import type_advantages
import random

def pokemon_stat():

    pokedex = pokedex_dictionary.pokedex

    new_pokedex= {}

    for pokemon_names in pokedex:
        pokemon_name = pokemon_names
        base_health = pokedex[pokemon_names]["HP"]
        base_attack = pokedex[pokemon_names]["Attack"]
        base_defense = pokedex[pokemon_names]["Defense"]
        base_special_Atk = pokedex[pokemon_names]["Special_Atk"]
        base_special_Def = pokedex[pokemon_names]["Special_Def"]
        base_speed = pokedex[pokemon_names]["Speed"]
        base_move = pokedex[pokemon_names]["moves"]
        pokemon_type = pokedex[pokemon_names]["Type"]

        level = 5
        
        health = int(((2 * base_health * level)/100 ) + level + 10)  # 18 charmancher , 19 squirtle , 19 bulbasaur  
        attack = int(((2 * base_attack * level)/100 ) + 5)  # 10 charmancher , 9 squirtle , 9 bulbasaur  
        defense = int(((2 * base_defense * level)/100 ) + 5) 
        special_atk = int(((2 * base_special_Atk * level)/100 ) + 5) 
        special_def = int(((2 * base_special_Def * level)/100 ) + 5) 
        speed = int(((2 * base_speed * level)/100 ) + 5) 

        new_pokedex[pokemon_name] = {
            "pokemon_name":pokemon_name,
            "health":health,
            "attack":attack,
            "defense":defense,
            "special_atk":special_atk,
            "special_def":special_def,
            "speed":speed,
            "level":level,
            "moves":base_move,
            "type":pokemon_type
            }

    return new_pokedex


new_pokemon_stats = pokemon_stat()

def my_pokemon_move_stat(choosen,opponent_poke):

    base_atk_stat = new_pokemon_stats[choosen]["attack"]
    pokemon_move_set = pokedex_dictionary.pokedex[choosen]["moves"]

    level = 5
    increment = 0
    move_dict = {}
    move_name_dict = {}
    move_type = {}
    print()
    print(f"My Pokemon {choosen} Moves")
    for key,value in pokemon_move_set.items():
        move_type = value["type"]
        move_accuracy = value["accuracy"]

        increment = increment+1
        print(f"{increment} {key} ")

        move_dict[increment] = value["power"]
        move_name_dict[increment] = {key : value["type"]}

    user_input = float(input("choose your move: "))

    while user_input < 1 or user_input > 4 :
        print("Wrong move chosen try again")
        user_input = float(input("choose your move: "))

    moveset_selection  = move_dict[user_input]

    used_moved_by_pokemon_type = list(move_name_dict[user_input].values())[0]
    used_moved_by_pokemon = move_name_dict[user_input]
    opponant_pokemon_type = opponent_poke["type"][0]
    type_advantage_number = type_advantages.type_advantages[used_moved_by_pokemon_type][opponant_pokemon_type]

    opponent_pokemon_defense = opponent_poke["defense"]

    damage = ((((2 * level) // 5 + 2) * moveset_selection * base_atk_stat // opponent_pokemon_defense) // 50) + 2

    print()
    print(f"{choosen} used {used_moved_by_pokemon}")
    print()
    print("Damage to",opponent_poke["pokemon_name"],damage*type_advantage_number)
    print()

    return damage*type_advantage_number
        

def opponent_pokemon_move_stat(random_pokemon_selected,player_pokemon):

    level = 5
    base_atk_stat = new_pokemon_stats[random_pokemon_selected]["attack"]

    pokemon_move_set = pokedex_dictionary.pokedex[random_pokemon_selected]["moves"]

    level = 5
    increment = 0
    move_dict = {}
    opponent_pokemon_selected = {}
    selected_pokemon_move_type = {}

    print()
    print(f"Opponant pokemon {random_pokemon_selected} Moves")
    for key,value in pokemon_move_set.items():
        increment = increment+1
        print(f"{increment} {key}")

        move_dict[increment] = value["power"]
        opponent_pokemon_selected[increment] = {key : value["type"]}
        selected_pokemon_move_type[increment] = value["type"]

    pokemon_battle_decision = (random.randint(1, 4))

    moveset_selection  = move_dict[pokemon_battle_decision]

    opponent_pokemon_selected_move = opponent_pokemon_selected[pokemon_battle_decision]
    opponent_pokemon_selected_move_type = selected_pokemon_move_type[pokemon_battle_decision]
    opponent_pokemon_type = list(player_pokemon["type"])[0]

    type_advantage_number = type_advantages.type_advantages[opponent_pokemon_selected_move_type][opponent_pokemon_type] # change the variable name here opponat maens the npc pokemon and the player pokemon

    player_pokemon_defense = player_pokemon["defense"]

    damage = ((((2 * level) // 5 + 2) * moveset_selection * base_atk_stat // player_pokemon_defense) // 50) + 2

    print()
    print("Opponant Pokemon",random_pokemon_selected,"used Attack", opponent_pokemon_selected_move)
    print()
    print("Damage to",player_pokemon["pokemon_name"],damage*type_advantage_number)
    print()
    return damage*type_advantage_number



def battle(choosen):
    pokedex_list = new_pokemon_stats.keys()
    random_pokemon_selected = random.choice(list(pokedex_list))

    print()
    print("************  Pokemon battle started  **********")
    print()
    print("Your chosen pokemon is:",new_pokemon_stats[choosen]["pokemon_name"], "Health:",new_pokemon_stats[choosen]["health"])
    print()
    print("Your opponant pokemon is:",new_pokemon_stats[random_pokemon_selected]["pokemon_name"], "Health:", new_pokemon_stats[random_pokemon_selected]["health"])
    print()

    my_pokemon = new_pokemon_stats[choosen]
    opponent_poke = new_pokemon_stats[random_pokemon_selected]
    opponnat_pokemon_health = new_pokemon_stats[random_pokemon_selected]["health"]
    chosen_pokemon_health = new_pokemon_stats[choosen]["health"]

    print("press 1 to battle\npress 2 to run")
    print()
    user_input = input()


    while not user_input == "1" and not user_input == "2":
        print("try again option not available")
        print("press 1 to battle\npress 2 to run")
        user_input = input()
        if user_input == "1" or user_input == "2":
            break


    while opponnat_pokemon_health > 0:

        pokemon_battle_decision = (random.randint(0, 1))

        if user_input == "1":

            print("MY POKEMON SPEED",my_pokemon["speed"])
            print("Opponnat POKEMON SPEED",opponent_poke["speed"])

            # print("The Faster Pokemon speed is", max(my_pokemon["speed"],opponent_poke["speed"]))

            if my_pokemon["speed"] > opponent_poke["speed"]:
                print(my_pokemon["speed"])

                chosen_pokemon_moves =  my_pokemon_move_stat(choosen,opponent_poke)
                opponnat_pokemon_health = opponnat_pokemon_health - chosen_pokemon_moves
                print()
                print(f"{random_pokemon_selected} Health:{opponnat_pokemon_health}")


                if pokemon_battle_decision == 0:
                    print("wild pokemon",opponent_poke["pokemon_name"],"attacked")

                    opponent_pokemon_moves = opponent_pokemon_move_stat(random_pokemon_selected,my_pokemon)

                    chosen_pokemon_health = chosen_pokemon_health - opponent_pokemon_moves
                    print(f'{choosen} Health: {chosen_pokemon_health}')
            
                else:
                    print("wild pokemon", opponent_poke["pokemon_name"], "did not attack")

            else:
                print(opponent_poke["speed"])

                if pokemon_battle_decision == 0:
                    print("wild pokemon",opponent_poke["pokemon_name"],"attacked")

                    opponent_pokemon_moves = opponent_pokemon_move_stat(random_pokemon_selected,my_pokemon)

                    chosen_pokemon_health = chosen_pokemon_health - opponent_pokemon_moves
                    print(f'{choosen} Health: {chosen_pokemon_health}')

                    chosen_pokemon_moves =  my_pokemon_move_stat(choosen,opponent_poke)
                    opponnat_pokemon_health = opponnat_pokemon_health - chosen_pokemon_moves
                    print()
                    print(f"{random_pokemon_selected} Health:{opponnat_pokemon_health}")
            
                else:
                    print("wild pokemon", opponent_poke["pokemon_name"], "did not attack")

                    chosen_pokemon_moves =  my_pokemon_move_stat(choosen,opponent_poke)
                    opponnat_pokemon_health = opponnat_pokemon_health - chosen_pokemon_moves
                    print()
                    print(f"{random_pokemon_selected} Health:{opponnat_pokemon_health}")




            # chosen_pokemon_moves =  my_pokemon_move_stat(choosen,opponent_poke)
            # opponnat_pokemon_health = opponnat_pokemon_health - chosen_pokemon_moves
            # print()
            # print(f"{random_pokemon_selected} Health:{opponnat_pokemon_health}")


            # if pokemon_battle_decision == 0:
            #     print("wild pokemon",opponent_poke["pokemon_name"],"attacked")

            #     opponent_pokemon_moves = opponent_pokemon_move_stat(random_pokemon_selected,my_pokemon)

            #     chosen_pokemon_health = chosen_pokemon_health - opponent_pokemon_moves
            #     print(f'{choosen} Health: {chosen_pokemon_health}')
        
            # else:
            #     print("wild pokemon", opponent_poke["pokemon_name"], "did not attack")






        if opponnat_pokemon_health <= 0:
            print()
            print(" *** battle ended opponant pokemon",opponent_poke["pokemon_name"], "fainted ***")
            print()
            break

        elif chosen_pokemon_health <= 0:
            print()
            print(f' *** battle ended {choosen} fainted ***')
            print()
            break

        elif user_input == "2":
            print("you ran away")
            break


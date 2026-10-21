from Pokedex import pokedex_dictionary
from Pokedex import type_advantages
from Monsters import pokemon_data_extraction
import random

new_pokemon_stats = pokemon_data_extraction.pokemon_stat()

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


def switch_Pokemon(choosen):
    print(choosen)
    # pokedex_list = new_pokemon_stats.keys()
    # user_input = int(input())-1

    # choosen_pokemon = choosen[user_input]

    # my_pokemon = new_pokemon_stats[choosen_pokemon]
    # chosen_pokemon_health = new_pokemon_stats[choosen_pokemon]["health"]

    # print("Your chosen pokemon is:",my_pokemon["pokemon_name"], "Health:",chosen_pokemon_health)

    # return my_pokemon["pokemon_name"]




def initial_battle(choosen):
    pokedex_list = new_pokemon_stats.keys()
    random_pokemon_selected = random.choice(list(pokedex_list))
    
    opponent_poke = new_pokemon_stats[random_pokemon_selected]
    opponnat_pokemon_health = new_pokemon_stats[random_pokemon_selected]["health"]

    first_pokemon =  choosen

    #   My first pokemon from the list 
    my_pokemon = new_pokemon_stats[first_pokemon]["pokemon_name"]

    chosen_pokemon_health = new_pokemon_stats[first_pokemon]["health"]

    print()
    print("************  Pokemon battle started  **********")
    print()
    print("Your chosen pokemon is:",my_pokemon, "Health:",chosen_pokemon_health)
    print()
    print("Your opponant pokemon is:",opponent_poke["pokemon_name"], "Health:", opponnat_pokemon_health)
    print()
    print("press 1 to battle\npress 2 to run \npress 3 to switch pokemon")
    print()

    # user_input = input()

    # while not user_input == "1" and not user_input == "2" and not user_input == "3":
    #     print("try again option not available")
    #     print("press 1 to battle\npress 2 to run \npress 3 to switch pokemon")
    #     user_input = input()
    #     if user_input == "1" or user_input == "2" or user_input == "3":
    #         break

    return my_pokemon, chosen_pokemon_health, opponnat_pokemon_health


def player_battle_menu():

    user_input = input()

    while not user_input == "1" and not user_input == "2" and not user_input == "3":
        print("try again option not available")
        print("press 1 to battle\npress 2 to run \npress 3 to switch pokemon")
        user_input = input()
        if user_input == "1" or user_input == "2" or user_input == "3":
            break

    return user_input



def battle_mechanism(choosen,poke_party):

    if choosen == "1":
        print("BATTLE STARTED")

    elif choosen == "2":
        return print("Player ran away safely") 

    elif choosen == "3":
        print("Player can switch pokemon from their party",poke_party)
        user_input = int(input())-1
        switched_pokemon = switch_Pokemon(user_input)




def battle(choosen):
    #BATTLE STARTED
    initial_battle(choosen[0])

    # BATTLE MENU
    user_input = player_battle_menu()

    battle_mechanism(user_input,choosen)

    

    # battle_mechanism(choosen)

    # user_input = input()

    # while not user_input == "1" and not user_input == "2" and not user_input == "3":
    #     print("try again option not available")
    #     print("press 1 to battle\npress 2 to run \npress 3 to switch pokemon")
    #     user_input = input()
    #     if user_input == "1" or user_input == "2" or user_input == "3":
    #         break


    # battle_mechanism(choosen, user_input)

    # while opponnat_pokemon_health > 0:

    #     if user_input == "1":
    #         print("BATTLE STARTED")

    #     elif user_input == "2":
    #         print("Player ran away safely")
    #         break

    #     elif user_input == "3":
    #         print("Player can switch pokemon from their party",choosen)
    #         switched_pokemon = switch_Pokemon(choosen)


    # print(f'player switched {my_pokemon} for {switched_pokemon}')



    # while opponnat_pokemon_health > 0:

    #     pokemon_battle_decision = (random.randint(0, 1))

    #     if user_input == "1":

    #         if my_pokemon["speed"] > opponent_poke["speed"]:

    #             chosen_pokemon_moves =  my_pokemon_move_stat(first_pokemon,opponent_poke)
    #             opponnat_pokemon_health = opponnat_pokemon_health - chosen_pokemon_moves
    #             print()
    #             print(f"{random_pokemon_selected} Health:{opponnat_pokemon_health}")

    #             if pokemon_battle_decision == 0:

    #                 if opponnat_pokemon_health < 0:
    #                     print(" *** battle ended opponant pokemon",opponent_poke["pokemon_name"], "fainted ***")
    #                     break

    #                 print("wild pokemon",opponent_poke["pokemon_name"],"attacked")
                
    #                 opponent_pokemon_moves = opponent_pokemon_move_stat(random_pokemon_selected,my_pokemon)

    #                 chosen_pokemon_health = chosen_pokemon_health - opponent_pokemon_moves
    #                 print(f'{first_pokemon} Health: {chosen_pokemon_health}') # MY Pokemon health 
            
    #             else:
    #                 print("wild pokemon", opponent_poke["pokemon_name"], "did not attack")

    #         else:

    #             if pokemon_battle_decision == 0:
    #                 print("wild pokemon",opponent_poke["pokemon_name"],"attacked")

    #                 opponent_pokemon_moves = opponent_pokemon_move_stat(random_pokemon_selected,my_pokemon)

    #                 chosen_pokemon_health = chosen_pokemon_health - opponent_pokemon_moves
    #                 print(f'{first_pokemon} Health: {chosen_pokemon_health}')

    #                 if chosen_pokemon_health < 0:
    #                     print(f' *** battle ended {first_pokemon} fainted ***')
    #                     choosen.pop(0)
    #                     print("remaining Pokemon",choosen)
    #                     switch_Pokemon(choosen)
    #                     break

    #                 chosen_pokemon_moves =  my_pokemon_move_stat(first_pokemon,opponent_poke)
    #                 opponnat_pokemon_health = opponnat_pokemon_health - chosen_pokemon_moves
    #                 print()
    #                 print(f"{random_pokemon_selected} Health:{opponnat_pokemon_health}")
            
    #             else:
    #                 print("wild pokemon", opponent_poke["pokemon_name"], "did not attack")

    #                 chosen_pokemon_moves =  my_pokemon_move_stat(first_pokemon,opponent_poke)
    #                 opponnat_pokemon_health = opponnat_pokemon_health - chosen_pokemon_moves
    #                 print()
    #                 print(f"{random_pokemon_selected} Health:{opponnat_pokemon_health}")

    #         if opponnat_pokemon_health <= 0:
    #             print()
    #             print(" *** battle ended opponant pokemon",opponent_poke["pokemon_name"], "fainted ***")
    #             print()
    #             break

    #         elif chosen_pokemon_health <= 0:
    #             print()
    #             print(f' *** battle ended {first_pokemon} fainted ***')
    #             choosen.pop(0)
    #             print("remaining Pokemon",choosen)

    #             print()
    #             break

    #         elif user_input == "2":
    #             print("you ran away")
    #             break


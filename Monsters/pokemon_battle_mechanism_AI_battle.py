from Pokedex import pokedex_dictionary
from Pokedex import type_advantages
from Monsters import pokemon_data_extraction
import sys
import random
import gemini_api

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
        

def opponent_pokemon_move_stat(random_pokemon_selected,player_pokemon,ai_pokemon_moves):

    level = 5
    base_atk_stat = new_pokemon_stats[random_pokemon_selected]["attack"]

    pokemon_move_set = pokedex_dictionary.pokedex[random_pokemon_selected]["moves"]

    level = 5
    increment = 0
    move_dict = {}
    opponent_pokemon_selected = {}
    selected_pokemon_move_type = {}
    new_dict = {}

    print()
    print(f"Opponant pokemon {random_pokemon_selected} Moves")
    for key,value in pokemon_move_set.items():
        increment = increment+1
        print(f"{increment} {key}")

        move_dict[increment] = value["power"]
        opponent_pokemon_selected[increment] = {key : value["type"]}
        selected_pokemon_move_type[increment] = value["type"]
        new_dict[key] = value["power"] , value["type"] , key

    ai_selected_move = new_dict[ai_pokemon_moves]

    print("******** ai selected move ************",ai_selected_move)

    ai_selected_move_power = ai_selected_move[0]
    ai_selected_move_type = ai_selected_move[1]
    ai_selected_move_name = ai_selected_move[2]

    player_pokemon_defense = player_pokemon["defense"]

    opponent_pokemon_type = list(player_pokemon["type"])[0]

    type_advantage_number = type_advantages.type_advantages[ai_selected_move_type][opponent_pokemon_type] # change the variable name here opponat maens the npc pokemon and the player pokemon

    damage = ((((2 * level) // 5 + 2) * ai_selected_move_power * base_atk_stat // player_pokemon_defense) // 50) + 2

    print(f'{random_pokemon_selected} used move {ai_selected_move_name} ')
    print("Damage to",player_pokemon["pokemon_name"],damage*type_advantage_number)

    return damage*type_advantage_number


def party_switch(choosen):
    print("Current Pokemon Party\nchoose your new pokemon",choosen)

    user_input = int(input())-1
    new_choosen_pokemon = choosen[user_input]
    # print("New Switched out Pokemon is",new_choosen_pokemon)

    return new_choosen_pokemon

def my_current_pokemon(choosen):
    # print("CHOSEN",choosen)
    first_pokemon = choosen
    my_pokemon = new_pokemon_stats[first_pokemon]
    chosen_pokemon_health = new_pokemon_stats[first_pokemon]["health"]

    return first_pokemon, my_pokemon, chosen_pokemon_health


def battle_sequence(my_pokemon,chosen_pokemon_health,opponent_poke,opponnat_pokemon_health):
    print()
    print("************  Pokemon battle started  **********")
    print()
    print("Your chosen pokemon is:",my_pokemon["pokemon_name"], "Health:",chosen_pokemon_health)
    print()
    print("Your opponant pokemon is:",opponent_poke["pokemon_name"], "Health:", opponnat_pokemon_health)
    print()

    print("press 1 to battle\npress 2 to run \npress 3 to switch pokemon")
    print()
    user_input = input()

    while not user_input == "1" and not user_input == "2" and not user_input == "3":
        print("try again option not available")
        print("press 1 to battle\npress 2 to run \npress 3 to switch pokemon")
        user_input = input()
        if user_input == "1" or user_input == "2" or user_input == "3":
            break

    return user_input


def battle(player_party,AI_party,ai_pokemon_moves):

    type_advantage_number = type_advantages.type_advantages 

    ai_full_party = AI_party.split(",")

    pokedex_list = new_pokemon_stats.keys()

    ai_selected_pokemon = ai_full_party[0]

    ai_pokemon_health = new_pokemon_stats[ai_selected_pokemon]["health"]
    opponent_poke = new_pokemon_stats[ai_selected_pokemon]

    first_pokemon , my_pokemon, chosen_pokemon_health = my_current_pokemon(player_party[0])

    print("FIRST POKEMON",first_pokemon) 
    print("My POKEMON",) 

    user_input = battle_sequence(my_pokemon,chosen_pokemon_health,opponent_poke,ai_pokemon_health)
    
    while ai_pokemon_health > 0:

        if user_input == "1":
            print("BATTLE STARTED SPEED")

            if my_pokemon["speed"] > opponent_poke["speed"]:
                print("Player pokemon is FASTER")

                if chosen_pokemon_health < 0:
                    print(f' *** Pokemon {first_pokemon} fainted ***')

                    player_party.remove(first_pokemon)
                    print("remaining Pokemon",player_party)

                    if len(player_party) < 1:
                        print("Whole parted fainted battle ended")
                        break

                    new_choosen_pokemon = party_switch(player_party)
                    first_pokemon , my_pokemon, chosen_pokemon_health = my_current_pokemon(new_choosen_pokemon)
                    user_input = battle_sequence(my_pokemon,chosen_pokemon_health,opponent_poke,ai_pokemon_health)

                    print("FIRST POKEMON", player_party)

                chosen_pokemon_moves =  my_pokemon_move_stat(first_pokemon,opponent_poke)
                ai_pokemon_health = ai_pokemon_health - chosen_pokemon_moves
                print()
                print(f"{ai_selected_pokemon} Health:{ai_pokemon_health}")

                ai_pokemon_move = opponent_poke["moves"]

                ai_decision_after = gemini_api.gemini_api_turns(ai_selected_pokemon,ai_pokemon_health,ai_pokemon_move, my_pokemon,chosen_pokemon_health,type_advantage_number)
                opponent_pokemon_attack_damange = opponent_pokemon_move_stat(ai_selected_pokemon,my_pokemon,ai_decision_after)
                chosen_pokemon_health = chosen_pokemon_health - opponent_pokemon_attack_damange
                print(f'{first_pokemon} Health:{chosen_pokemon_health}')

            else:

                print("AI pokemon is FASTER")

                ai_pokemon_move = opponent_poke["moves"]

                ai_decision_after = gemini_api.gemini_api_turns(ai_selected_pokemon,ai_pokemon_health,ai_pokemon_move, my_pokemon,chosen_pokemon_health,type_advantage_number)
                opponent_pokemon_attack_damange = opponent_pokemon_move_stat(ai_selected_pokemon,my_pokemon,ai_decision_after)
                # opponent_pokemon_attack_damange = opponent_pokemon_move_stat(ai_selected_pokemon,my_pokemon,ai_pokemon_moves)

                chosen_pokemon_health = chosen_pokemon_health - opponent_pokemon_attack_damange
                print(f'{first_pokemon} Health:{chosen_pokemon_health}')

                if chosen_pokemon_health < 0:
                    print(f' *** Pokemon {first_pokemon} fainted ***')

                    player_party.remove(first_pokemon)
                    print("remaining Pokemon",player_party)

                    if len(player_party) < 1:
                        print("Whole parted fainted battle ended")
                        break

                    new_choosen_pokemon = party_switch(player_party)
                    first_pokemon , my_pokemon, chosen_pokemon_health = my_current_pokemon(new_choosen_pokemon)
                    user_input = battle_sequence(my_pokemon,chosen_pokemon_health,opponent_poke,ai_pokemon_health)

                    print("FIRST POKEMON", player_party)

                chosen_pokemon_moves =  my_pokemon_move_stat(first_pokemon,opponent_poke)
                ai_pokemon_health = ai_pokemon_health - chosen_pokemon_moves
                print()
                print(f"{ai_selected_pokemon} Health:{ai_pokemon_health}")

        elif user_input == "2":
            print("you ran away")
            break

        elif user_input == "3":
            new_choosen_pokemon = party_switch(player_party)
            first_pokemon , my_pokemon, chosen_pokemon_health = my_current_pokemon(new_choosen_pokemon)
            user_input = battle_sequence(my_pokemon,chosen_pokemon_health,opponent_poke,ai_pokemon_health)
 

from Pokedex import pokedex_dictionary
from Pokedex import type_advantages
from Monsters import pokemon_data_extraction

new_pokemon_stats = pokemon_data_extraction.pokemon_stat()

def opponent_pokemon_move_stat(random_pokemon_selected,player_pokemon,ai_pokemon_move):

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
    print(f"--- Opponent's turn: {random_pokemon_selected} ---")
    print("Opponent moves:")
    for key,value in pokemon_move_set.items():
        increment = increment+1
        print(f"  {increment}. {key}")

        move_dict[increment] = value["power"]
        opponent_pokemon_selected[increment] = {key : value["type"]}
        selected_pokemon_move_type[increment] = value["type"]
        new_dict[key] = value["power"] , value["type"] , key

    ai_selected_move = new_dict[ai_pokemon_move]

    # print("******** ai selected move ************",ai_selected_move)

    ai_selected_move_power = ai_selected_move[0]
    ai_selected_move_type = ai_selected_move[1]
    ai_selected_move_name = ai_selected_move[2]

    player_pokemon_defense = player_pokemon["defense"]

    opponent_pokemon_type = list(player_pokemon["type"])[0]

    type_advantage_number = type_advantages.type_advantages[ai_selected_move_type][opponent_pokemon_type] # change the variable name here opponat maens the npc pokemon and the player pokemon

    damage = ((((2 * level) // 5 + 2) * ai_selected_move_power * base_atk_stat // player_pokemon_defense) // 50) + 2

    print()
    print(f'{random_pokemon_selected} used {ai_selected_move_name}!')
    print(f"It dealt {damage*type_advantage_number} damage to {player_pokemon['pokemon_name']}.")

    return damage*type_advantage_number , ai_selected_move_name


def my_pokemon_move_stat(choosen,opponent_poke):

    base_atk_stat = new_pokemon_stats[choosen]["attack"]
    pokemon_move_set = pokedex_dictionary.pokedex[choosen]["moves"]

    level = 5
    increment = 0
    move_dict = {}
    move_name_dict = {}
    print()
    print(f"--- Your turn: {choosen} ---")
    print("Your moves:")
    for key,value in pokemon_move_set.items():

        increment = increment+1
        print(f"  {increment}. {key}")

        move_dict[increment] = value["power"]
        move_name_dict[increment] = {key : value["type"]}

    user_input = float(input("Choose your move (1-4): "))

    while user_input < 1 or user_input > 4 :
        print("Wrong move chosen, try again.")
        user_input = float(input("Choose your move (1-4): "))

    moveset_selection  = move_dict[user_input]

    used_moved_by_pokemon_type = list(move_name_dict[user_input].values())[0]
    used_moved_by_pokemon = move_name_dict[user_input]
    opponant_pokemon_type = opponent_poke["type"][0]
    type_advantage_number = type_advantages.type_advantages[used_moved_by_pokemon_type][opponant_pokemon_type]

    opponent_pokemon_defense = opponent_poke["defense"]

    damage = ((((2 * level) // 5 + 2) * moveset_selection * base_atk_stat // opponent_pokemon_defense) // 50) + 2

    print()
    print(f"{choosen} used {list(used_moved_by_pokemon.keys())[0]}!")
    print(f"It dealt {damage*type_advantage_number} damage to {opponent_poke['pokemon_name']}.")

    return damage*type_advantage_number , used_moved_by_pokemon
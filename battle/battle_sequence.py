from pokemon_battle_mechanism import pokemon_data_extraction
new_pokemon_stats = pokemon_data_extraction.pokemon_stat()


def battle_sequence(my_pokemon,chosen_pokemon_health,opponent_poke,opponnat_pokemon_health):
    print()
    print("==================================================")
    print("              POKEMON BATTLE STARTED")
    print("==================================================")
    print(f" You:      {my_pokemon['pokemon_name']}   HP: {chosen_pokemon_health}")
    print(f" Opponent: {opponent_poke['pokemon_name']}   HP: {opponnat_pokemon_health}")
    print("--------------------------------------------------")
    print(" [1] Battle    [2] Run    [3] Switch Pokemon")
    print()
    user_input = input()

    while not user_input == "1" and not user_input == "2" and not user_input == "3":
        print("Invalid option, please try again.")
        print(" [1] Battle    [2] Run    [3] Switch Pokemon")
        user_input = input()
        if user_input == "1" or user_input == "2" or user_input == "3":
            break

    return user_input

new_pokemon_stats = pokemon_data_extraction.pokemon_stat()


def my_current_pokemon(choosen):
    first_pokemon = choosen
    my_pokemon = new_pokemon_stats[first_pokemon]
    chosen_pokemon_health = new_pokemon_stats[first_pokemon]["health"]

    return first_pokemon, my_pokemon, chosen_pokemon_health
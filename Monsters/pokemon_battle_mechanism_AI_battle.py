# from Pokedex import pokedex_dictionary
from Pokedex import type_advantages
from Monsters import pokemon_data_extraction
from moves import pokemon_moves
import gemini_api

new_pokemon_stats = pokemon_data_extraction.pokemon_stat()

def party_switch(choosen):
    print()
    print("--------------------------------------------------")
    print("Your party:", choosen)
    print("Choose your next pokemon (enter its number in the party):")
    user_input = int(input())-1
    new_choosen_pokemon = choosen[user_input]

    return new_choosen_pokemon

def my_current_pokemon(choosen):
    first_pokemon = choosen
    my_pokemon = new_pokemon_stats[first_pokemon]
    chosen_pokemon_health = new_pokemon_stats[first_pokemon]["health"]

    return first_pokemon, my_pokemon, chosen_pokemon_health


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


def battle(player_party,AI_party):

    battle_commentary = {}

    type_advantage_number = type_advantages.type_advantages

    ai_full_party = AI_party.split(",")

    ai_selected_pokemon = ai_full_party[0]

    ai_pokemon_health = new_pokemon_stats[ai_selected_pokemon]["health"]
    opponent_poke = new_pokemon_stats[ai_selected_pokemon]

    first_pokemon , my_pokemon, chosen_pokemon_health = my_current_pokemon(player_party[0])

    user_input = battle_sequence(my_pokemon,chosen_pokemon_health,opponent_poke,ai_pokemon_health)

    while ai_pokemon_health > 0:

        if user_input == "1":
            if my_pokemon["speed"] > opponent_poke["speed"]:
                print()
                print("Your pokemon is faster, you move first.")

                if chosen_pokemon_health < 0:
                    print()
                    print(f'*** {first_pokemon} fainted ***')

                    player_party.remove(first_pokemon)
                    print("Remaining pokemon:",player_party)

                    if len(player_party) < 1:
                        print("All your pokemon fainted. Battle over.")
                        break

                    new_choosen_pokemon = party_switch(player_party)
                    first_pokemon , my_pokemon, chosen_pokemon_health = my_current_pokemon(new_choosen_pokemon)
                    user_input = battle_sequence(my_pokemon,chosen_pokemon_health,opponent_poke,ai_pokemon_health)

                    print(f"Go, {first_pokemon}!")

                chosen_pokemon_move_damange, used_moved_by_pokemon =  pokemon_moves.my_pokemon_move_stat(first_pokemon,opponent_poke)
                ai_pokemon_health = ai_pokemon_health - chosen_pokemon_move_damange
                print(f"{ai_selected_pokemon} HP: {ai_pokemon_health}")

                ai_pokemon_move = opponent_poke["moves"]

                ai_decision_after = gemini_api.gemini_api_turns(ai_selected_pokemon,ai_pokemon_health,ai_pokemon_move, my_pokemon,chosen_pokemon_health,type_advantage_number)

                opponent_pokemon_attack_damange , ai_selected_move_name = pokemon_moves.opponent_pokemon_move_stat(ai_selected_pokemon,my_pokemon,ai_decision_after)

                chosen_pokemon_health = chosen_pokemon_health - opponent_pokemon_attack_damange
                print(f'{first_pokemon} HP: {chosen_pokemon_health}')

                battle_commentary = {
                    "ai_selected_pokemon": ai_selected_pokemon,
                    "ai_pokemon_health": ai_pokemon_health,
                    "ai_pokemon_move": ai_selected_move_name,
                    "my_pokemon": my_pokemon,
                    "chosen_pokemon_health": chosen_pokemon_health,
                    "type_advantage_number": type_advantage_number,
                    "chosen_pokemon_moves":used_moved_by_pokemon
                    }

                ai_decision_after = gemini_api.gemini_battle_commentary(battle_commentary)
                print()
                print("Commentary:",ai_decision_after)
                print("--------------------------------------------------")

            else:
                ai_pokemon_move = opponent_poke["moves"]

                ai_decision_after = gemini_api.gemini_api_turns(ai_selected_pokemon,ai_pokemon_health,ai_pokemon_move, my_pokemon,chosen_pokemon_health,type_advantage_number)
                opponent_pokemon_attack_damange, ai_selected_move_name = pokemon_moves.opponent_pokemon_move_stat(ai_selected_pokemon,my_pokemon,ai_decision_after)

                chosen_pokemon_health = chosen_pokemon_health - opponent_pokemon_attack_damange
                print(f'{first_pokemon} HP: {chosen_pokemon_health}')

                if chosen_pokemon_health < 0:
                    print()
                    print(f'*** {first_pokemon} fainted ***')

                    player_party.remove(first_pokemon)
                    print("Remaining pokemon:",player_party)

                    if len(player_party) < 1:
                        print("All your pokemon fainted. Battle over.")
                        break

                    new_choosen_pokemon = party_switch(player_party)
                    first_pokemon , my_pokemon, chosen_pokemon_health = my_current_pokemon(new_choosen_pokemon)
                    user_input = battle_sequence(my_pokemon,chosen_pokemon_health,opponent_poke,ai_pokemon_health)

                    print(f"Go, {first_pokemon}!")

                chosen_pokemon_move_damange , used_moved_by_pokemon =  pokemon_moves.my_pokemon_move_stat(first_pokemon,opponent_poke)

                ai_pokemon_health = ai_pokemon_health - chosen_pokemon_move_damange
                print()
                print(f"{ai_selected_pokemon} HP: {ai_pokemon_health}")

                battle_commentary = {
                    "ai_selected_pokemon": ai_selected_pokemon,
                    "ai_pokemon_health": ai_pokemon_health,
                    "ai_pokemon_move": ai_selected_move_name,
                    "my_pokemon": my_pokemon,
                    "chosen_pokemon_health": chosen_pokemon_health,
                    "type_advantage_number": type_advantage_number,
                    "chosen_pokemon_moves":used_moved_by_pokemon
                    }

                ai_decision_after = gemini_api.gemini_battle_commentary(battle_commentary)
                print()
                print("Commentary:",ai_decision_after)
                print("--------------------------------------------------")

        elif user_input == "2":
            print("You ran away safely.")
            break

        elif user_input == "3":
            new_choosen_pokemon = party_switch(player_party)
            first_pokemon , my_pokemon, chosen_pokemon_health = my_current_pokemon(new_choosen_pokemon)
            user_input = battle_sequence(my_pokemon,chosen_pokemon_health,opponent_poke,ai_pokemon_health)
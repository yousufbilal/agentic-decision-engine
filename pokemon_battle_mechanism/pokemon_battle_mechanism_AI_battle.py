from Pokedex import type_advantages
from moves import pokemon_moves
from switch_party import switch_party
from battle import battle_sequence
from pokedex_data_extraction import pokemon_stat
import gemini_api

new_pokemon_stats = pokemon_stat.pokemon_stat()
type_advantage_number = type_advantages.type_advantages
battle_commentary = {}

def ai_commentary(ai_selected_pokemon, ai_pokemon_health, ai_selected_move_name, my_pokemon, chosen_pokemon_health, type_advantage_number, used_moved_by_pokemon):
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


def battle(player_party,ai_full_party):

    ai_selected_pokemon = ai_full_party[0]
    opponent_poke = new_pokemon_stats[ai_selected_pokemon]
    ai_pokemon_health = new_pokemon_stats[ai_selected_pokemon]["health"]
    first_pokemon , my_pokemon, chosen_pokemon_health = battle_sequence.my_current_pokemon(player_party[0])
    user_input = battle_sequence.battle_sequence(my_pokemon,chosen_pokemon_health,opponent_poke,ai_pokemon_health)    


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

                    new_choosen_pokemon = switch_party.party_switch(player_party)
                    first_pokemon , my_pokemon, chosen_pokemon_health = battle_sequence.my_current_pokemon(new_choosen_pokemon)
                    user_input = battle_sequence.battle_sequence(my_pokemon,chosen_pokemon_health,opponent_poke,ai_pokemon_health)

                    print(f"Go, {first_pokemon}!")

                chosen_pokemon_move_damange, used_moved_by_pokemon =  pokemon_moves.my_pokemon_move_stat(first_pokemon,opponent_poke)
                ai_pokemon_health = ai_pokemon_health - chosen_pokemon_move_damange
                print(f"{ai_selected_pokemon} HP: {ai_pokemon_health}")

                ai_pokemon_move = opponent_poke["moves"]

                ai_decision_after = gemini_api.gemini_api_turns(ai_selected_pokemon,ai_pokemon_health,ai_pokemon_move, my_pokemon,chosen_pokemon_health,type_advantage_number)

                opponent_pokemon_attack_damange , ai_selected_move_name = pokemon_moves.opponent_pokemon_move_stat(ai_selected_pokemon,my_pokemon,ai_decision_after)

                chosen_pokemon_health = chosen_pokemon_health - opponent_pokemon_attack_damange
                print(f'{first_pokemon} HP: {chosen_pokemon_health}')

                ai_commentary(ai_selected_pokemon, ai_pokemon_health, ai_selected_move_name, my_pokemon, chosen_pokemon_health, type_advantage_number, used_moved_by_pokemon)

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

                    new_choosen_pokemon = switch_party.party_switch(player_party)
                    first_pokemon , my_pokemon, chosen_pokemon_health = battle_sequence.my_current_pokemon(new_choosen_pokemon)
                    user_input = battle_sequence.battle_sequence(my_pokemon,chosen_pokemon_health,opponent_poke,ai_pokemon_health)

                    print(f"Go, {first_pokemon}!")

                chosen_pokemon_move_damange , used_moved_by_pokemon =  pokemon_moves.my_pokemon_move_stat(first_pokemon,opponent_poke)

                ai_pokemon_health = ai_pokemon_health - chosen_pokemon_move_damange
                print()
                print(f"{ai_selected_pokemon} HP: {ai_pokemon_health}")

                # The AI switch 
                if ai_pokemon_health < 0:
                    ai_full_party.remove(ai_selected_pokemon)
                    
                    if len(ai_full_party) < 1:
                        print("*** All AI pokemon Party Fainted Battle over. ****")
                        break

                    ai_new_choosen_pokemon = switch_party.ai_party_switch(ai_full_party,first_pokemon)
                    print(f"Go, {ai_new_choosen_pokemon}!")

                    opponent_poke = new_pokemon_stats[ai_new_choosen_pokemon]
                    ai_pokemon_health = new_pokemon_stats[ai_new_choosen_pokemon]["health"]

                    user_input = battle_sequence.battle_sequence(new_choosen_pokemon,chosen_pokemon_health,opponent_poke,ai_pokemon_health)

                ai_commentary(ai_selected_pokemon, ai_pokemon_health, ai_selected_move_name, my_pokemon, chosen_pokemon_health, type_advantage_number, used_moved_by_pokemon)

        elif user_input == "2":
            print("You ran away safely.")
            break

        elif user_input == "3":
            new_choosen_pokemon = switch_party.party_switch(player_party)
            first_pokemon , my_pokemon, chosen_pokemon_health = battle_sequence.my_current_pokemon(new_choosen_pokemon)
            user_input = battle_sequence.battle_sequence(my_pokemon,chosen_pokemon_health,opponent_poke,ai_pokemon_health)
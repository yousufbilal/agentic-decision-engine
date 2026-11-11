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
    ai_selected_pokemon_move = gemini_api.gemini_battle_commentary(battle_commentary)
    print()
    print("Commentary:",ai_selected_pokemon_move)
    print("--------------------------------------------------")


def battle(player_party,ai_full_party):

    ai_selected_pokemon = ai_full_party[0]
    opponent_poke = new_pokemon_stats[ai_selected_pokemon]
    ai_pokemon_health = new_pokemon_stats[ai_selected_pokemon]["health"]
    player_current_pokemon , my_pokemon, player_pokemon_health = battle_sequence.my_current_pokemon(player_party[0])
    
    user_input = battle_sequence.battle_sequence(my_pokemon,player_pokemon_health,opponent_poke,ai_pokemon_health)    

    while ai_pokemon_health > 0:

        if user_input == "1":

            print("AI attacks first")

            ai_selected_pokemon_move = gemini_api.gemini_api_turns(ai_selected_pokemon,ai_pokemon_health,opponent_poke["moves"], my_pokemon,player_pokemon_health,type_advantage_number)
            opponent_pokemon_attack_damange, ai_selected_move_name = pokemon_moves.opponent_pokemon_move_stat(ai_selected_pokemon,my_pokemon,ai_selected_pokemon_move)

            # the result of first turn showcase damange to player
            player_pokemon_health = player_pokemon_health - opponent_pokemon_attack_damange
            print(f'{player_current_pokemon} HP: {player_pokemon_health}')

            # if player pokemon faints after attack from enemy 
            if player_pokemon_health <= 0:
                print()
                print(f'*** {player_current_pokemon} fainted ***')

                player_party.remove(player_current_pokemon)
                print("Remaining pokemon:",player_party)

                # Condition when the player entire party faints 
                if len(player_party) < 1:
                    print("All your pokemon fainted. Battle over.")
                    break

                # if player has some pokemon they can switch to new 
                new_choosen_pokemon = switch_party.party_switch(player_party)
                player_current_pokemon , my_pokemon, player_pokemon_health = battle_sequence.my_current_pokemon(new_choosen_pokemon)
                user_input = battle_sequence.battle_sequence(my_pokemon,player_pokemon_health,opponent_poke,ai_pokemon_health)

                print(f"player sends out, {player_current_pokemon}!")

            # Player finally starts his turn 
            chosen_pokemon_move_damange , used_moved_by_pokemon =  pokemon_moves.my_pokemon_move_stat(player_current_pokemon,opponent_poke)
            ai_pokemon_health = ai_pokemon_health - chosen_pokemon_move_damange
            print()
            print(f"{ai_selected_pokemon} HP: {ai_pokemon_health}")

            ai_commentary(ai_selected_pokemon, ai_pokemon_health, ai_selected_move_name, my_pokemon, player_pokemon_health, type_advantage_number, used_moved_by_pokemon)

            # if ai pokemon faints after attack from player 
            if ai_pokemon_health <= 0:
                ai_full_party.remove(ai_selected_pokemon)

                # Condition when the AI entire party faints 
                if len(ai_full_party) < 1:
                    print("*** All AI pokemon Party Fainted Battle over. ****")
                    break

                # if AI has some pokemon they can switch to new 
                ai_new_choosen_pokemon = switch_party.ai_party_switch(ai_full_party,player_current_pokemon)
                opponent_poke = new_pokemon_stats[ai_new_choosen_pokemon]
                ai_pokemon_health = new_pokemon_stats[ai_new_choosen_pokemon]["health"]

                user_input = battle_sequence.battle_sequence(my_pokemon,player_pokemon_health,opponent_poke,ai_pokemon_health)
                ai_selected_pokemon = ai_new_choosen_pokemon
                # ai_commentary(ai_selected_pokemon, ai_pokemon_health, ai_selected_move_name, my_pokemon, player_pokemon_health, type_advantage_number, used_moved_by_pokemon)

        elif user_input == "2":
            print("You ran away safely.")
            break

        elif user_input == "3":
            new_choosen_pokemon = switch_party.party_switch(player_party)
            player_current_pokemon , my_pokemon, player_pokemon_health = battle_sequence.my_current_pokemon(new_choosen_pokemon)
            user_input = battle_sequence.battle_sequence(my_pokemon,player_pokemon_health,opponent_poke,ai_pokemon_health)
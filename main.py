from pokemon_battle_mechanism import pokemon_battle_mechanism
from pokemon_battle_mechanism import pokemon_battle_mechanism_AI_battle
from pokedex_data_extraction import pokemon_stat
import gemini_api

def main():
    all_pokemon = pokemon_stat.pokemon_stat()

    num = 0
    player_party = []
    available_pokemon = []
    print("==================================================")
    print("                 CHOOSE YOUR PARTY")
    print("==================================================")
    for x in all_pokemon:
        num = num +1
        available_pokemon.append(x)
        print(f"  {num}. {x}")

    print("--------------------------------------------------")
    print("Pick 3 pokemon by entering their numbers:")

    while len(player_party) < 3:

        choosen = int(input())-1

        while choosen < 0 or choosen > 9:
            print("Invalid choice, enter a number from 1 to 10.")
            choosen = int(input())-1

        pokemons = available_pokemon[choosen]

        if pokemons not in player_party:
            player_party.append(pokemons)
            print(f"Added {pokemons} to your party.")
        else:
            print("You can't add the same pokemon twice.")

        print("Your party:", player_party)

    ai_party = gemini_api.gemini_api_get_3_pokemon()

    ai_full_party = ai_party.split(",")

    print("AI PARTY: ",ai_full_party)
    print("Player PARTY:",player_party)

    pokemon_battle_mechanism_AI_battle.battle(player_party,ai_full_party)

main()
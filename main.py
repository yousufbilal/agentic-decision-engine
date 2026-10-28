from Monsters import pokemon_battle_mechanism
from Monsters import pokemon_battle_mechanism_AI_battle
from Monsters import pokemon_data_extraction
import gemini_api

def main():
    all_pokemon = pokemon_data_extraction.pokemon_stat()

    num = 0
    player_party = []
    available_pokemon = []
    for x in all_pokemon:
        num = num +1
        available_pokemon.append(x)
        print(num,x)

    print("Choose your pokemon")
    
    while len(player_party) < 3:

        choosen = int(input())-1

        if choosen < 0 or choosen > 9:
            print("wrong option try again")
            break

        pokemons = available_pokemon[choosen]
        print("Your Chosen Pokemon is",pokemons)

        if pokemons not in player_party:
            player_party.append(pokemons)
            print("Choose One More Pokemon")
        else:
            print("You cant add 2 or more pokemon of the same kind")

        print("Total Pokemon in your party are", player_party)

    # pokemon_battle_mechanism.battle(player_party)
    # pokemon_battle_mechanism_AI_battle.battle(player_party)


    # player_party = ["charmander,squirtle,bulbasaur"]
    AI_party = gemini_api.gemini_api_get_3_pokemon()
    ai_pokemon_moves=  gemini_api.gemini_api_pokemon_moves(AI_party,player_party)

    pokemon_battle_mechanism_AI_battle.battle(player_party,AI_party,ai_pokemon_moves)

main()
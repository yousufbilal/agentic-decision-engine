from Monsters import pokemon_battle_mechanism
from Monsters import pokemon_data_extraction

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

    pokemon_battle_mechanism.battle(player_party)

main()
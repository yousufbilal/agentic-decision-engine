from Pokedex import pokedex_dictionary
import random


def pokemon_stat():

    pokedex = pokedex_dictionary.pokedex

    new_pokedex= {}

    for pokemon_names in pokedex:
        pokemon_name = pokemon_names
        base_health = pokedex[pokemon_names]["HP"]
        base_attack = pokedex[pokemon_names]["Attack"]
        base_defense = pokedex[pokemon_names]["Defense"]
        base_special_Atk = pokedex[pokemon_names]["Special_Atk"]
        base_special_Def = pokedex[pokemon_names]["Special_Def"]
        base_speed = pokedex[pokemon_names]["Speed"]
        level = 5
        # Moves
        # base_tackle =  pokedex[pokemon_names]["moves"]["tackle"]
        

        health = int(((2 * base_health * level)/100 ) + level + 10)  # 18 charmancher , 19 squirtle , 19 bulbasaur  
        attack = int(((2 * base_attack * level)/100 ) + 5)  # 10 charmancher , 9 squirtle , 9 bulbasaur  
        defense = int(((2 * base_defense * level)/100 ) + 5) 
        special_atk = int(((2 * base_special_Atk * level)/100 ) + 5) 
        special_def = int(((2 * base_special_Def * level)/100 ) + 5) 
        speed = int(((2 * base_speed * level)/100 ) + 5) 

        new_pokedex[pokemon_name] = {
            "pokemon_name":pokemon_name,
            "health":health,
            "attack":attack,
            "defense":defense,
            "special_atk":special_atk,
            "special_def":special_def,
            "speed":speed,
            "level":level,
            }

    return new_pokedex


new_pokemon_stats = pokemon_stat()



def battle(choosen):

    pokemon_battle_decision = (random.randint(0, 1))
    print(pokemon_battle_decision)


    if choosen == "charmander":
        print("Your chosen pokemon is:",new_pokemon_stats["charmander"])
        print()
        print("Your opponant pokemon is: ",new_pokemon_stats["squirtle"])

        squirtle_health = new_pokemon_stats["squirtle"]["health"]
        charmander_health = new_pokemon_stats["charmander"]["health"]


        print("************  Pokemon battle started  **********")

        while squirtle_health > 0:
            print()
            print("press 1 to attack\npress 2 to run")
            user_input = input()

            if user_input == "1":
                print()
                squirtle_health = squirtle_health - new_pokemon_stats["charmander"]["attack"]
                print("*** opponant pokemon health ***",squirtle_health) 

                if pokemon_battle_decision == 0:
                    if squirtle_health <= 0:
                         print(" *** battle ended opponant pokemon fainted ***")
                         break
                    print("*** opponant pokemon attacked ***")
                    charmander_health = charmander_health - new_pokemon_stats["squirtle"]["attack"]
                    print("My pokemon health",charmander_health) 
                else:
                    print("*** wild pokemon did no attack ***")


                if squirtle_health <= 0:
                    print(" *** battle ended opponant pokemon fainted ***")
                    break
                elif charmander_health <= 0:
                    print(" *** battle ended you lost ***")
                    break

            elif user_input == "2":
                print("ran away safely")
                break












pokedex = {
    "charmander" : {
        "Type": ["fire"],
        "HP": 39,
        "Attack": 52,
        "Defense": 43,
        "Special_Atk": 60,
        "Special_Def": 50,
        "Speed": 65,
        "Pokedex entries" : "Obviously prefers hot places. When it rains, steam is said to spout from the tip of its tail.",
        "moves":{
            "tackle": 40
        }
    },

    "squirtle" : {
        "Type": ["water"],
        "HP": 44,
        "Attack": 48,
        "Defense": 65,
        "Special_Atk": 50,
        "Special_Def": 64,
        "Speed": 43,
        "Pokedex entries" : "After birth, its back swells and hardens into a shell. Powerfully sprays foam from its mouth.",
        "moves":{
            "tackle": 40
        }
    },

    "bulbasaur" : {
        "Type": ["grass", "poison"],
        "HP": 45,
        "Attack": 49,
        "Defense": 49,
        "Special_Atk": 65,
        "Special_Def": 65,
        "Speed": 45,
        "Pokedex entries" : "A strange seed was planted on its back at birth. The plant sprouts and grows with this POKéMON.",
        "moves":{
            "tackle": 40
        }
    }
}    


def pokemon_stat():

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
        base_tackle =  pokedex[pokemon_names]["moves"]["tackle"]
        

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




#     print("""
#           ▄████▄
#         █▀█████▀██
#         ███▀  ▀███
#         ███ ▄▄ ███
#          ████████
#          ▄██████▄      *
#         ██████████    /|\\
#        ████████████  ▄███
#        ████████████   ▀█▄
#        ████████████    ▀█▄
#         ████  ████▀▀▀▀▀▀██
#          ▀▀    ▀▀ 
# """)





#     print("""
#           ▄████▄
#         █▀█████▀██
#         ███▀  ▀███
#         ███ ▄▄ ███
#          ▀██████▀
#        ▄██████████▄
#       ██████████████
#       ██████████████
#      ▄██████████████▄  ▄▄
#     █████████████████████
#      ▀██████████████▀ ▀▀
#         ████  ████
#         ▀▀▀▀  ▀▀▀▀
# """)




#     print("""
#             ▄█▄
#           ▄█████▄
#         ▄█████████▄
#    ▄▄  █████████████  ▄▄
#   ███████████████████████
#   █████▀  ▀█████▀  ▀█████
#   █████ ▄▄ █████ ▄▄ █████
#   ▀█████████████████████▀
#     ▀████  ▄▄▄▄  ████▀
#    ▄██████████████████▄
#   █████▀██████████▀█████
#   ████  ████  ████  ████
#    ▀▀    ▀▀    ▀▀    ▀▀
# """)



def battle(chosen):

    if chosen == "charmander":
        print("Your chosen pokemon is:",new_pokemon_stats["charmander"])
        print()
        print("Your opponant pokemon is: ",new_pokemon_stats["squirtle"])

        print("************  Pokemon battle started  **********")

        squirtle_health = new_pokemon_stats["squirtle"]["health"]


        while squirtle_health >0:
            user_input = input()

            if user_input == "attack":
                print(squirtle_health) 
                squirtle_health = squirtle_health - new_pokemon_stats["charmander"]["attack"]
                print(squirtle_health) 

                if squirtle_health < 0:
                    print("battle ended opponant pokemon fainted")
                    break



    elif chosen == "squirtle":
        print(new_pokemon_stats["squirtle"])

    elif chosen == "bulbasaur":
        print(new_pokemon_stats["bulbasaur"])

    else:
        print("pokemon not available")




              # while pokemon_health > 0 :

        #     userinput = input()

        #     if userinput == "attack":
        #         pokemon_health = pokemon_health - pokemon_attack
        #         print(pokemon_health)
                
        #         if pokemon_health < 0:
        #             print("opponant pokemond died")

        #     elif userinput == "quit":
        #         print("battle over")
        #         break










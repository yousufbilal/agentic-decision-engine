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
        base_move = pokedex[pokemon_names]["moves"]


        level = 5
        
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
            "moves":base_move
            }

    return new_pokedex



new_pokemon_stats = pokemon_stat()

# def pokemon_move_stat(my_atk,opponent_dfn):
def my_pokemon_move_stat(choosen,opponent_poke):
    level = 5
    my_atk = new_pokemon_stats[choosen]["attack"]
    print()
    print("choose a move \n 1 tacke \n 2 ember \n 3 dragon breath \n 4 slash")
    print()
    
    pokemon_move_set = pokedex_dictionary.pokedex[choosen]["moves"]

    move_attack = 0

    user_input = float(input())

    if user_input == 1:
        move_attack = pokemon_move_set["tackle"]["power"]

    elif user_input == 2:
        move_attack = pokemon_move_set["ember"]["power"]

    elif user_input == 3:
        move_attack = pokemon_move_set["dragon_breath"]["power"]

    elif user_input == 4:
        move_attack = pokemon_move_set["slash"]["power"]

    else:
        print("move not available")

    opponent_pokemon_defense = opponent_poke["defense"]

    damage = ((((2 * level) // 5 + 2) * move_attack * my_atk // opponent_pokemon_defense) // 50) + 2

    print("Damage:",damage)

    return damage

def opponent_pokemon_move_stat(opponent_pokemon):

    level = 5
    my_atk = new_pokemon_stats["squirtle"]["attack"]
    print()
    print("choose a move \n 1 tacke \n 2 water_gun \n 3 bubble_beam breath \n 4 aqua_jet")
    print()
    pokemon_move_set = pokedex_dictionary.pokedex["squirtle"]["moves"]

    pokemon_battle_decision = (random.randint(0, 4))

    move_attack = 0

    if pokemon_battle_decision == 1:
        move_attack = pokemon_move_set["tackle"]["power"]

    elif pokemon_battle_decision == 2:
        move_attack = pokemon_move_set["water_gun"]["power"]

    elif pokemon_battle_decision == 3:
        move_attack = pokemon_move_set["bubble_beam"]["power"]

    elif pokemon_battle_decision == 4:
        move_attack = pokemon_move_set["aqua_jet"]["power"]

    else:
        print("move not available")

    opponent_pokemon_defense = opponent_pokemon["defense"]

    damage = ((((2 * level) // 5 + 2) * move_attack * my_atk // opponent_pokemon_defense) // 50) + 2

    print("Damage to charmander:",damage)

    return damage








def battle(choosen):


    print("************  Pokemon battle started  **********")
    print()

    if choosen == "charmander":
        print("Your chosen pokemon is:",new_pokemon_stats["charmander"]["pokemon_name"], "Health:",new_pokemon_stats["charmander"]["health"])
        print()
        print("Your opponant pokemon is:",new_pokemon_stats["squirtle"]["pokemon_name"], "Health:", new_pokemon_stats["squirtle"]["health"])
        print()

        my_pokemon = new_pokemon_stats["charmander"]
        opponent_poke = new_pokemon_stats["squirtle"]
        squirtle_health = new_pokemon_stats["squirtle"]["health"]
        charmander_health = new_pokemon_stats["charmander"]["health"]

        print("press 1 to battle\npress 2 to run")
        print()
        user_input = input()

        while squirtle_health > 0:

            pokemon_battle_decision = (random.randint(0, 1))

            if user_input == "1":
                chosen_pokemon_moves =  my_pokemon_move_stat(choosen,opponent_poke)
                opponent_pokemon_moves = opponent_pokemon_move_stat(my_pokemon)
                squirtle_health = squirtle_health - chosen_pokemon_moves
                print()
                print("Squirtle Health",squirtle_health)
                print()
                
                if pokemon_battle_decision == 0:
                    print("wild pokemon attacked")

                    charmander_health = charmander_health - opponent_pokemon_moves
                    print("Charmander Health", charmander_health)
                    
                else:
                    print("wild pokemon did not attack")

            if squirtle_health <= 0:
                print()
                print(" *** battle ended opponant pokemon fainted ***")
                print()

                break
            elif charmander_health <= 0:
                print()
                print(" *** battle ended you lost ***")
                print()
                break

            elif user_input == 2:
                print("you ran away")













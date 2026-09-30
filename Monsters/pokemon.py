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

def charmander():
    base_health = pokedex["charmander"]["HP"]
    base_attack = pokedex["charmander"]["Attack"]
    base_defense = pokedex["charmander"]["Defense"]
    base_special_Atk = pokedex["charmander"]["Special_Atk"]
    base_special_Def = pokedex["charmander"]["Special_Def"]
    base_speed = pokedex["charmander"]["Speed"]
    level = 5
    
    # Moves
    base_tackle =  pokedex["charmander"]["moves"]["tackle"]

    health = round(((2 * base_health * level)/100 ) + level + 10,2)
    attack = round(((2 * base_attack * level)/100 ) + 5,2) 
    defense = round(((2 * base_defense * level)/100 ) + 5,2) 
    special_atk = round(((2 * base_special_Atk * level)/100 ) + 5,2) 
    special_def = round(((2 * base_special_Def * level)/100 ) + 5,2) 
    speed = round(((2 * base_speed * level)/100 ) + 5,2) 
    # Moves
    tackle = round((((((2*level/5)+2) * base_tackle * attack)/(50 * defense))+2),0)



    print("Charmander")
    print("health: ", health)
    print("attack: ", attack)
    print("defense: ", defense)
    print("special_atk: ", special_atk)
    print("special_def: ", special_def)
    print("speed: ", speed)
    print("tackle: ", tackle)
    print()


def squirtle():
    base_health = pokedex["squirtle"]["HP"]
    base_attack = pokedex["squirtle"]["Attack"]
    base_defense = pokedex["squirtle"]["Defense"]
    base_special_Atk = pokedex["squirtle"]["Special_Atk"]
    base_special_Def = pokedex["squirtle"]["Special_Def"]
    base_speed = pokedex["squirtle"]["Speed"]
    level = 5

    # Moves
    base_tackle =  pokedex["squirtle"]["moves"]["tackle"]


    health = round(((2 * base_health * level)/100 ) + level + 10,2)
    attack = round(((2 * base_attack * level)/100 ) + 5,2) 
    defense = round(((2 * base_defense * level)/100 ) + 5,2) 
    special_atk = round(((2 * base_special_Atk * level)/100 ) + 5,2) 
    special_def = round(((2 * base_special_Def * level)/100 ) + 5,2) 
    speed = round(((2 * base_speed * level)/100 ) + 5,2) 
    # Moves
    tackle = round((((((2*level/5)+2) * base_tackle * attack)/(50 * defense))+2),0)




    print("Squirtle")
    print("health: ", health)
    print("attack: ", attack)
    print("defense: ", defense)
    print("special_atk: ", special_atk)
    print("special_def: ", special_def)
    print("speed: ", speed)
    print("tackle: ", tackle)
    print()

    return health, attack, defense, special_atk, special_def, speed, tackle



def bulbasaur():
    base_health = pokedex["bulbasaur"]["HP"]
    base_attack = pokedex["bulbasaur"]["Attack"]
    base_defense = pokedex["bulbasaur"]["Defense"]
    base_special_Atk = pokedex["bulbasaur"]["Special_Atk"]
    base_special_Def = pokedex["bulbasaur"]["Special_Def"]
    base_speed = pokedex["bulbasaur"]["Speed"]
    level = 5

    # Moves
    base_tackle =  pokedex["bulbasaur"]["moves"]["tackle"]

    health = round(((2 * base_health * level)/100 ) + level + 10,2)
    attack = round(((2 * base_attack * level)/100 ) + 5,2) 
    defense = round(((2 * base_defense * level)/100 ) + 5,2) 
    special_atk = round(((2 * base_special_Atk * level)/100 ) + 5,2) 
    special_def = round(((2 * base_special_Def * level)/100 ) + 5,2) 
    speed = round(((2 * base_speed * level)/100 ) + 5,2) 
    # Moves
    tackle = round((((((2*level/5)+2) * base_tackle * attack)/(50 * defense))+2),0)

    print("Bulbasaur")
    print("health: ", health)
    print("attack: ", attack)
    print("defense: ", defense)
    print("special_atk: ", special_atk)
    print("special_def: ", special_def)
    print("speed: ", speed)
    print("tackle: ", tackle)
    print()

    return health, attack, defense, special_atk, special_def, speed, tackle





# charmander()
# squirtle()
# bulbasaur()

def battle():
    bulbasaur_health, bulbasaur_attack, bulbasaur_defense, bulbasaur_special_atk, bulbasaur_special_def, bulbasaur_speed, bulbasaur_tackle = bulbasaur()
    squirtle_health, squirtle_attack, squirtle_defense, squirtle_special_atk, squirtle_special_def, squirtle_speed, squirtle_tackle = squirtle()

    print("bulbasaur_health health",bulbasaur_health)

    while bulbasaur_health >= 0:
        print("bulbasaur_health health",bulbasaur_health)
        print("TEST")


        

battle()



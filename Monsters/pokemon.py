pokedex = {
    "charmander" : {
        "Type": ["fire"],
        # "HP": 39,
        "HP": 100,
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

    "Squirtle" : {
        "Type": ["water"],
        # "HP": 44,
        "HP": 100,
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

    "Bulbasaur" : {
        "Type": ["grass", "poison"],
        # "HP": 45,
        "HP": 100,
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

def pokedex_func(chosen):
    if chosen == "1":
        print(pokedex["charmander"])
    elif chosen == "2":
        print(pokedex["Squirtle"])
    elif chosen == "3":
        print(pokedex["Bulbasaur"])
    
import gemini_api


def party_switch(choosen):
    print()
    print("--------------------------------------------------")
    print("Your party:", choosen)
    print("Choose your next pokemon (enter its number in the party):")
    user_input = int(input())-1
    new_choosen_pokemon = choosen[user_input]

    return new_choosen_pokemon

def ai_party_switch(ai_full_party,first_pokemon):
    print(f'The remining pokemon for AI team:{ai_full_party}')
    # print(f'The current pokemon for Player team:{first_pokemon}')
    ai_current_pokemon = gemini_api.ai_pokemon_team_switch(ai_full_party,first_pokemon)
    # print("AI NEW CHOSEN POKEMON: ",ai_current_pokemon)

    return ai_current_pokemon


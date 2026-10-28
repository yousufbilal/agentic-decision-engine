import requests
from dotenv import load_dotenv
import os
import json
from Pokedex import pokedex_dictionary
from Pokedex import type_advantages


load_dotenv()

def gemini_api_get_3_pokemon():
            
    pokdex_data = pokedex_dictionary.pokedex
    type_advantages_game = type_advantages.type_advantages

    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent"

    headers = {
        "x-goog-api-key": GEMINI_API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "contents": [
            {
                "parts": [

                    {"text": f'{pokdex_data} {type_advantages_game} reply with only the three names, nothing before or after them for the pokemon battle against the player'}
                    

                ]
            }
        ]
    }

    response = requests.post(url,headers=headers,json=body)

    data = response.json()
    llm_response = data["candidates"][0]["content"]["parts"][0]["text"]

    return llm_response


def gemini_api_pokemon_moves(ai_party,player_party):

    pokdex_data = pokedex_dictionary.pokedex
    type_advantages_game = type_advantages.type_advantages

    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent"

    headers = {
        "x-goog-api-key": GEMINI_API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "contents": [
            {
                "parts": [
                    {"text": f'''You are the opponent in a pokemon battle. Your pokemon: {ai_party}. 
                     Type advantages: {type_advantages_game}. The player team: {player_party}. 
                     Pokemon and moves data: {pokdex_data}. 
                     Choose one move for your pokemon, using only the moves listed for it in the data. 
                     Reply with only the move name in lowercase plain text, with no asterisks, 
                     no formatting, and nothing before or after it.  
                     ONLY GIVE THE MOVE FOR THE CHOSEN POKEMON FROM THE 4 MOVES'''}]
            }
        ]
    }

    response = requests.post(url,headers=headers,json=body)

    data = response.json()
    llm_response = data["candidates"][0]["content"]["parts"][0]["text"]

    return llm_response



def gemini_api_turns(ai_selected_pokemon,ai_pokemon_health,ai_pokemon_move, my_pokemon,chosen_pokemon_health,type_advantage_number):

    pokdex_data = pokedex_dictionary.pokedex
    type_advantages_game = type_advantages.type_advantages

    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent"

    headers = {
        "x-goog-api-key": GEMINI_API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "contents": [
            {
                "parts": [
                    {"text": f'''You are the opponent in a pokemon battle. It is your turn to attack.
                                Your pokemon: {ai_selected_pokemon}, health {ai_pokemon_health}.
                                Player's pokemon: {my_pokemon["pokemon_name"]}, type {my_pokemon["type"][0]}, health {chosen_pokemon_health}.
                                Your four moves, with type, power and accuracy:
                                {pokdex_data[ai_selected_pokemon]["moves"]}
                                Type chart. The first key is the attacking move type, the second key is the defending pokemon type, and the number is the damage multiplier:
                                {type_advantages_game}
                                Choose the best move for this situation. You must pick one of your four moves listed above, and nothing else.
                                Reply with only the move name in lowercase plain text, with no asterisks, no formatting, and nothing before or after it.'''}]
            }
        ]
    }

    response = requests.post(url,headers=headers,json=body)

    data = response.json()
    llm_response = data["candidates"][0]["content"]["parts"][0]["text"]

    return llm_response
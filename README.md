# Agentic Decision Engine

A terminal monster battler in Python where the opponent is an LLM. Google Gemini builds the AI's team, chooses its moves, switches its monsters, and commentates every turn, while a deterministic Python engine handles the rules: stats, damage, type effectiveness, fainting, and win or loss.

## Features

### Team building
- Roster of 10 monsters, each with a type, 6 base stats, a Pokedex entry and 4 moves
- Pick a team of 3, with input checks: out-of-range numbers are rejected and duplicates are blocked

### Stats
- Level 5 stats calculated from base stats with a scaling formula for HP, Attack, Defense, Special Attack, Special Defense and Speed

### Combat
- Turn-based battle loop with Battle, Run and Switch options
- Damage formula using level, move power, attack and defense
- Type effectiveness: a 6-type chart (fire, water, grass, normal, electric, ground) with x2, x0.5 and x1 multipliers
- HP tracking for both sides, and fainting at 0 HP
- Win or loss detection when a whole team faints

### Party management
- Switch monsters mid-battle by choice
- Forced switch when a monster faints, which removes it from the team
- The AI also switches when its monster faints

### Battle history
- Every battle result is saved to SQLite: win or loss, and the final monster on each side
- A battle intro built from past results, including the win and loss score

## How the AI is used

Gemini makes the opponent's decisions. Each prompt gives the model the game data it needs and tells it exactly what format to reply in.

| Decision | What Gemini receives | What it returns |
|---|---|---|
| Team building | The whole Pokedex and the type chart | The AI's 3 monsters |
| Move choice, each turn | Both monsters' HP and its own moves (type, power, accuracy) | One move |
| Switching | Your current monster and its remaining team | The best replacement |
| Live commentary | The turn's battle data | 2 sentences, told not to invent moves |
| Battle intro | Your saved battle history | A short summary before the fight |

## Tech

| Tech | Used for |
|---|---|
| Python 3.14 | Everything |
| Google Gemini API (REST) | Opponent decisions, commentary, battle intro |
| requests | HTTP calls to Gemini and parsing the JSON replies |
| python-dotenv and .env | Keeping the API key out of the code |
| SQLite (sqlite3) | Battle history |
| pytest | Unit tests |
| Git and GitHub | Feature branch, pull request, code review |
| Virtual environment (.venv) | Keeping project packages separate |

## Setup

1. Clone the repository and move into the folder.
2. Create and activate a virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
```

3. Install the packages:

```
pip install requests python-dotenv pytest
```

4. Create a `.env` file in the project root and add your Gemini API key (see `gemini_api.py` for the variable name it reads).

## Run the game

```
python3 main.py
```

## Run the tests

From the project root:

```
python3 -m pytest tests
```

The tests cover the stat calculation (exact values for chosen monsters, plus range checks across all of them) and the damage formula.

## Project structure

The code is split across packages: Pokedex data and the type chart, moves and damage, battle flow, party switching, the stat calculation, the Gemini API calls, and the SQLite battle history.

## What I learned

- Modelling data with nested dictionaries: the Pokedex, movesets and the type chart
- Splitting code into modules and packages
- Refactoring: breaking up a long battle function and removing duplicated code
- Separating pure logic from input and output, which is what made the damage formula testable
- Validating user input and re-asking on bad entries
- Managing game state through a loop: HP, the active monster and team lists
- Working with external APIs: building request bodies and reading nested JSON
- Prompt engineering: controlling output format and grounding the model with game data
- SQL basics: CREATE TABLE IF NOT EXISTS and parameterised queries
- Unit testing with pytest: exact values, ranges, and one test per promise
- A pull request workflow with 16 rounds of code review

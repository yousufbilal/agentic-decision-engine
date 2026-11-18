# Agentic Decision Engine: LLM Monster Battler

A turn-based monster battle game played in the terminal. You pick a team of 3, and an **AI opponent powered by Google Gemini** builds its own team, picks its moves, swaps monsters when one faints, and narrates the fight as it happens. Every battle result is saved to a local SQLite database, and the AI uses that history to introduce the next battle.

This is a learning project. I'm building it step by step to learn Python, game logic, working with APIs, databases and testing.

---

## Features

### Team selection
- Choose 3 monsters from a roster of 10 (Charmander, Squirtle, Bulbasaur, Snorlax, Mewtwo, Gengar, Dragonite, Mew, Lugia, Suicune).
- Bad input is rejected: numbers outside 1–10 are refused, and you can't pick the same monster twice.

### Stat system
- Each monster has base stats (HP, Attack, Defense, Special Attack, Special Defense, Speed) stored in the Pokédex.
- Real battle stats are calculated at **level 5** using a level-scaling formula, e.g.
  `HP = (2 × base × level / 100) + level + 10`

### Moves and damage
- Each monster has 4 moves, each with a type, power and accuracy.
- Damage uses a level / power / attack / defense formula:
  `damage = ((((2 × level) // 5 + 2) × power × attack // defense) // 50) + 2`
- The formula is its own function (`move_damage_formula`), so it can be unit tested.

### Type advantages
- A type chart (fire, water, grass, normal, electric, ground) multiplies the damage:
  **×2** super effective, **×0.5** not very effective, **×1** neutral.

### Battle loop
- Each turn you can **[1] Battle**, **[2] Run** or **[3] Switch**.
- HP is tracked for both sides, and a monster faints at 0 HP.
- When your monster faints, it's removed from your team and you choose the next one.
- The battle ends when either side's whole team has fainted, or when you run away.

### AI opponent (Google Gemini)
The opponent's decisions are made by an LLM through the Gemini REST API (`gemini_api.py`):

| What the AI does | Function |
|---|---|
| Builds its 3-monster team from the Pokédex and type chart | `gemini_api_get_3_pokemon` |
| Picks a move each turn based on HP, moves and type matchups | `gemini_api_turns` |
| Picks the best replacement when its monster faints | `ai_pokemon_team_switch` |
| Writes 2-sentence commentary after every turn | `gemini_battle_commentary` |
| Introduces each battle using your past results | `gemini_battle_background` |

### Battle history (SQLite)
- At the end of each battle, the result (`win` / `loss`) and the final monster on each side are saved to `poke_table` in `test_database.db`.
- Before a new battle, the saved history is read back and Gemini turns it into a short "previously on…" intro with the win/loss score.

### Unit tests (pytest)
- Tests in `tests/unit_test.py` check:
  - calculated stats for specific monsters (e.g. Charmander HP = 18)
  - that every monster's stats stay in a sensible range
  - the damage formula

---

## Project structure

```
agentic-decision-engine/
├── main.py                         # Entry point: team selection, then starts the battle
├── gemini_api.py                   # Every call to the Gemini API (team, moves, switching, commentary, intro)
├── sqlite3_battle_db.py            # Saves and loads battle results (SQLite)
├── Pokedex/
│   ├── pokedex_dictionary.py       # Base stats, types and moves for all 10 monsters
│   └── type_advantages.py          # Type effectiveness chart
├── pokedex_data_extraction/
│   └── pokemon_stat.py             # Turns base stats into level-5 battle stats
├── moves/
│   └── pokemon_moves.py            # Move selection (player and AI) and the damage formula
├── battle/
│   └── battle_sequence.py          # Battle menu screen and active-monster lookup
├── switch_party/
│   └── switch_party.py             # Switching monsters for the player and the AI
├── pokemon_battle_mechanism/
│   ├── pokemon_battle_mechanism_AI_battle.py   # Main battle loop against the Gemini AI (used by main.py)
│   └── pokemon_battle_mechanism.py             # Older battle against a random wild monster (not used)
└── tests/
    └── unit_test.py                # pytest unit tests
```

---

## Setup

**Requirements:** Python 3.14 and a [Google Gemini API key](https://aistudio.google.com/app/apikey).

```bash
# 1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Install the dependencies
pip install requests python-dotenv pytest

# 3. Add your API key in a .env file in the project root
echo "GEMINI_API_KEY=your_key_here" > .env
```

## Run the game

Run it from the project root so the imports work:

```bash
python main.py
```

## Run the tests

```bash
python -m pytest
```

> Use `python -m pytest` rather than plain `pytest`. The `-m` form adds the project root to Python's import path, so the tests can import the game's modules.

---

## Known issues

This is still being built. These are the known bugs being worked on:

- Choosing **Run** right after switching in a fainted monster's replacement is ignored for one turn.
- The game uses Gemini's replies (e.g. the name of the AI's next monster) without checking them, so an unexpected reply (extra spaces or a newline) can crash the game.
- Battle commentary is given the whole type chart instead of the actual multiplier for the move used.
- On a fresh install with no existing database, the battle intro crashes because the results table hasn't been created yet.
- Speed isn't used yet: the AI always attacks first.

## Roadmap

**Phase 1: Terminal combat core** *(in progress)*
- [x] Monster data, level-5 stats, moves, damage formula
- [x] Type-effectiveness chart
- [x] 3-monster teams with fainting and switching
- [x] Gemini AI opponent (team building, move choice, switching, commentary)
- [x] SQLite battle history and AI battle intro
- [x] First unit tests
- [ ] Fix the known issues above
- [ ] Speed-based turn order and damage variance
- [ ] Refactor into classes (`Pokemon`, `Trainer`)
- [ ] More test coverage (type multipliers, database, mocked Gemini calls)

**Later phases**
- [ ] Phase 2: Voice input (push-to-talk → speech-to-text)
- [ ] Phase 3: LLM arbiter (structured AI decisions, running in the background)
- [ ] Phase 4: Real-world context (live weather and time of day affect battles)
- [ ] Phase 5: Retro pixel graphics (Pyxel)
- [ ] Phase 6: Full integration (overworld → battle game loop)
- [ ] Phase 7: Content, boss fights and polish

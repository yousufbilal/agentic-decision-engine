from pokedex_data_extraction import pokemon_stat
from moves import pokemon_moves

def test_charmander_check_labels():
    pokemon_stat_data = pokemon_stat.pokemon_stat()
    assert "health" in pokemon_stat_data["charmander"]
    assert "attack" in pokemon_stat_data["charmander"]
    assert "defense" in pokemon_stat_data["charmander"]
    assert "special_atk" in pokemon_stat_data["charmander"]
    assert "special_def" in pokemon_stat_data["charmander"]
    assert "speed" in pokemon_stat_data["charmander"]

def test_bulbasaur_check_labels():
    pokemon_stat_data = pokemon_stat.pokemon_stat()
    assert "health" in pokemon_stat_data["bulbasaur"]
    assert "attack" in pokemon_stat_data["bulbasaur"]
    assert "defense" in pokemon_stat_data["bulbasaur"]
    assert "special_atk" in pokemon_stat_data["bulbasaur"]
    assert "special_def" in pokemon_stat_data["bulbasaur"]
    assert "speed" in pokemon_stat_data["bulbasaur"]

def test_mewtwo_check_labels():
    pokemon_stat_data = pokemon_stat.pokemon_stat()
    assert "health" in pokemon_stat_data["mewtwo"]
    assert "attack" in pokemon_stat_data["mewtwo"]
    assert "defense" in pokemon_stat_data["mewtwo"]
    assert "special_atk" in pokemon_stat_data["mewtwo"]
    assert "special_def" in pokemon_stat_data["mewtwo"]
    assert "speed" in pokemon_stat_data["mewtwo"]

def test_move_damage_formula_tackle():
    damage = pokemon_moves.move_damage_formula(5, 40, 10, 9)
    assert damage == 5

def test_pokemon_stat_rangechecker():
    pokemon_stat_data = pokemon_stat.pokemon_stat()

    for x in pokemon_stat_data:
        print(x)

        assert pokemon_stat_data[x]["health"] > 0
        assert pokemon_stat_data[x]["health"] < 100
        assert pokemon_stat_data[x]["attack"] > 0
        assert pokemon_stat_data[x]["attack"] < 100
        assert pokemon_stat_data[x]["defense"] > 0
        assert pokemon_stat_data[x]["defense"] < 100
        assert pokemon_stat_data[x]["special_atk"] > 0
        assert pokemon_stat_data[x]["special_atk"] < 100
        assert pokemon_stat_data[x]["special_def"] > 0
        assert pokemon_stat_data[x]["special_def"] < 100
        assert pokemon_stat_data[x]["speed"] > 0
        assert pokemon_stat_data[x]["speed"] < 100


def test_pokemon_stat_charmander():
    pokemon_stat_data = pokemon_stat.pokemon_stat()
    assert pokemon_stat_data["charmander"]["health"] == 18
    assert pokemon_stat_data["charmander"]["attack"] == 10
    assert pokemon_stat_data["charmander"]["defense"] == 9
    assert pokemon_stat_data["charmander"]["special_atk"] == 11
    assert pokemon_stat_data["charmander"]["special_def"] == 10
    assert pokemon_stat_data["charmander"]["speed"] == 11

def test_pokemon_stat_bulbasaur():
    pokemon_stat_data = pokemon_stat.pokemon_stat()
    assert pokemon_stat_data["bulbasaur"]["health"] == 19
    assert pokemon_stat_data["bulbasaur"]["attack"] == 9
    assert pokemon_stat_data["bulbasaur"]["defense"] == 9
    assert pokemon_stat_data["bulbasaur"]["special_atk"] == 11
    assert pokemon_stat_data["bulbasaur"]["special_def"] == 11
    assert pokemon_stat_data["bulbasaur"]["speed"] == 9

def test_pokemon_stat_mewtwo():
    pokemon_stat_data = pokemon_stat.pokemon_stat()
    assert pokemon_stat_data["mewtwo"]["health"] == 25
    assert pokemon_stat_data["mewtwo"]["attack"] == 16
    assert pokemon_stat_data["mewtwo"]["defense"] == 14
    assert pokemon_stat_data["mewtwo"]["special_atk"] == 20
    assert pokemon_stat_data["mewtwo"]["special_def"] == 14
    assert pokemon_stat_data["mewtwo"]["speed"] == 18
    
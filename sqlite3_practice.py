import sqlite3

connection = sqlite3.connect("test_database.db")
cursor = connection.cursor()

def make_db(battle_result_dict):
    cursor.execute("""CREATE TABLE IF NOT EXISTS poke_table(id INTEGER PRIMARY KEY, player_monster, ai_monster,result)""")

    cursor.execute(
        "INSERT INTO poke_table (player_monster, ai_monster, result) VALUES (?, ?, ?)",
        (
            battle_result_dict["player_pokemon"],
            battle_result_dict["ai_pokemon"],
            battle_result_dict["result"],
        ),
    )
    connection.commit()
    cursor.execute("""SELECT * FROM poke_table""")
    rows = cursor.fetchall()
    print(rows)

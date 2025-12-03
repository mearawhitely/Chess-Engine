import sqlite3


class Game:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def StoreGame(self):
        insert_query = "INSERT INTO game (name, score) VALUES (?, ?)"
        scores_data = sqlite3.connect('scores.db')
        cursor = scores_data.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS game(name, score)
        """)
        scores_data.commit()
        cursor.execute(insert_query, (self.name, self.score))
        scores_data.commit()
        scores_data.close()

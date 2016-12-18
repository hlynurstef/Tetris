import sqlite3


class DBConnection():
    """A class that talks to the database, currently SQLite3"""

    def __init__(self):
        """Open up the connection to the db"""
        self.conn = sqlite3.connect('highscore.db')
        self.c = self.conn.cursor()
        self.create_table()


    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS high_score(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        name varchar,
                        score int NOT NULL)''')


    def add_score(self, name, score):
        self.c.execute(''' INSERT INTO high_score(name, score)
                        VALUES(?,?)''', (name, str(score)))

    def get_top_ten(self):
        self.c.execute('''SELECT name, score
                        FROM high_score
                        ORDER BY score DESC''')
        print(self.c.fetchmany(10))

    def get_all_scores(self):
        self.c.execute('''SELECT name, score
                        FROM high_score
                        ORDER BY score DESC''')
        print(self.c.fetchall())

    def close_connection(self):
        self.conn.commit()
        self.conn.close()

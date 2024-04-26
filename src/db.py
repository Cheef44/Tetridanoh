import sqlite3

class DataBase:
    def __init__(self, password = None, username = None, email = None) -> None:
        self.password = password
        self.username = username
        self.email = email
        
    def check_db(self):
        try:
            with sqlite3.connect('user_database.db') as conn:
                cursor = conn.cursor()
                email = cursor.execute("""SELECT email FROM user""").fetchall()
                if email:
                    return True
                else:
                    return False
        except sqlite3.OperationalError:
            return False
    
    def create_db(self):
        with sqlite3.connect('user_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS user(
                user_name TEXT,
                password TEXT,
                email TEXT);
            """)
            
            if not self.check_db():
                cursor.execute("INSERT INTO user(user_name, password, email) VALUES(?, ?, ?);", (self.username, self.password, self.email))
                cursor.close()
                conn.commit()
                return True
            else:
                return False
            
    def retrieve_data(self):
        with sqlite3.connect('user_database.db') as conn:
            cursor = conn.cursor()
            name = cursor.execute("""SELECT user_name FROM user""").fetchall()
            password = cursor.execute("""SELECT password FROM user""").fetchall()
            email = cursor.execute("""SELECT email FROM user""").fetchall()
            return [name, password, email]
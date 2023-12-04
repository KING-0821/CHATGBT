import sqlite3
from datetime import datetime

db = sqlite3.connect('date.db')
sql = db.cursor()

sql.execute(f"CREATE TABLE IF NOT EXISTS Users (ID INTEGER PRIMARY KEY AUTOINCREMENT, Telegram_ID INTEGER, PhoneNumber TEXT, FirstName TEXT, RegDate datetime)")
sql.execute(f"CREATE TABLE IF NOT EXISTS User_Datol (ID INTEGER PRIMARY KEY AUTOINCREMENT, Telegram_ID INTEGER, UserQuestion TEXT, Date datetime)")


def register_user(Telegram_ID, PhoneNumber, FirstName):
    db = sqlite3.connect('date.db')
    sql = db.cursor()

    sql.execute(f"INSERT INTO Users (Telegram_ID, PhoneNumber, FirstName, RegDate) VALUES (?,?,?,?);", (Telegram_ID, PhoneNumber, FirstName, datetime.now()))

    db.commit()
    db.close()

def check_user(Telegram_ID):
    db = sqlite3.connect('date.db')
    sql = db.cursor()

    Users = sql.execute(f"SELECT Telegram_ID FROM Users WHERE Telegram_ID=?;", (Telegram_ID,)).fetchone()

    if Users:
        return True

    else:
        return False
    
def add_user_data(Telegram_ID, UserQuestion):
    db = sqlite3.connect('date.db')
    sql = db.cursor()

    sql.execute(f"INSERT INTO User_Datol (Telegram_ID, UserQuestion, Date) VALUES (?,?,?); ", (Telegram_ID, UserQuestion, datetime.now()))

    db.commit()
    db.close()

def delate_user_data(Telegram_ID):
    db = sqlite3.connect('date.db')
    sql = db.cursor()

    sql.execute(f"DELETE FROM User_Datol WHERE Telegram_ID;", (Telegram_ID,))

    db.commit()
    db.close()
import sqlite3

conn = sqlite3.connect('bd.db')
cursor = conn.cursor()

# запись, год, месяц, день, час, напр ветра, осадки, темпер-ра, влажность
cursor.execute("""CREATE TABLE IF NOT EXISTS stations(
                query№ INT PRIMARY KEY,
                stationid INT,
                year INT,
                month INT,
                day INT,
                hour INT,
                dirwind TEXT,
                precipit REAL,
                temperature REAL,
                humidity REAL);"""
               )
conn.commit()

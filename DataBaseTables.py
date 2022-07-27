import sqlite3

# Define connection and cursor
conn = sqlite3.connect('cinema.db')
cursor = conn.cursor()

# Users Table
cursor.execute(""" CREATE TABLE IF NOT EXISTS
    user(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT NOT NULL,
        password TEXT NOT NULL,
        is_active INTEGER DEFAULT 1 NOT NULL,
        create_table DATETIME DEFAULT CURRENT_TIMESTAMP,
        update_table DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")

# States Table
cursor.execute(""" CREATE TABLE IF NOT EXISTS
    state(
        state_id INTEGER PRIMARY KEY AUTOINCREMENT,
        state_code TEXT NOT NULL,
        name TEXT NOT NULL,
        is_active INTEGER DEFAULT 1 NOT NULL,
        create_table DATETIME DEFAULT CURRENT_TIMESTAMP,
        update_table DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")

# Cities Table
cursor.execute(""" CREATE TABLE IF NOT EXISTS
    city(
        city_id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_code TEXT NOT NULL,
        name TEXT NOT NULL,
        is_active INTEGER DEFAULT 1 NOT NULL,
        create_table DATETIME DEFAULT CURRENT_TIMESTAMP,
        update_table DATETIME DEFAULT CURRENT_TIMESTAMP,
        state_id INTEGER,
        FOREIGN KEY(state_id) REFERENCES state(state_id)
    )""")

# Screen Table / Tabla para las salas del cine
cursor.execute(""" CREATE TABLE IF NOT EXISTS
    screen(
        screen_id INTEGER PRIMARY KEY AUTOINCREMENT,
        screen_number INTEGER NOT NULL,
        city_id INTEGER,
        is_active INTEGER DEFAULT 1 NOT NULL,
        create_table DATETIME DEFAULT CURRENT_TIMESTAMP,
        update_table DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(city_id) REFERENCES city(city_id)
    )""")

# Table for relationship between movies and screens. So we can delete a movie from a specific city/screen
# without deleting it from another city/screen
cursor.execute(""" CREATE TABLE IF NOT EXISTS
    screen_movie(
        screen_id INTEGER,
        movie_id INTEGER,
        movie_time TIME NOT NULL,
        is_active INTEGER DEFAULT 1 NOT NULL,
        create_table DATETIME DEFAULT CURRENT_TIMESTAMP,
        update_table DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(screen_id) REFERENCES screen(screen_id),
        FOREIGN KEY(movie_id) REFERENCES movie(movie_id)
    )""")

# Movies Table
cursor.execute(""" CREATE TABLE IF NOT EXISTS
    movie(
        movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        director TEXT,
        producer TEXT,
        rating TEXT,
        length FLOAT NOT NULL,
        is_active INTEGER DEFAULT 1 NOT NULL,
        create_table DATETIME DEFAULT CURRENT_TIMESTAMP,
        update_table DATETIME DEFAULT CURRENT_TIMESTAMP,
        genero_id INTEGER,
        FOREIGN KEY(genero_id) REFERENCES genero(genero_id)
    )""")

# generos Table
cursor.execute(""" CREATE TABLE IF NOT EXISTS
    genero(
        genero_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        is_active INTEGER DEFAULT 1 NOT NULL,
        create_table DATETIME DEFAULT CURRENT_TIMESTAMP,
        update_table DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")
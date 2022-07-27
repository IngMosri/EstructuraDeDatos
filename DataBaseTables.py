import sqlite3

# Define connection and cursor
conn = sqlite3.connect('cinema.db')
cursor = conn.cursor()



# Creacion de tabla en la base de datos/ tabla estados
cursor.execute(""" CREATE TABLE IF NOT EXISTS
    state(
        state_id INTEGER PRIMARY KEY AUTOINCREMENT,
        state_code TEXT NOT NULL,
        name TEXT NOT NULL,
        is_active INTEGER DEFAULT 1 NOT NULL,
        create_table DATETIME DEFAULT CURRENT_TIMESTAMP,
        update_table DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")

# Creacion de tabla en la base de datos/ tabla cuidades 
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

# Creacion de tabla en la base de datos/ salas del cine

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

#Tabla para la relación entre películas y pantallas. Así que podemos eliminar una película de una ciudad / pantalla específica 
# sin eliminarlo de otra ciudad / pantalla

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

#Creacion de tabla en la base de datos/ tabla peliculas 
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

#Creacion de tabla en la base de datos/ tabla generos 
cursor.execute(""" CREATE TABLE IF NOT EXISTS
    genero(
        genero_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        is_active INTEGER DEFAULT 1 NOT NULL,
        create_table DATETIME DEFAULT CURRENT_TIMESTAMP,
        update_table DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")

import psycopg2
import configparser

from work_bd import get_password


# Функция создания таблиц words, users, users_words
def create_table(conn):
    cur.execute("""
        DROP TABLE IF EXISTS users_words;
        DROP TABLE IF EXISTS users;
        DROP TABLE IF EXISTS words;
        """)
    conn.commit()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS words(
        id SERIAL PRIMARY KEY,
        eng VARCHAR(40) NOT NULL UNIQUE,
        rus VARCHAR(40) NOT NULL);
         """)
    conn.commit()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        name VARCHAR(40) NOT NULL,
        surname VARCHAR(40),
        nickname VARCHAR(40) UNIQUE);
        """)
    conn.commit()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users_words(
        id_word INTEGER NOT NULL REFERENCES words(id),
        id_user INTEGER NOT NULL REFERENCES users(id),
        CONSTRAINT users_words_fk PRIMARY KEY (id_word, id_user));
         """)
    conn.commit()


# Функция добавления первоначального списка слов в таблицу words
def add_initial_words(conn, eng, rus):
            cur.execute("""
                INSERT INTO words(eng, rus) 
                VALUES(%s, %s)
                ON CONFLICT (eng) DO NOTHING
                RETURNING id, eng, rus
                """, (eng, rus))
            new_word = cur.fetchone()
            print(f'Добавлена пара слов английское-русский перевод {new_word}')
            conn.commit()


# Отдельное самостоятельное создание, наполнение первоначальным списком слов и
# удаление таблиц users_words, users, words
if __name__ == '__main__':

    with psycopg2.connect(database=get_password()[1], user="postgres", password=get_password()[0]) as conn:
        with conn.cursor() as cur:
            # Создание таблиц
            create_table(conn)

            # Добавление первоначального списка слов в таблицу words
            add_initial_words(conn, 'freedom', 'свобода')
            add_initial_words(conn, 'speed', 'скорость')
            add_initial_words(conn, 'smart', 'умный')
            add_initial_words(conn, 'technology', 'технология')
            add_initial_words(conn, 'programming', 'программирование')
            add_initial_words(conn, 'car', 'машина')
            add_initial_words(conn, 'phone', 'телефон')
            add_initial_words(conn, 'table', 'стол')
            add_initial_words(conn, 'door', 'дверь')
            add_initial_words(conn, 'house', 'дом')
    conn.close()

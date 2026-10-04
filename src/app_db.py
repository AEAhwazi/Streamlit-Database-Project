import streamlit as st
import sqlite3

DBNAME = 'MoviesData.db'

def init_db():
    conn = sqlite3.connect(DBNAME)
    conn.close()
#=================================================

def create_table():
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()

    query = '''
        CREATE TABLE IF NOT EXISTS movies
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         movie_id INTEGER
         title TEXT,
         year INTEGER,
         country TEXT,
         imdb_rating REAL)'''
    
    cursor.execute(query)
    conn.commit()
    conn.close()
#=================================================

def insert_record(movie_id, title, year, country, imdb_rating):
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()

    '''
    query = 'SELECT * FROM movie WHERE movie_id = ?'
    cursor.execute(query, (movie_id,))
    exists = cursor.fetchone()

    if exists:
            return 'EXISTS'

    else:
    '''

    quary = '''
            INSERT INTO movies(movie_id, title, year, country, imdb_rating)
            VALUES(?, ?, ?, ?, ?)'''
    
    
    cursor.execute(quary, (movie_id, title, year, country, imdb_rating))
    conn.commit()
    conn.close()
    
    return None
#=================================================

def update_record_by_id(old_movie_id, new_movie_id, title, year, country, imdb_rating):
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()

    query = '''
            UPDATE movies SET movie_id = ?, title = ?, year = ?, country = ?, imdb_rating = ?
            WHERE movie_id = ?'''
    
    cursor.execute(query, (new_movie_id, title, year, country, imdb_rating, old_movie_id))
    conn.commit()
    conn.close()

    if cursor.rowcount > 0:
         return True

    else:
         return False

#=================================================

def update_record_by_title(movie_id, old_title, new_title, year, country, imdb_rating):
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()

    query = '''
            UPDATE movies SET movie_id = ?, title = ?, year = ?, country = ?, imdb_rating = ?
            WHERE title = ?'''
    
    cursor.execute(query, (movie_id, new_title, year, country, imdb_rating, old_title))
    conn.commit()
    conn.close()

    if cursor.rowcount > 0:
         return True

    else:
         return False
#=================================================

def delete_record_by_id(movie_id):

        conn = sqlite3.connect(DBNAME)
        cursor = conn.cursor()
        query = 'DELETE FROM movies WHERE movie_id = ?'
               
        cursor.execute(query, (movie_id,))
        conn.commit()
        deleted = cursor.rowcount
        conn.close()

        if deleted > 0:
            return True
        else:
            return None
   
#=================================================

def delete_record_by_title(title):

        conn = sqlite3.connect(DBNAME)
        cursor = conn.cursor()
        query = 'DELETE FROM movies WHERE title = ?'
               
        cursor.execute(query, (title,))
        conn.commit()
        deleted = cursor.rowcount
        conn.close()

        if deleted > 0:
            return True
        else:
            return None
   
#=================================================

def select_all_record():
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()

    query = '''SELECT * FROM movies'''
    
    rows = cursor.execute(query).fetchall()
    conn.close()
    return rows
#=================================================

def select_record_by_id(id):
    query = 'SELECT * FROM movies WHERE id=?'
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    row = cursor.execute(query, (id,)).fetchone()
    conn.close()
    return row
#=================================================

def select_record_by_title(title):
    pass
#=================================================

def select_record_by_rating(rate):
    pass

#=================================================

#init_db()
#create_table()
#insert_record()
#result = delete_record_by_title('My Movie')
#print(result)
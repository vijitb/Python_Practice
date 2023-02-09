import re

import psycopg2
import sqlalchemy
import pandas as pd
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine


def request_website(url):
    # download data from website
    web_results = requests.get(url)
    soup = BeautifulSoup(web_results.text, "html.parser")
    return soup


def get_data(movies, crew, ratings):
    movie_list = []
    for index in range(0, len(movies)):
        movie = movies[index].get_text().split()
        movie_year = ''.join(movie[-1]).replace('(', '').replace(')', '')
        movie_name = ' '.join(movie[1:len(movie) - 1])
        data = {"name": movie_name,
                "year": movie_year,
                "rating": ratings[index],
                "crew": crew[index]}
        movie_list.append(data)

    return movie_list


def list_to_dataframe(movie_list):
    movies_df = pd.DataFrame(movie_list)
    pd.set_option("display.width", 200)
    pd.set_option("display.max_columns", 5)

    return movies_df


# def create_table():
#     # Connection Params
#     DB_NAME = "learn_de"
#     DB_USER = "postgres"
#     DB_PASS = "root"
#     DB_HOST = "localhost"
#     DB_PORT = "5433"
#     table_create_sql = '''
#         CREATE TABLE IF NOT EXISTS dba.imdb_movies (
#         NAME CHAR(100),
#         YEAR INT,
#         RATING DECIMAL,
#         CREW CHAR(100));
#         '''
#
#     conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
#     cursor = conn.cursor()
#     cursor.execute(table_create_sql)
#     conn.commit()
#     cursor.close()
#     conn.close()


def df_to_table(movies_df):
    # Connection Params
    conn_string = 'postgresql://postgres:root@localhost:5433/learn_de'

    db_engine = create_engine(conn_string)
    conn = db_engine.connect()
    movies_df.to_sql('imdb_movies', con=conn, if_exists='replace', index=False, schema='dba')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    str = 'http://www.imdb.com/chart/top'
    results = request_website(str)
    movies = results.select('td.titleColumn')
    crew = [item.attrs.get('title') for item in results.select('td.titleColumn a')]
    ratings = [item.attrs.get('data-value') for item in results.select('td.posterColumn span[name=ir]')]

    # GET LIST OF MOVIES AND RELATED INFORMATION
    movie_list = get_data(movies, crew, ratings)

    # CONVERT LIST TO A DATA FRAME
    movies_df = list_to_dataframe(movie_list)

    # CREATE TABLE SCHEMA
    # create_table()

    # WRITE DATAFRAME to TABLE
    df_to_table(movies_df)

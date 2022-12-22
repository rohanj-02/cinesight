# import pandas as pd
# import os

# DATA_DIR = "data/tmdb/"

# # for all files in data_dir convert to csv
# for file in os.listdir(DATA_DIR):
#     if file.endswith(".xlsx"):
#         df = pd.read_excel(DATA_DIR + file)
#         df.to_csv(DATA_DIR + file[:-5] + ".tsv", index=False, sep="\t")


import csv
import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost",
    database="iia_project"
    # user="root",
    # password="rootroot"
)

mycursor = mydb.cursor()


sql = "INSERT INTO TMDBMovie(title, original_title, release_date, runtime, is_adult, imdb_link, overview, popularity, poster_path, collection_belongs_to, revenue, budget, tagline, homepage_link) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


imdbSQL = "INSERT INTO IMDBMovie(primary_title, original_title, release_date, runtime, is_adult, imdb_link, genres) VALUES (%s, %s, %s, %s, %s, %s, %s)"


# insert imdb rows
count = 0
with open('data/imdb/titleBasics.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        if count == 0:
            count += 1
            continue
        if count >= 1000:
            break
        count += 1
        id = row[0]
        imdb_id = row[1]
        primaryTitle = row[3]
        originalTitle = row[4]
        isAdult = row[5]
        startYear = row[6]
        endYear = row[7]
        runtimeMinutes = row[8]
        genres = row[9]
        # convert start year to date type for sql
        if startYear != '\\N':
            startYear = datetime.strptime(startYear, '%Y')
        # convert runtime to int
        if runtimeMinutes != '\\N':
            runtimeMinutes = int(runtimeMinutes)
        else:
            runtimeMinutes = None

        # print(id, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres)
        vals = (primaryTitle, originalTitle, startYear, runtimeMinutes,
                isAdult, imdb_id, genres)
        mycursor.execute(imdbSQL, vals)
        mydb.commit()

count = 0
with open('data/tmdb/movie.tsv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    # for each line in the file
    for row in reader:

        if count == 0:
            count += 1
            continue
        if count >= 1000:
            break
        count += 1
        # get the movie id
        id = row[0]
        film_id = row[1]
        title = row[2]
        isAdult = row[3]
        backdrop_path = row[4]
        budget = row[5]
        homepage = row[6]
        imdb_id = row[7]
        original_language = row[8]
        original_title = row[9]
        overview = row[10]
        popularity = row[11]
        poster_path = row[12]
        release_date = row[13]
        revenue = row[14]
        runtime = row[15]
        vote_average = row[16]
        vote_count = row[17]
        status = row[18]
        tagline = row[19]
        collection_id = row[20]
        isAdult = bool(isAdult)
        if isAdult:
            isAdult = 1
        else:
            isAdult = 0
        try:
            vals = (title, original_title, release_date, runtime, isAdult, imdb_id, overview,
                    popularity, poster_path, collection_id, revenue, budget, tagline, homepage)

            mycursor.execute(sql, vals)
            mydb.commit()
        except Exception as e:
            print(e)
            print(vals)


print("Entry Complete")

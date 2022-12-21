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

mydb = mysql.connector.connect(
    host="localhost",
    # user="root",
    # password="rootroot"
)

mycursor = mydb.cursor()


sql = "INSERT INTO MOVIES(title, original_title, release_date, runtime, is_adult, imdb_link, overview, popularity, poster_path, collection_belongs_to, revenue, budget, tagline, homepage_link) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# open titleAkas.csv and titleBasics.csv
with open('titleBasics.csv', 'r') as f:
    # ,tconst,titleType,primaryTitle,originalTitle,isAdult,startYear,endYear,runtimeMinutes,genres
    # tconst = title Id
    reader = csv.reader(f, delimiter=',')
    # for each line in the file
    for row in reader:
        # get the movie id
        id = row[0]
        # get the title
        imdb_id = row[1]
        primaryTitle = row[3]
        originalTitle = row[4]
        isAdult = row[5]
        startYear = row[6]
        endYear = row[7]
        runtimeMinutes = row[8]
        genres = row[9]
        # print(id, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres)
        vals = (primaryTitle, originalTitle, startYear, runtimeMinutes,
                isAdult, imdb_id, "", "", "", "", "", "", "", "")
        mycursor.execute(sql, vals)
        mydb.commit()

print(mydb)

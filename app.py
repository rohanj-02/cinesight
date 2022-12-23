# uncomment all the lines with mydb and mycursor to connect to the database


from flask import Flask, request, render_template
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    database="iia_project",
    user="root",
    password="123456"
)

mycursor = mydb.cursor()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# route to display all the data with id as parameter
@app.route('/query/<string:queryNum>')
def query(queryNum):

    queryParams = request.args.get('queryParam')  # movie name etc.
    # get query from queryNum
   # this corresponds to the queries present in the index page
    queries = [
        {
            # dummy query
            "query": "SELECT * FROM TMDBMovie WHERE title LIKE '%{}%'".format(queryParams),
            "name": "Recommend movies by title"
        },
        {
            # dummy query
            "query": "SELECT * FROM TMDBMovie WHERE original_title LIKE '%{}%'".format(queryParams),
            "name": "Show all movies with original title"
        }
    ]
    query = queries[int(queryNum)]
    print(query)
    print(queryParams)
    print(queryNum)
    # query = "SELECT * FROM TMDBMovie WHERE title LIKE '%{}%'".format(queryParam)

    # mycursor.execute(query["query"])
    # data = mycursor.fetchall()
    # run query with params based on query number and then return data
    data = [
        ["title", "original_title", "release_date", "runtime", "is_adult", "imdb_link", "overview",
            "popularity", "poster_path", "collection_belongs_to", "revenue", "budget", "tagline", "homepage_link"],
        ["title", "original_title", "release_date", "runtime", "is_adult", "imdb_link", "overview",
            "popularity", "poster_path", "collection_belongs_to", "revenue", "budget", "tagline", "homepage_link"],
    ]  # dummy data and columns because my sql db stopped working (mac issue)
    query_columns = ["title", "original_title", "release_date", "runtime", "is_adult", "imdb_link", "overview",
                     "popularity", "poster_path", "collection_belongs_to", "revenue", "budget", "tagline", "homepage_link"]
    return render_template('query.html', data=data, columns=query_columns, query_name=query["name"])

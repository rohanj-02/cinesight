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

    queryParams = [request.args.get('genre'),'','',request.args.get('keyword'),'']  # movie name etc.
    # get query from queryNum
   # this corresponds to the queries present in the index page
    queries = [
        {
            # dummy query
            "query": "select title, release_date, runtime, overview, popularity, genres,rating,ratings from Movie where runtime<100 and (LOWER(Movie.genres)) LIKE '%{}%' ORDER BY runtime".format(queryParams[0]),
            "name": "Check Out Short Movies of your favourite genre"
        },
        {
            # dummy query
            "query": 'select title, release_date, runtime, overview, popularity, genres,rating,ratings from Movie where popularity>50 and rating>8.2 and ratings>4',
            "name": "Query: Show all movies that are very famous across all platforms"
        },
        {
            # dummy query
            "query": "select year(release_date), AVG(rating) 'IMDB Average Ratings', AVG(ratings) 'Movielens Average Ratings', AVG(popularity) from Movie group by (year(release_date))  ORDER BY year(release_date) desc",
            "name": "Query: Yearwise summary of ratings across different years"
        },
        {
            # dummy query
            "query": "SELECT title, release_date, runtime, overview, popularity, genres FROM Movie WHERE LOWER(Movie.title) LIKE '%{}%' or LOWER(Movie.overview) LIKE '%{}%' or LOWER(Movie.genres) LIKE '%{}%';".format(queryParams[3],queryParams[3],queryParams[3]),
            "name": "Query: Search movies using a keyword based filter"
        },
        {
            # dummy query
            "query": "select title, release_date, runtime, overview, popularity, genres,rating,ratings from Movie where revenue-budget<0 and rating>7; ",
            "name": "Popular Movies that made a loss in the theatres"
        }
    ]
    query = queries[int(queryNum)]
    print(query)
    print(queryParams)
    print(queryNum)
    # query = "SELECT * FROM TMDBMovie WHERE title LIKE '%{}%'".format(queryParam)

    mycursor.execute(query["query"])
    data = mycursor.fetchall()
    # run query with params based on query number and then return data
    # data = [
    #     ["title", "original_title", "release_date", "runtime", "is_adult", "imdb_link", "overview",
    #         "popularity", "poster_path", "collection_belongs_to", "revenue", "budget", "tagline", "homepage_link"],
    #     ["title", "original_title", "release_date", "runtime", "is_adult", "imdb_link", "overview",
    #         "popularity", "poster_path", "collection_belongs_to", "revenue", "budget", "tagline", "homepage_link"],
    # ]  # dummy data and columns because my sql db stopped working (mac issue)
    query_columns = [['title', 'release_date', 'runtime', 'overview', 'popularity', 'genres','rating','ratings'],['title', 'release_date', 'runtime', 'overview', 'popularity', 'genres','rating','ratings'],['year', 'IMDB Average Ratings', 'Movielens Average Ratings','popularity'],['title', 'release_date', 'runtime', 'overview', 'popularity', 'genres','rating','ratings'],['title', 'release_date', 'runtime', 'overview', 'popularity', 'genres','rating','ratings']]
    return render_template('query.html', data=data, columns=query_columns[int(queryNum)], query_name=query["name"])

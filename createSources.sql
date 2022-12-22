DROP TABLE IF EXISTS IMDBMovie;
CREATE TABLE IMDBMovie (
    id INT NOT NULL AUTO_INCREMENT,
    primary_title VARCHAR(255),
    original_title VARCHAR(255),
    release_date DATE,
    runtime INT,
    is_adult BOOLEAN,
    imdb_link TEXT,
    genres TEXT,
    PRIMARY KEY (id)
);
DROP TABLE IF EXISTS TMDBMovie;
CREATE TABLE TMDBMovie (
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(255),
    original_title VARCHAR(255),
    release_date DATE,
    runtime INT,
    is_adult BOOLEAN,
    imdb_link TEXT,
    overview TEXT,
    popularity FLOAT,
    poster_path TEXT,
    collection_belongs_to TEXT,
    revenue FLOAT,
    budget FLOAT,
    tagline TEXT,
    homepage_link TEXT,
    PRIMARY KEY (id)
);
DROP TABLE IF EXISTS IMDBPerson;
CREATE TABLE IMDBPerson(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255),
    birthday DATE,
    deathday DATE,
    primary_profession TEXT,
    known_for TEXT,
    imdb_link TEXT,
    PRIMARY KEY (id)
);
DROP TABLE IF EXISTS TMDBPerson;
CREATE TABLE TMDBPerson(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255),
    birthday DATE,
    deathday DATE,
    alias_name VARCHAR(255),
    gender TEXT,
    biography TEXT,
    profile_path TEXT,
    popularity FLOAT,
    place_of_birth VARCHAR(255),
    homepage TEXT,
    home_country VARCHAR(255),
    imdb_link TEXT,
    PRIMARY KEY (id)
);
DROP TABLE IF EXISTS MovieReview;
DROP TABLE IF EXISTS Movie_Crew;
DROP TABLE IF EXISTS Person;
DROP TABLE IF EXISTS Movie_Keywords;
DROP TABLE IF EXISTS Movie_Genre;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Movie_Language;
DROP TABLE IF EXISTS Language;
DROP TABLE IF EXISTS Movie_ProductionHouses;
DROP TABLE IF EXISTS ProductionHouses;
DROP TABLE IF EXISTS Keywords;
DROP TABLE IF EXISTS Movie;
-- CREATE TABLE Movie (
--     id INT NOT NULL AUTO_INCREMENT,
--     title VARCHAR(255),
--     original_title VARCHAR(255),
--     release_date DATE,
--     runtime INT,
--     is_adult BOOLEAN,
--     imdb_link TEXT,
--     overview TEXT,
--     popularity FLOAT,
--     poster_path TEXT,
--     collection_belongs_to TEXT,
--     revenue INT,
--     budget INT,
--     tagline TEXT,
--     homepage_link TEXT,
--     PRIMARY KEY (id)
-- );
-- CREATE TABLE Language (
--     id INT NOT NULL AUTO_INCREMENT,
--     name VARCHAR(255),
--     PRIMARY KEY (id)
-- );
-- CREATE TABLE Movie_Language (
--     movie_id INT NOT NULL,
--     language_id INT NOT NULL,
--     FOREIGN KEY (movie_id) REFERENCES Movie(id),
--     FOREIGN KEY (language_id) REFERENCES Language(id)
-- );
-- CREATE TABLE Genre (
--     id INT NOT NULL AUTO_INCREMENT,
--     name VARCHAR(255),
--     PRIMARY KEY (id)
-- );
-- CREATE TABLE Movie_Genre (
--     movie_id INT NOT NULL,
--     genre_id INT NOT NULL,
--     FOREIGN KEY (movie_id) REFERENCES Movie(id),
--     FOREIGN KEY (genre_id) REFERENCES Genre(id)
-- );
-- CREATE TABLE Keywords (
--     id INT NOT NULL AUTO_INCREMENT,
--     name VARCHAR(255),
--     PRIMARY KEY (id)
-- );
-- CREATE TABLE Movie_Keywords (
--     movie_id INT NOT NULL,
--     keyword_id INT NOT NULL,
--     FOREIGN KEY (movie_id) REFERENCES Movie(id),
--     FOREIGN KEY (keyword_id) REFERENCES Keywords(id)
-- );
-- CREATE TABLE Person (
--     id INT NOT NULL AUTO_INCREMENT,
--     name VARCHAR(255),
--     birthday DATE,
--     deathday DATE,
--     primary_profession TEXT,
--     known_for TEXT,
--     aliases TEXT,
--     gender TEXT,
--     biography TEXT,
--     profile_path TEXT,
--     popularity FLOAT,
--     place_of_birth VARCHAR(255),
--     homepage TEXT,
--     home_country VARCHAR(255),
--     imdb_link TEXT,
--     PRIMARY KEY (id)
-- );
-- CREATE TABLE Movie_Crew (
--     movie_id INT NOT NULL,
--     person_id INT NOT NULL,
--     job VARCHAR(255),
--     RANKING INT,
--     character_potrayed VARCHAR(255),
--     FOREIGN KEY (movie_id) REFERENCES Movie(id),
--     FOREIGN KEY (person_id) REFERENCES Person(id)
-- );
-- CREATE TABLE MovieReview (
--     id INT NOT NULL AUTO_INCREMENT,
--     movie_id INT NOT NULL,
--     imdb_avg_votes FLOAT,
--     imdb_num_votes INT,
--     tmdb_avg_votes FLOAT,
--     tmdb_num_votes INT,
--     rt_all_critics FLOAT,
--     rt_top_critics FLOAT,
--     rt_audience FLOAT,
--     movielens_rating FLOAT,
--     reviews TEXT,
--     FOREIGN KEY (movie_id) REFERENCES Movie(id),
--     PRIMARY KEY (id)
-- );
-- CREATE TABLE ProductionHouses (
--     id INT NOT NULL AUTO_INCREMENT,
--     name VARCHAR(255),
--     homepage TEXT,
--     description TEXT,
--     headquarter TEXT,
--     company_id INT,
--     logo_path TEXT,
--     origin_country VARCHAR(255),
--     parent_company TEXT,
--     PRIMARY KEY (id)
-- );
-- CREATE TABLE Movie_ProductionHouses (
--     movie_id INT NOT NULL,
--     production_house_id INT NOT NULL,
--     movie_countries TEXT,    
--     movie_locations TEXT,
--     FOREIGN KEY (movie_id) REFERENCES Movie(id),
--     FOREIGN KEY (production_house_id) REFERENCES ProductionHouses(id)
-- );
use iia_project;
DROP VIEW IF EXISTS Movie;
DROP TABLE IF EXISTS Person;
CREATE VIEW Movie AS (
    Select t.id, t.title, t.original_title, t.release_date, t.runtime, t.is_adult, t.imdb_link, t.overview, t.popularity,t.poster_path, t.collection_belongs_to, t.revenue, t.budget, t.tagline, t.homepage_link, i.genres
    from TMDBMovie t,
        IMDBMovie i
    where t.imdb_link = i.imdb_link
);
CREATE VIEW Person AS (
    Select t.id, t.name, t.birthday, t.deathday, t.alias_name, t.gender, t.biography, t.profile_path, t.popularity, t.place_of_birth, t.homepage, t.home_country, t.imdb_link,i.primary_profession, i.known_for
    from TMDBPerson t,
        IMDBPerson i
    where t.imdb_link = i.imdb_link
);
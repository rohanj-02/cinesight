use iia_project;
DROP VIEW IF EXISTS Movie;
CREATE VIEW Movie AS (
    Select *
    from TMDBMovie
);
DROP TABLE IF EXISTS Person;
CREATE VIEW Person AS (
    Select *,
        i.primary_profession,
        i.known_for
    from TMDBPerson,
        IMDBPerson i
    where TMDBPerson.imdb_link = i.imdb_link
);
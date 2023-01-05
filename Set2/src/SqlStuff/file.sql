-- #####################################################################################################################
-- #####################################################################################################################
-- Example DataSets
DROP TABLE IF EXISTS actors;
CREATE TABLE actors (Id INT, name VARCHAR(50));
DROP TABLE IF EXISTS actors_movies;
CREATE TABLE actors_movies (actor_id INT, movie_id INT);
DROP TABLE IF EXISTS movies;
CREATE TABLE movies (id INT, name VARCHAR(50));

INSERT INTO actors VALUES(1, 'Aaaa');
INSERT INTO actors VALUES(2, 'Bbbb');
INSERT INTO actors VALUES(3, 'Cccc');

INSERT INTO actors_movies VALUES(1, 1);
INSERT INTO actors_movies VALUES(2, 1);
INSERT INTO actors_movies VALUES(3, 1);
INSERT INTO actors_movies VALUES(1, 2);
INSERT INTO actors_movies VALUES(3, 2);
INSERT INTO actors_movies VALUES(1, 3);
INSERT INTO actors_movies VALUES(2, 3);
INSERT INTO actors_movies VALUES(1, 4);
INSERT INTO actors_movies VALUES(3, 5);

INSERT INTO movies VALUES(1, 'Film1ABC');
INSERT INTO movies VALUES(2, 'Film2AC');
INSERT INTO movies VALUES(3, 'Film3AB');
INSERT INTO movies VALUES(4, 'Film4A');
INSERT INTO movies VALUES(5, 'Film5C');

SELECT * FROM movies;
SELECT * FROM actors_movies;
SELECT * FROM actors;
-- #####################################################################################################################
-- #####################################################################################################################

-- Required queries
-- 1.
SELECT actors.name FROM actors WHERE actors.name = 'Cccc';
-- 2.
-- https://learn.microsoft.com/en-us/sql/t-sql/functions/count-transact-sql?view=sql-server-ver16
SELECT actors_movies.actor_id AS actor_id, COUNT(*) AS films
FROM actors_movies GROUP BY actor_id ORDER BY actor_id ASC;


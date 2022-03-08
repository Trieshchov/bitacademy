SELECT * FROM series WHERE  has_won_awards > 0;
SELECT * FROM series WHERE rating > 2.5;
SELECT * FROM series WHERE country ENUM = 'NL' AND language ENUM = 'NL';
SELECT * FROM series WHERE seasons < 5;

SELECT MAX(rating) FROM series;

SELECT * FROM series WHERE seasons < 3 OR > 20;
SELECT * FROM series WHERE title LIKE '%Th%';
SELECT * FROM series WHERE seasons <> 3;


SELECT * FROM series WHERE rating > 2.5 ORDER BY rating;
SELECT * FROM series WHERE seasons < 5 ORDER BY seasons DESC;
SELECT * FROM series WHERE seasons < 3 OR > 20 ORDER BY country, seasons;
-- lists all genres and shows linked to them
SELECT name AS genre, COUNT(name) AS number_of_shows
  FROM tv_genres JOIN tv_show_genres
    ON id = genre_id
 GROUP BY name
 ORDER BY number_of_shows DESC;


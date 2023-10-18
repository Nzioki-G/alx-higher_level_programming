-- lists all comedy show in the db
SELECT title FROM tv_shows
  JOIN tv_show_genres
    ON tv_shows.id = show_id
  JOIN tv_genres
    ON tv_genres.id = genre_id
 WHERE name = 'Comedy'
 ORDER BY title;


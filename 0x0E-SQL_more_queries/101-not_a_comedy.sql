-- get all non-comedy shows with subquery
SELECT title FROM tv_shows
 WHERE title NOT IN(
       SELECT title FROM tv_shows 
         LEFT JOIN tv_show_genres
           ON tv_shows.id = show_id
         LEFT JOIN tv_genres
           ON tv_genres.id = genre_id
        WHERE name = 'Comedy'
 )
 ORDER BY title;


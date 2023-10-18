-- lists all genres in the db by their rating
SELECT name, SUM(rate) AS rating
  FROM tv_genres AS g JOIN tv_show_genres AS s_g
    ON g.id = s_g.genre_id
  JOIN tv_show_ratings AS r
    ON r.show_id = s_g.show_id
  GROUP BY name
  ORDER BY rating DESC;


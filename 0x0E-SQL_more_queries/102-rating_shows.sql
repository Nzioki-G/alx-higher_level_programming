-- get sum of ratings per show
SELECT title, SUM(rate) AS rate
  FROM tv_shows
  JOIN tv_show_ratings
    ON id = show_id
 GROUP BY title
 ORDER BY rate DESC;


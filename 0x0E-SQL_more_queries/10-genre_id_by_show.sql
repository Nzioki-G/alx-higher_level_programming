-- lists all shows
SELECT sh.title, gen.genre_id
  FROM tv_shows AS sh JOIN tv_show_genres AS gen
    ON sh.id = gen.show_id
 ORDER BY sh.title, gen.genre_id;


-- lists the cities of California in the db
SELECT id, name
  FROM cities
  WHERE id = (
       SELECT state_id FROM states
        WHERE name = 'California')
  ORDER BY id ASC;


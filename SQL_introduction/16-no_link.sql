-- lists all records of the table second_table of the DB.
-- it doesnt list rows where the name column does not contain a value.
-- results displays the score and the name
-- records lists by descending score.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;

-- second_table in the database 
CREATE TABLE IF NOT EXISTS second_table(
	id BIGINT NOT NULL  PRIMARY KEY
	name VARCHAR(256)
	score NOT NULL  BIGINT
);
INSERT INTO second_table( id, name, score)
VALUES (1, "JOHN", 10), (2, "ALEX", 3), (3, 'Bob', 14),  (4, 'George', 8);


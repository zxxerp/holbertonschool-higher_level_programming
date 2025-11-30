-- Create the table 'second_table' if it does not exist
CREATE TABLE IF NOT EXISTS second_table (
    id BIGINT NOT NULL PRIMARY KEY,
    name VARCHAR(256),
    score BIGINT NOT NULL
);

INSERT INTO second_table (id, name, score)
VALUES 
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);

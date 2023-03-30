-- Lists all records with best score in the table second_table in MySQL server
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;

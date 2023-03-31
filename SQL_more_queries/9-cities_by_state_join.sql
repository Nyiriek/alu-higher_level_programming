-- Lists all the cities contained in the database
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.sate_id IN states.id;

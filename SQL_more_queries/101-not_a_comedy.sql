-- Lists all shows with the genre comedy in the database
SELECT title from tv_shows LEFT JOIN comedy_shows ON comedy_shows.title = tv_shows.title WHERE comedy_shows.title IS NULL ORDER BY title;

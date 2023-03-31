-- Lists all shows with the genre comedy in the database
SELECT title FROM tv_shows LEFT JOIN (SELECT title FROM tv_shows JOIN tv_show_genres ON tv_genres.id = tv_shows.id JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id WHERE tv_genres.name = "Comedy" ORDER BY tv_shows.id) comedy_shows ON comedy_shows.title = tv_shows.title WHERE comedy_shows.title IS NULL ORDER BY title;

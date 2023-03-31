-- Lists all shows and genres in the database in the MySQL server
SELECT title, name FROM tv_shows LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id ORDER BY title, name;

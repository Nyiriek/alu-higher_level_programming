-- Lists all comedy shows contained in the database hbtn_0d_tvshows on the MySQL server
SELECT title FROM tv_shows JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id WHERE tv_genres.name = "Comedy" ORDER BY title;

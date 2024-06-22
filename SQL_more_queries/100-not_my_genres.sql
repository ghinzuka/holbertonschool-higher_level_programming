-- Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- select the name from tv_genre where the id is NOT 
-- in the sub query : select genre_id from the tv_show_genre table join with tv showe where
-- id is the same as the id of dexter 
SELECT name
FROM tv_genres
WHERE id NOT IN (
    SELECT genre_id
    FROM tv_show_genres
    INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY name ASC;

use movies;
show tables;

select count(*) from movie;
select movie_id, title from movie where title like '%Inception' order by movie_id asc;
select count(*) from movie_genre;
select * from movie_genre order by movie_id desc;

select count(*) from movie_language;
select * from movie_language order by movie_id desc;


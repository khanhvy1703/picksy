SELECT table_schema AS "Database",
       ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS "Size (MB)"
FROM information_schema.tables
GROUP BY table_schema;

use movie_tvshow;
show tables;

select * from companies;
select * from countries;
select * from genres;
select * from languages;
select * from title;



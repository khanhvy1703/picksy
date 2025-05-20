use genres;

create table genre (
  genre_id int primary key,
  name varchar(1000) not null
);

# -------------------- INSERT GENRES --------------------------------
Insert into genre (genre_id, name) VALUES (1, 'Action');
Insert into genre (genre_id, name) VALUES (2, 'Adventure');
Insert into genre (genre_id, name) VALUES (3, 'Animation');
Insert into genre (genre_id, name) VALUES (4, 'Comedy');
Insert into genre (genre_id, name) VALUES (5, 'Crime');
Insert into genre (genre_id, name) VALUES (6, 'Documentary');
Insert into genre (genre_id, name) VALUES (7, 'Drama');
Insert into genre (genre_id, name) VALUES (8, 'Family');
Insert into genre (genre_id, name) VALUES (9, 'Fantasy');
Insert into genre (genre_id, name) VALUES (10, 'Kids');
Insert into genre (genre_id, name) VALUES (11, 'History');
Insert into genre (genre_id, name) VALUES (12, 'Horror');
Insert into genre (genre_id, name) VALUES (13, 'Musical');
Insert into genre (genre_id, name) VALUES (14, 'Mystery');
Insert into genre (genre_id, name) VALUES (15, 'Romance');
Insert into genre (genre_id, name) VALUES (16, 'Science Fiction');
Insert into genre (genre_id, name) VALUES (17, 'TV Movie');
Insert into genre (genre_id, name) VALUES (18, 'Thriller');
Insert into genre (genre_id, name) VALUES (19, 'War');
Insert into genre (genre_id, name) VALUES (20, 'Western');
Insert into genre (genre_id, name) VALUES (21, 'News');
Insert into genre (genre_id, name) VALUES (22, 'Reality');
Insert into genre (genre_id, name) VALUES (23, 'Short');
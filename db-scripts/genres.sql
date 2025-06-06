use genres;

create table genre (
  genre_id int primary key auto_increment,
  name varchar(1000) not null
);

# -------------------- INSERT GENRES --------------------------------
Insert into genre (name) VALUES ('Action');
Insert into genre (name) VALUES ('Adventure');
Insert into genre (name) VALUES ('Animation');
Insert into genre (name) VALUES ('Comedy');
Insert into genre (name) VALUES ('Crime');
Insert into genre (name) VALUES ('Documentary');
Insert into genre (name) VALUES ('Drama');
Insert into genre (name) VALUES ('Family');
Insert into genre (name) VALUES ('Fantasy');
Insert into genre (name) VALUES ('Kids');
Insert into genre (name) VALUES ('History');
Insert into genre (name) VALUES ('Horror');
Insert into genre (name) VALUES ('Musical');
Insert into genre (name) VALUES ('Mystery');
Insert into genre (name) VALUES ('Romance');
Insert into genre (name) VALUES ('Science Fiction');
Insert into genre (name) VALUES ('TV Movie');
Insert into genre (name) VALUES ('Thriller');
Insert into genre (name) VALUES ('War');
Insert into genre (name) VALUES ('Western');
Insert into genre (name) VALUES ('News');
Insert into genre (name) VALUES ('Reality');
Insert into genre (name) VALUES ('Short');
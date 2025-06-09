use movies;

drop table if exists movie;
create table movie (
  movie_id int primary key auto_increment,
  title varchar(1000) not null,
  original_title varchar(1000),
  description text,
  release_date date,
  homepage_url text,
  trailer_url text,
  image_url text,
  overall_rating float default 0,
  total_ratings int default 0,
  total_votes int default 0,
  duration int, 
  revenue bigint,
  budget bigint,
  adult bool,
  created_at timestamp default current_timestamp
);
alter table movie auto_increment = 1;

drop table if exists rating;
create table rating (
  user_id int not null,
  movie_id int not null,
  rating float check (rating >= 0 and rating <= 10),
  created_at timestamp default current_timestamp,
  primary key (user_id, movie_id),
  foreign key (movie_id) references movie(movie_id) on delete cascade
);

drop table if exists movie_genre;
create table movie_genre (
  movie_id int,
  genre_id int,
  primary key (movie_id, genre_id),
  foreign key (movie_id) references movie(movie_id) on delete cascade
);

drop table if exists movie_language;
create table movie_language (
  movie_id int,
  language_id int,
  primary key (movie_id, language_id),
  foreign key (movie_id) references movie(movie_id) on delete cascade
);

drop table if exists movie_country;
create table movie_country (
  movie_id int,
  country_id int,
  primary key (movie_id, country_id),
  foreign key (movie_id) references movie(movie_id) on delete cascade
);

drop table if exists production_company;
create table production_company (
  movie_id int,
  company_id int,
  primary key (movie_id, company_id),
  foreign key (movie_id) references movie(movie_id) on delete cascade
);



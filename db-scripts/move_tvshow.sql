create database if not exists movie_tvshow
	default character set utf8mb4
  collate utf8mb4_unicode_ci;
use movie_tvshow;

-- ================================
-- Common tables
-- ================================

drop table if exists languages;
create table languages (
  id int primary key auto_increment,
  name varchar(100) not null,
  iso_code varchar(10) unique not null
);

drop table if exists genres;
create table  genres (
  id int primary key auto_increment,
  name varchar(500) unique not null
);

drop table if exists countries;
create table  countries (
  id int primary key auto_increment,
  name varchar(100) not null,
  iso_code char(2),
  flag_emoji varchar(4)
);

drop table if exists companies;
create table  companies (
  id int primary key auto_increment,
  name varchar(255) unique not null,
  headquarters varchar(255),
  website text
);

-- ================================
-- Movie-TVShow Table
-- ================================
drop table if exists title;
create table title (
  title_id int primary key auto_increment,
  title varchar(1000) not null,
  original_title varchar(1000),
  type enum('movie', 'tv_show') not null,
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

-- ================================
-- Episode table for tv shows
-- ================================
drop table if exists episode;

-- ================================
-- Relationship tables
-- ================================
drop table if exists title_genre;
create table title_genre (
  title_id int,
  genre_id int,
  primary key (title_id, genre_id),
  foreign key (title_id) references title(title_id) on delete cascade,
  foreign key (genre_id) references genres(id)
);

drop table if exists title_language;
create table title_language (
  title_id int,
  language_id int,
  primary key (title_id, language_id),
  foreign key (title_id) references title(title_id) on delete cascade,
  foreign key (language_id) references languages(id)
);

drop table if exists title_country;
create table title_country (
  title_id int,
  country_id int,
  primary key (title_id, country_id),
  foreign key (title_id) references title(title_id) on delete cascade,
  foreign key (country_id) references countries(id)
);

drop table if exists title_company;
create table title_company (
  title_id int,
  company_id int,
  primary key (title_id, company_id),
  foreign key (title_id) references title(title_id) on delete cascade,
  foreign key (company_id) references companies(id)
);

-- ================================
-- Rating table
-- ================================
drop table if exists rating;
create table rating (
  user_id varchar(64) not null,
  title_id int not null,
  rating float check (rating >= 0 and rating <= 10),
  created_at timestamp default current_timestamp,
  primary key (user_id, title_id),
  foreign key (title_id) references title(title_id) on delete cascade
);





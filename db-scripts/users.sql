use movies;

create table users (
  user_id int primary key auto_increment,
  username varchar(100) not null unique,
  email varchar(100) unique,
  avatar_url varchar(1000),
  role enum('user', 'admin') default 'user',
  created_at timestamp default current_timestamp
);

create table followers (
	user_id int,
    friend_id int,
    primary key (user_id, friend_id),
    foreign key (user_id) references users(user_id) on delete cascade,
    foreign key (friend_id) references users(user_id) on delete cascade
);


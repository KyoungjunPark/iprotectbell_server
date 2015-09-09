drop table if exists user;
create table user (
  user_id integer primary key autoincrement,
  user_name text not null
);

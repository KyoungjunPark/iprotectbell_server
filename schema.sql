drop table if exists user;
create table user (
    user_id text primary key,
    user_password text not null,
    bell_id integer not null,
    FOREIGN KEY(bell_id)
    REFERENCES bell(id)
);

drop table if exists bell;
create table bell (
    id integer primary key autoincrement,
    open_status integer not null
);

drop table if exists log;
create table log (
    date date_time not null,
    information text not null,
    importance integer not null
);


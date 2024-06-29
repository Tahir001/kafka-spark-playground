create database tolldata;

use tolldata;

create table livetolldata(
    timestamp datetime,
    vehicle_id int,
    vehicle_type char(25),
    toll_plaza_id smallint
);
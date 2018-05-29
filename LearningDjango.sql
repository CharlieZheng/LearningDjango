use LearningGo;
alter table userdetail default character set utf8;
alter table userinfo default character set utf8;
show create table userdetail;
show create table userinfo;

alter table userinfo modify department varchar(64) character set utf8;
alter table userinfo modify username varchar(64) character set utf8;
alter table userdetail modify intro varchar(64) character set utf8;
alter table userdetail modify profile varchar(64) character set utf8;

set character_set_connection = 'utf8';
set character_set_results = 'utf8';
set character_set_client = 'utf8';

select * from  userinfo;
drop table userinfo;
drop table userdetail;
select * from TestModel_question;
CREATE TABLE `userinfo` (
	`uid` INT(10) NOT NULL AUTO_INCREMENT,
	`username` VARCHAR(64) NULL DEFAULT NULL,
	`department` VARCHAR(64) NULL DEFAULT NULL,
	`created` DATE NULL DEFAULT NULL,
	PRIMARY KEY (`uid`)
);

CREATE TABLE `userdetail` (
	`uid` INT(10) NOT NULL DEFAULT '0',
	`intro` TEXT NULL,
	`profile` TEXT NULL,
	PRIMARY KEY (`uid`)
)

select * from userdetail;
select * from userinfo;
BEGIN;

DROP DATABASE IF EXISTS `myblog`;
CREATE DATABASE `myblog` DEFAULT CHARACTER SET utf8 ;
USE myblog;
DROP TABLE IF EXISTS `blog`;
CREATE TABLE `blog` (
    `id` int(11) not null AUTO_INCREMENT,
    `title` varchar(100) not null,
    `content` longtext not null,
    `summary` text not null,
    `create_time` DATETIME not null,
    `update_time` DATETIME not null,
    `view_times` int(11) not null DEFAULT 0,
    PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS `comments`;
CREATE TABLE `comments` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(32) NOT NULL, 
    `userimage` varchar(100) NULL, 
    `blog_id` int(11) NOT NULL, 
    `content` text NOT NULL, 
    `create_time` datetime NOT NULL, 
    `parent_id` int(11) NOT NULL,
    `comment_id` int(11) NOT NULL, 
    `comment_username` varchar(32) NULL,
    PRIMARY KEY (`id`)
);


DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(32) NOT NULL, 
    `image` varchar(100) NULL, 
    `account` varchar(100) NULL, 
    `passwd` varchar(100) NULL, 
    PRIMARY KEY (`id`)
);

COMMIT;



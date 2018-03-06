MYSQL

数据库操作:
    查看所有数据库  show databases;
    创建数据库  create database 数据库名 charset=utf-8;
    删除数据库  drop database 数据库名;
    切换数据库  use 数据库名;
    查看当前选择的数据库  select database();

表操作：
    可视化查看表结构  desc 表名;
    查看当前数据库中所有表  show tables;
    创建表  create table 表名(列及类型);
        eg: create table students(id int auto_increment primary key,
                                  name varchar(10) not null,
                                  birthday datetime);
    修改表  alter table 表名 add|change|drop 列名 类型;
        eg: alter table students add birthday datetime;
    删除表  drop table 表名;
    更改表名称  rename table 原表名 to 新表名;
    查看表的创建语句  show create table 表名;

数据操作：
    查询  select * from 表名;
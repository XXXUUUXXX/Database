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
    增加
        全列插入  insert into 表名 values(...);   按照列的顺序输入
            eg: insert into students values(0,'佩奇','1999-1-1');
        缺省插入  insert into 表名(列1,...) values(值1,,...);
            eg: insert into students(name) values('小猪');
        同时插入多条数据  insert into 表名 values(...),(...);或insert into 表名(列名,...) values(值),(值);
    修改  update 表名 set 列1=值1,...where 条件;    
        eg: update students set birthday='2001-01-01' where id=2;
    删除  delete from 表名 where 条件;

数据备份：
    sudo -s
    cd /var/lib/mysql
    mysqldump -uroot -p 数据库名 > ~/Desktop/备份文件.sql;

数据恢复：
    mysql -uroot -p 数据库名 < ~/Desktop/备份文件.sql;

消除重复行：
    select distinct 行名 from 表名;
        eg: select distinct gender from students;

比较运算符：
    等于=
    大于>
    大于等于>=
    小于<
    小于等于<=
    不等于!=或<>

逻辑运算符：
    and
    or
    not

模糊查询
    like
    %表示任意多个任意字符
    _表示一个任意字符
    eg:查询姓黄并且名字是一个字的学生
        select * from students where name like '黄_';
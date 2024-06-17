# SQL - Introduction

![Project badge](path/to/project-badge-image)

**Level:** Novice  
**Author:** Guillaume  
**Weight:** 1  

**Note:** This project has been migrated to checker v2. Your score will be updated as you progress.

## Concepts
For this project, we expect you to explore the concept of Databases.

## Resources
Read or watch the following resources:
- [What is Database & SQL?](#)
- [Install MySQL (MySQL Server)](#)
- [A Basic MySQL Tutorial](#)
- [Basic SQL statements: DDL and DML](#)
- [Basic queries: SQL and RA](#)
- [SQL technique: functions](#)
- [SQL technique: subqueries](#)
- [What makes the big difference between a backtick and an apostrophe?](#)
- [MySQL Cheat Sheet](#)
- [MySQL 8.0 SQL Statement Syntax](#)

## Learning Objectives
By the end of this project, you should be able to explain the following concepts without the help of Google:

### General
- What is a database
- What is a relational database
- What does SQL stand for
- What is MySQL
- How to create a database in MySQL
- What do DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE, or DELETE data
- What are subqueries
- How to use MySQL functions

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e., syntax above)
- All your files should start with a comment describing the task
- All SQL keywords should be in uppercase (e.g., `SELECT`, `WHERE`)
- A `README.md` file, at the root of the project folder, is mandatory
- The length of your files will be tested using `wc`

## More Info

### Comments for your SQL file
Example:
```sql
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$


# MySQL Scripts

## Tasks

### 0. List databases
**mandatory**

Write a script that lists all databases of your MySQL server.

Example usage:
```bash
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database
information_schema
mysql
performance_schema
sys

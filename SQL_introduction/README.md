# SQL - Introduction

![image](https://github.com/ghinzuka/holbertonschool-higher_level_programming/assets/102736316/68ea7090-4c9c-41dc-ac09-4857ef019749)



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
```

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
```
| Task Number | Task Title               | Description                                                                                                                                                                                                                          |
|-------------|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0           | List databases           | Write a script that lists all databases of your MySQL server.                                                                                                                                                                        |
| 1           | Create a database        | Write a script that creates the database hbtn_0c_0 in your MySQL server. If the database hbtn_0c_0 already exists, your script should not fail.                                                                                       |
| 2           | Delete a database        | Write a script that deletes the database hbtn_0c_0 in your MySQL server. If the database hbtn_0c_0 doesn’t exist, your script should not fail.                                                                                       |
| 3           | List tables              | Write a script that lists all the tables of a database in your MySQL server.                                                                                                                                                         |
| 4           | First table              | Write a script that creates a table called first_table in the current database in your MySQL server. If the table first_table already exists, your script should not fail.                                                           |
| 5           | Full description         | Write a script that prints the full table description of the table first_table from the database hbtn_0c_0 in your MySQL server.                                                                                                     |
| 6           | List all in table        | Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.                                                                                                                        |
| 7           | First add                | Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.                                                                                                                             |
| 8           | Count 89                 | Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.                                                                                             |
| 9           | Full creation            | Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and adds multiple rows.                                                                                                              |
| 10          | List by best             | Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server, ordered by score (top first).                                                                                        |
| 11          | Select the best          | Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server, ordered by score (top first).                                                                     |
| 12          | Cheating is bad          | Write a script that updates the score of Bob to 10 in the table second_table without using Bob’s id value, only the name field.                                                                                                      |
| 13          | Score too low            | Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.                                                                                                   |
| 14          | Average                  | Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.                                                                                              |
| 15          | Number by score          | Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server, sorted by the number of records (descending).                                          |
| 16          | Say my name              | Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server, excluding rows without a name value, ordered by descending score.                                                    |
| 17          | Go to UTF8               | Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.                                                                                                                   |
| 18          | Temperatures #0          | Import in hbtn_0c_0 database this table dump: download. Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).                                                              |
| 19          | Temperatures #1          | Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0). Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending).                          |
| 20          | Temperatures #2          | Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0). Write a script that displays the max temperature of each state (ordered by State name).                                                           |

AUTHOR : BAPTISTE POUQUEROU
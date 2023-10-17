# SQL - Introduction

* A <b>database</b> is a bunch of records
* In a <b>relational database</b> the data stored is organised in rows and colums.
* <b>MySQL</b> is a database management system for structured data
* A <b>Data Definition Language, DDL</b> defines/modifies the structure of the objects in the database. Examples: CREATE, DROP
* A <b>Data Manipulation Language, DML</b> defines/modifies the data stored in the database. Examples: SELECT, UPDATE, DELETE
* Create a student table:
```
CREATE TABLE students (
	student_id NUMBER,
	name VARCHAR(32),
	age NUMBER,
	graduation_year DATE
	);
```
* To select from the table:<br>
```SELECT * FROM students WHERE student_id=12```

* To insert a record:<br> ```INSERT INTO students (student_id, name, age, graduation_year) VALUES (2290, Vicky, 39, 12-5-2018)```

* To update a record:<br>```UPDATE students WHERE student_id=2290 SET age=29```

* A subquery is a query within a query. Surround it with (). For example, give me all students whose graduation year is <em>the same as Vicky's</em>. The year is retrieved by a subquery
```
SELECT * students
WHERE graduation_year=
    (SELECT graduation_year
    FROM students
    WHERE name=Vicky)
```

Some of MySQL's functions:
* AVG()
* SUM()
* COUNT()
* MAX()
* MIN()


### References:
* <a href="https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US">SQL Commands Cheat Sheet</a>
* <a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=intro.html">Database design with UML and SQL</a>, a great book
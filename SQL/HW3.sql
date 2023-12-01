/* Спроектировать бд “школы”
необходимо спроектировать таблицы “школа” и “ученики”
1.1. показать всех школы и их учеников
1.2. Показать всех учеников  с фамилией “Иванов” и школы, в которых они учатся
1.3. Показать всех  учеников с именем “Иван” или именем “Лариса” и школы, в которых они учатся
1.4. Показать всех учеников в возрасте от 10 до 15 лет включительно и школы, в которых они учатся*/
create database shcool;
use shcool;

create table if not exists students(
	name_student varchar (255),
    surname_student varchar (255),
    age int ,
    id_student int primary key AUTO_INCREMENT
);
create table if not exists shcools(
	id_shcool int primary key AUTO_INCREMENT,
    name_shcool varchar(255),
    id_student int,
    FOREIGN KEY (id_student) REFERENCES students(id_student)
);

insert into students(name_student, surname_student,age) values
("Иван", "Иванов", 15), -- 1 
("Нина", "Иванова", 13), -- 2
("Лариса", "Киселёва", 15), -- 3
("Иван", "Соколов", 14), -- 4
("Марина", "Сидорова", 9), -- 5
("Лариса", "Котова", 7), -- 6
("Михаил", "Иванов", 18), -- 7
("Анна", "Волкова", 17), -- 8
("Василий", "Николаев", 15); -- 9

insert into shcools(name_shcool, id_student) values
("СОШ №1", 1),
("СОШ №5", 2),
("СОШ №3", 3),
("СОШ №11", 4),
("СОШ №55", 5),
("СОШ №44", 6),
("Лицей №1", 7),
("Гимназия №1", 8),
("Лицей №2", 9);

/* 1.1. показать всех школы и их учеников */
select name_shcool, name_student, surname_student from students, shcools 
where shcools.id_student = students.id_student;

/* 1.2. Показать всех учеников  с фамилией “Иванов” и школы, в которых они учатся */
select name_shcool, name_student, surname_student from students, shcools 
where surname_student = "Иванов" and shcools.id_student = students.id_student;

/* 1.3. Показать всех  учеников с именем “Иван” или именем “Лариса” и школы, в которых они учатся */
select name_shcool, name_student, surname_student from students, shcools 
where (name_student = "Иван" or name_student = "Лариса") and shcools.id_student = students.id_student;

/* 1.4. Показать всех учеников в возрасте от 10 до 15 лет включительно и школы, в которых они учатся*/
select name_shcool, name_student, surname_student, age from students, shcools 
where age >= 10 and age <= 15 and shcools.id_student = students.id_student;


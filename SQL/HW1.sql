/*1.
Создать таблицу группа (имя, рейтинг, курс)
добавить 3 любые группы
показать группы(имя рейтинг и курс) рейтинг*/
create table training_course(
  name_student varchar(50),
  rating int,
  course varchar(100)
);
insert into training_course
value
("Ekatrina", 78, "QA"),
("Viktoria", 65, "Paython"),
("Maksim", 69, "SQL");
select * from training_course;
select rating from training_course;

/*3.
Создать таблицу игры (имя игры, дата и время сохранения)
добавить 3 любые игры
показать все записи игр*/
create table game(
  name_game varchar(50),
  data_save date,
  time_save time
);
insert into game
value
("World of Warcraft", "2023-11-28", "22:17:48"),
("RAFT", "2020-10-11", "17:11:03"),
("The Long Dark", "2022-05-17", "03:57:30");
select * from game;

/*4.
Создать таблицу врачи(имя, должность, ставка)
добавить 3 любых врача
показать всех врачей(имя должность ставка)*/
create table doctors(
  name_doctor varchar(50),
  job_title varchar(50),
  bid int
);
insert into doctors
value
("Nike", "surgeon", 10000),
("Leam", "therapist", 7500),
("Anna", "ENT", 8700);

/* ----- Задание 1 ----- */
 use best_aero;
create table if not exists passengers (
	id INT PRIMARY KEY auto_increment,
    name_passenger VARCHAR(30) );
    

create table if not exists companies(
	company_name varchar (255),
    id int primary key AUTO_INCREMENT
);
create table if not exists trips(
    plane varchar(255),
    town_from varchar (255),
    town_to varchar (255),
    time_out datetime,
    time_in datetime,
    id int primary key AUTO_INCREMENT,
    company int,
    foreign key (company) REFERENCES companies(id)
    );
create table if not exists Pass_in_trip(
	id INT PRIMARY KEY auto_increment,
	trip INT,
     FOREIGN KEY (trip) REFERENCES trips (id),
    passenger INT,
     FOREIGN KEY (passenger) REFERENCES passengers (id),
     place VARCHAR(3));



-- Добавление записей в таблицу "passengers"
INSERT INTO passengers (name_passenger) VALUES
    ('John Smith'),
    ('Emma Johnson'),
    ('Michael Brown'),
    ('Sophia Williams'),
    ('William Davis'),
    ('Olivia Miller'),
    ('James Wilson'),
    ('Ava Martinez'),
    ('Robert Anderson'),
    ('Mia Garcia'), 
    ('Sophie Brown'),
    ('Liam Johnson'),
    ('Charlotte Davis'),
    ('Noah Martinez'),
    ('Ava Smith'),
    ('Ethan Wilson'),
    ('Isabella Thompson'),
    ('Mason Garcia'),
    ('Olivia Clark'),
    ('William Rodriguez');

-- Добавление записей в таблицу "companies"
INSERT INTO companies (company_name) VALUES
    ('Delta Airlines'),
    ('United Airlines'),
    ('American Airlines'),
    ('Lufthansa'),
    ('Emirates'),
    ('British Airways'),
    ('Air France'),
    ('Qatar Airways'),
    ('Singapore Airlines'),
    ('Cathay Pacific');

-- Добавление записей в таблицу "trips"
INSERT INTO trips (plane, town_from, town_to, time_out, time_in, company) VALUES
    ('Boeing 737', 'New York', 'Los Angeles', '2023-01-01 08:00:00', '2023-01-01 11:00:00', 1),
    ('Airbus A320', 'London', 'Paris', '2023-01-02 09:00:00', '2023-01-02 10:30:00', 2),
    ('Boeing 777', 'Tokyo', 'Sydney', '2023-01-03 10:00:00', '2023-01-03 22:00:00', 3),
    ('Airbus A350', 'Dubai', 'Singapore', '2023-01-04 11:00:00', '2023-01-04 15:00:00', 4),
    ('Boeing 787', 'Berlin', 'Moscow', '2023-01-05 12:00:00', '2023-01-05 14:30:00', 5),
    ('Airbus A380', 'Rome', 'Tokyo', '2023-01-06 13:00:00', '2023-01-06 20:00:00', 6),
    ('Boeing 747', 'Paris', 'Dubai', '2023-01-07 14:00:00', '2023-01-07 18:00:00', 7),
    ('Airbus A330', 'Singapore', 'Hong Kong', '2023-01-08 15:00:00', '2023-01-08 16:30:00', 8),
    ('Boeing 767', 'New Delhi', 'Sydney', '2023-01-09 16:00:00', '2023-01-09 23:00:00', 9),
    ('Airbus A310', 'Hong Kong', 'Tokyo', '2023-01-10 17:00:00', '2023-01-10 19:30:00', 10);



-- Добавление записей в таблицу "Pass_in_trip"
INSERT INTO Pass_in_trip (trip, passenger, place) VALUES
    (1, 1, 'A1'),
    (2, 2, 'B3'),
    (3, 3, 'C2'),
    (4, 4, 'D4'),
    (4, 15, 'F4'),
      (4, 16, 'E4'),
      (4, 17, 'A5'),
      (4, 18, 'B5'),
    (5, 5, 'E6'),
    (6, 6, 'F5'),
    (7, 7, 'G8'),
    (8, 8, 'H10'),
    (8, 11, 'B10'),
    (8, 12, 'A11'),
    (8, 13, 'C10'),
    (8, 14, 'D10'),
    (9, 9, 'I7'),
    (10, 10, 'J9'); 

-- Выбрать пассажиров и их места в рейсе: 
select name_passenger, trip, place 
from passengers 
join  Pass_in_trip 
on Pass_in_trip.passenger = passengers.id 
order by trip; 

-- Посчитать общее количество пассажиров на конкретном рейсе:
select count(place), trip
from passengers 
join  Pass_in_trip 
on Pass_in_trip.passenger = passengers.id 
group by trip
order by trip; 

-- посчитать рейсы, отправляющиеся после 2023-01-05:
select count(id) 
from trips 
where time_out > '2023-01-05 23:59:59';

-- Посчитать количество рейсов, отправленных из каждого города:
select distinct town_from, count(trip)
from trips
join pass_in_trip
on pass_in_trip.trip = trips.id
group by town_from;

-- Выбрать среднюю продолжительность рейсов для каждой компании:
select company_name, time(avg(timediff(time_in, time_out)))
from trips
join companies
on trips.company = companies.id
group by company_name;

-- Выбрать пассажиров, у которых имя начинается на 'J' и место в рейсе начинается на 'B':
-- данный запрос вернет пустую таблицу, потому что таих совпадений нет, 
-- но если вместо B в поиск места поставить A, то у нас будет не пустой ответ.
select name_passenger, place
from passengers
join pass_in_trip
on Pass_in_trip.passenger = passengers.id 
and name_passenger like "J%" 
and place like "B%";

-- Выбрать компании и количество рейсов, осуществленных каждой из них:
select distinct company_name, count(pass_in_trip.id)
from companies
join trips
join pass_in_trip
on trips.company = companies.id
and pass_in_trip.trip = trips.id
group by company_name; 


/* ----- Задание 3 - запросы для магазинчика ----- */
-- 1.	найти всех пользователей и их адреса
SELECT * FROM user_addrs, users WHERE users.last_id = user_addrs.user;

-- 2.	найти все заказы и заказанные предметы
SELECT orders.last_id, orders.price, orders.phone, orders.addr, items.title, items.price
FROM orders 
JOIN order_items 
JOIN items
ON orders.last_id = order_items.order_id
AND order_items.item_id = items.last_id;

-- 3.	найти всех пользователей и их номера телефона
SELECT * FROM users, user_phones WHERE users.last_id = user_phones.last_id;

-- 4.	посчитать кол-во пользователей сделавших заказ
SELECT count(DISTINCT user_id) FROM orders;

-- 5.	подсчитать общую сумму заказов для каждого пользователя 
SELECT sum(price), users.name 
FROM orders 
JOIN users
ON users.last_id = orders.user_id
GROUP BY users.name;



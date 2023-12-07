/* задание 1 
1.	На основе таблиц ниже, составьте запрос, где стоимость заказов больше 1000 и меньше 3000
(Вместо стоимость id - это обговороено на уроке)!!!
2.	На основе таблиц ниже, составьте запрос за весенние месяцы 2016 года
3.	Покажите Пользователей у кого нет заказов */

create database hw4_1;
use hw4_1;

CREATE TABLE customers
( customer_id int NOT NULL,
  last_name char(50) NOT NULL,
  first_name char(50) NOT NULL,
  favorite_website char(50),
  CONSTRAINT customers_pk PRIMARY KEY (customer_id)
);

CREATE TABLE orders
( order_id int NOT NULL,
  customer_id int,
  order_date date,
  CONSTRAINT orders_pk PRIMARY KEY (order_id),
  foreign key (customer_id) references customers(customer_id)
);

INSERT INTO customers
(customer_id, last_name, first_name, favorite_website)
VALUES
(4000, 'Jackson', 'Joe', 'techonthenet.com'),
(5000, 'Smith', 'Jane', 'digminecraft.com'),
(6000, 'Ferguson', 'Samantha', 'bigactivities.com'),
(7000, 'Reynolds', 'Allen', 'checkyourmath.com'),
(8000, 'Anderson', 'Paige', NULL),
(9000, 'Johnson', 'Derek', 'techonthenet.com');

INSERT INTO orders
(order_id, customer_id, order_date)
VALUES
(1,7000,'2016/04/18'),
(2,5000,'2016/04/18'),
(3,8000,'2016/04/19'),
(4,4000,'2016/04/20'),
(5,null,'2016/05/01');


/* 1.	На основе таблиц ниже, составьте запрос, где стоимость заказов больше 1000 и меньше 3000
(Вместо стоимость id)!!! */
select customer_id, last_name, first_name from customers
where customer_id > 1000 and customer_id < 3000;
-- этот запрос будет пустым, потому что у нас нет таких значений
-- но если мы немного исправим условия поиска под наши данные, то запрос будет работать
select customer_id, last_name, first_name from customers
where customer_id > 4000 and customer_id < 7000;

/* 2.	На основе таблиц ниже, составьте запрос за весенние месяцы 2016 года */
select * from   orders where year(order_date) = 2016
and month(order_date) < 6 and month(order_date) > 2;

/* 3.	Покажите Пользователей у кого нет заказов */
select customer_id, last_name, first_name from customers
where customers.customer_id not in 
(select customers.customer_id from customers, orders
where orders.customer_id = customers.customer_id);


/* задание 3.
Спроектировать  бд “семья”
по схеме и создать запросы
1.1. Найти имена всех матерей (mother)
1.2. Определить, кто из членов семьи покупал картошку (potato)
1.3. Определить какие товары не были куплены */

create database hw4_2;
use hw4_2;

create table if not exists goodtypes(
good_type_id int primary key,
good_type_name varchar(255)
);

create table if not exists goods(
good_id int primary key,
good_name varchar(255),
type int,
foreign key (type) REFERENCES goodtypes(good_type_id)
);

create table if not exists familymembers(
member_id int primary key,
status varchar(255),
member_name varchar(255),
birthday datetime
);

create table if not exists payments(
payment_id int primary key,
family_member int,
good int,
amount int,
unit_price int,
date datetime,
foreign key (family_member) REFERENCES familymembers(member_id),
foreign key (good) REFERENCES goods(good_id)
);

insert into goodtypes values
(1, 'food'),
(2, 'household chemicals'),
(3, 'electronics'),
(4, 'cloth'),
(5, 'shoes');

insert into goods values
(151, 'milk', 1),
(100, 'potato', 1),
(1547, 'shampoo', 2),
(102468, 'smartphone', 3),
(4684, 'socks', 4),
(65466, 'shoes', 5);

insert into familymembers values
(10, 'mother', 'Nina Pavlova', '1987-05-28'),
(20, 'father', 'Boris Pavlov', '1984-07-22'),
(30, 'dother', 'Liza Pavlova', '2002-01-18');

insert into payments values
(1, 10, 1547, 2, 250, '2023-08-03'),
(2, 10, 100, 10, 500, '2023-05-01'),
(3, 20, 151, 3, 100, '2023-07-09'),
(4, 30, 100, 1, 50, '2023-06-29'),
(5, 10, 102468, 1, 15999, '2023-07-29'),
(6, 30, 65466, 2, 7000, '23-07-30'); 

/* 1.1. Найти имена всех матерей (mother) */
select status, member_name from familymembers where status = 'mother';

/* 1.2. Определить, кто из членов семьи покупал картошку (potato) */
select member_name from familymembers, goods, payments 
where familymembers.member_id = payments.family_member
and goods.good_id = payments.good
and good_name = 'potato';

/* 1.3. Определить какие товары не были куплены  */
select good_name from goods
where good_id not in 
(select good_id from goods, payments
where goods.good_id = payments.good);
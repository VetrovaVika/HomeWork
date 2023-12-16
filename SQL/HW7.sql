/* Задание */
create database restaurants;
use restaurants;
-- Создание таблицы для ресторана
CREATE TABLE Restaurant (
    RestaurantID INT PRIMARY KEY,
    Name VARCHAR(50),
    Address VARCHAR(100),
    Phone VARCHAR(15)
);

-- Создание таблицы для столиков
CREATE TABLE Tables (
    TableID INT PRIMARY KEY,
    RestaurantID INT,
    Capacity INT,
    IsAvailable BOOLEAN,
    FOREIGN KEY (RestaurantID) REFERENCES Restaurant(RestaurantID)
);

-- Создание таблицы для клиентов
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(50),
    Email VARCHAR(50),
    Phone VARCHAR(15)
);

-- Создание таблицы для бронирований
CREATE TABLE Reservations (
    ReservationID INT PRIMARY KEY,
    TableID INT,
    CustomerID INT,
    ReservationTime DATETIME,
    FOREIGN KEY (TableID) REFERENCES Tables(TableID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Создание таблицы для официантов
CREATE TABLE Waiters (
    WaiterID INT PRIMARY KEY,
    Name VARCHAR(50),
    RestaurantID INT,
    FOREIGN KEY (RestaurantID) REFERENCES Restaurant(RestaurantID)
);


INSERT INTO Restaurant (RestaurantID, Name, Address, Phone)
VALUES
    (1, 'The Grand Bistro', '123 Main St, Cityville', '+1234567890'),
    (2, 'Taste of Italy', '456 Oak Ave, Townsville', '+0987654321'),
    (3, 'Sushi Delight', '789 Elm St, Villageton', '+1112223333'),
    (4, 'La Brasserie', '246 Maple St, Hamletown', '+4445556666'),
    (5, 'Mediterranean Oasis', '879 Pine St, Groveside', '+7778889999'),
    (6, 'Spice Kingdom', '369 Walnut St, Junction City', '+3334445555'),
    (7, 'The Steakhouse', '654 Birch Ave, Riversville', '+6667778888'),
    (8, 'Café Belle', '987 Cedar St, Hillside', '+2223334444'),
    (9, 'Seafood Harbor', '741 Ocean Dr, Bayview', '+9990001111'),
    (10, 'Pizzeria Roma', '321 Laurel St, Cliffside', '+8889990000');

INSERT INTO Tables (TableID, RestaurantID, Capacity, IsAvailable)
VALUES
    (1, 1, 4, true),
    (2, 1, 6, true),
    (3, 2, 8, true),
    (4, 3, 5, false),
    (5, 4, 10, true),
    (6, 5, 6, true),
    (7, 6, 4, true),
    (8, 7, 7, true),
    (9, 8, 3, false),
    (10, 9, 9, true);


INSERT INTO Customers (CustomerID, Name, Email, Phone)
VALUES
    (1, 'John Doe', 'johndoe@email.com', '+1112223334'),
    (2, 'Jane Smith', 'janesmith@email.com', '+2223334445'),
    (3, 'Alex Johnson', 'alexjohnson@email.com', '+3334445556'),
    (4, 'Emily Brown', 'emilybrown@email.com', '+4445556667'),
    (5, 'Michael Wilson', 'michaelwilson@email.com', '+5556667778'),
    (6, 'Olivia Miller', 'oliviamiller@email.com', '+6667778889'),
    (7, 'William Garcia', 'williamgarcia@email.com', '+7778889990'),
    (8, 'Sophia Martinez', 'sophiamartinez@email.com', '+8889990001'),
    (9, 'Daniel Lee', 'daniellee@email.com', '+9990001112'),
    (10, 'Ava Rodriguez', 'avarodriguez@email.com', '+1234567890');


INSERT INTO Reservations (ReservationID, TableID, CustomerID, ReservationTime)
VALUES
    (1, 1, 1, '2023-12-15 18:00:00'),
    (2, 2, 2, '2023-12-20 19:30:00'),
    (3, 3, 3, '2023-12-18 20:00:00'),
    (4, 4, 4, '2023-12-21 17:45:00'),
    (5, 5, 5, '2023-12-16 19:15:00'),
    (6, 6, 6, '2023-12-17 18:30:00'),
    (7, 7, 7, '2023-12-19 19:00:00'),
    (8, 8, 8, '2023-12-22 20:30:00'),
    (9, 9, 9, '2023-12-18 18:45:00'),
    (10, 10, 10, '2023-12-21 19:45:00');

INSERT INTO Waiters (WaiterID, Name, RestaurantID)
VALUES
    (1, 'Mark Thompson', 1),
    (2, 'Sarah Johnson', 2),
    (3, 'Chris Brown', 3),
    (4, 'Emma Davis', 4),
    (5, 'Ryan Wilson', 5),
    (6, 'Sophia Miller', 6),
    (7, 'David Garcia', 7),
    (8, 'Olivia Martinez', 8),
    (9, 'Daniel Lee', 9),
    (10, 'Ava Rodriguez', 10);

-- 1. Запрос на получение информации о ресторане:
-- Получить название, адрес и контактный телефон ресторана с идентификатором 1.
select name, address, phone from restaurant 
where restaurantid = 1;

-- 2. Запрос на выборку доступных столов:
-- Получить номера и вместимость столов, доступных для бронирования в ресторане с идентификатором 2.
select tableid, capacity from tables 
where isavailable = 1 and restaurantid = 2;

-- 3. Запрос на получение списка бронирований для ресторана:
-- Получить информацию о бронированиях, включая идентификатор бронирования, 
-- имя клиента, номер столика и время бронирования для столов из ресторана с идентификатором 3.
select ReservationID, customers.Name, Reservations.TableID, ReservationTime 
from Reservations join customers join tables
on Reservations.TableID = tables.TableID
and Reservations.CustomerID = Customers.CustomerID
and RestaurantID = 3;

-- 4. Запрос на получение списка официантов для ресторана:
-- Получить идентификатор и имя официантов, работающих в ресторане с идентификатором 4.
select WaiterID, Waiters.Name from Waiters
where RestaurantID = 4;

-- 5. Запрос на обновление данных о столике:
-- Изменить статус доступности столика с номером 5 на "недоступен".
update tables set IsAvailable = 0 where TableID = 5;

-- 6. Запрос на удаление клиента из базы данных:
-- Удалить информацию о клиенте с идентификатором 6 из базы данных.
update Customers set Name = default, Email = default, Phone = default
where CustomerID = 6;

-- 7. Запрос на получение информации о бронировании по идентификатору:
-- Получить все данные о бронировании с идентификатором 7.
-- select * from Reservations where ReservationID = 7;

-- 8. Запрос на подсчет количества столов в ресторане:
-- Получить общее количество столов в ресторане с идентификатором 8.
select count(TableID) from Tables where RestaurantID = 8;

-- 9. Запрос на выборку столов по вместимости:
-- Получить номера и вместимость столов, вместимость которых больше или равна 6.
select TableID, Capacity from Tables where Capacity >= 6;

-- 10. Запрос на поиск информации о клиенте по имени:
-- Найти всех клиентов, имя которых содержит "John".
select Name from Customers where name like '%John%';







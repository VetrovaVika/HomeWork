/*ЗАДАНИЕ
Для всех примеров:
1.	создать схему (нарисовать в paint, erdplus , фото рисунка вашей схему и т.д.  )
2.	 написать SQL запросы на создания таких таблиц, а также придумать и написать на 
sql 3 разных select -запроса  (примеры показать все заказы покупателя "Иванов" и "Иванова"
все заказы покупателя "Иванов") 
Есть бд “МАГАЗИН”
необходимо спроектировать таблицы “ПОСТАВЩИКИ” и “ТОВАРЫ”*/
create database my_shop;
use my_shop;

create table if not exists products(
	id_product int primary key AUTO_INCREMENT,
    name_product varchar(255),
    min_quantity int, -- минимальное количество в упаковке/коробке/палете
    lifetime int -- срок годности/эксплуатации
);
create table if not exists providers(
	name_provider varchar (255),
    min_order int,
    id_provider int primary key,
    id_product int,
    FOREIGN KEY (id_product) REFERENCES products(id_product)
);


insert into products(name_product, min_quantity, lifetime) values
("food", 150, 1), -- 1
("household chemicals", 100, 36), -- 2
("cloth", 120, 60), -- 3
("electronics", 50, 48), -- 4
("furniture", 10, 120); -- 5

insert into providers values
("GEBA", 5000, 458798, 1),
("Polli_voz", 200, 252698, 5),
("Lukas", 1000, 362978, 2),
("Tom&Tim", 1200, 354560, 3),
("Eldorado", 50, 448768, 4);

/* 1. Какой поставщик возит товары "electronics"? */
select name_provider, name_product from providers, products
where name_product = "electronics" 
and providers.id_product = products.id_product;
/* 2. Показать поставщика, название товара и сроки годности/эксплуатации, 
которые меньше 50 месяцев. */
select name_provider, name_product, lifetime from providers, products
where lifetime < 50
and providers.id_product = products.id_product;
/* 3. Показать поставщика, у которого в поле ID есть цифра 4. */
select name_provider, id_provider from providers
where id_provider like "%4%";



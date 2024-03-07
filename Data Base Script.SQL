COPY INTO TRANSACTION
FROM @DATA 
FILES = ('transactions_clean.csv')
FILE_FORMAT = (TYPE='csv' SKIP_header = 1);ASSESMENT.ASSESMENTASSESMENT.ASSESMENTASSESMENT.ASSESMENT.DATA;

select * from transaction;

create table client(
client_id number,
client_name varchar,
client_last_name varchar,
email varchar
);

INSERT INTO client
SELECT client_id, client_name, client_lastname, email FROM transaction

create table Store(
store_id number,
store_name varchar,
location varchar
);

INSERT INTO Store
SELECT store_id, store_name, location FROM transaction

create or replace table Product(
product_id number,
street varchar,
city varchar,
state varchar,
zip_code number
);

INSERT INTO Product
SELECT product_id, street, city, state, zip_code FROM transaction

create or replace table Sales_fact(
transaction_id number,
quantity_of_items_sold number,
unit_price number(11,9),
discount number(3,2),
id number IDENTITY start 1 increment 1
);


INSERT INTO Sales_fact
SELECT transaction_id, quantity_of_items_sold, unit_price, discount, ROW_NUMBER()
  OVER (ORDER BY client_id DESC) FROM TRANSACTION

  select * from sales_fact

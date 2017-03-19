.read data.sql

-- Q1
create table flight_costs as
  with price_table(day1, price1, day2, price2) as (
      select 1, 20, 2, 30 union
      select day2, price2, day2 + 1, (price1 + price2) / 2 + 5 * ((day2 + 1) % 7) FROM price_table
      where day1 <= 24
  )
  select day1 as day, price1 as price from price_table;

-- Q2
create table schedule as
  with schedule_temp(path, dest, stops, price) as (
    select departure || ', ' || arrival, arrival, 1, price from flights
    where departure = 'SFO' union
    select s.path || ', ' || f.arrival, f.arrival, s.stops + 1, s.price + f.price
    from schedule_temp as s, flights as f
    where s.dest = f.departure and s.stops <= 1
  )
  select path, price from schedule_temp where dest = 'PDX' order by price asc;

-- Q3
create table shopping_cart as
  with cart(items, price, budget) as (
    select item, price, 60 - price from supermarket where price <= 60 union
    select c.items || ', ' || s.item, s.price, budget - s.price
    from cart as c, supermarket as s
    where s.price >= c.price and budget >= s.price
  )
  select items as list, budget as left_budget from cart
  order by left_budget asc, list asc;

-- Q4
create table number_of_options as
  select count(distinct meat) as number_of_options from main_course;

-- Q5
create table calories as
  select count(*) from main_course as m, pies as p where m.calories + p.calories < 2500;

-- Q6
create table healthiest_meats as
  select meat, min(m.calories + p.calories) as total_calories from main_course as m, pies as p 
  group by meat having max(m.calories + p.calories) <= 3000;

-- Q7
create table average_prices as
  select category, avg(msrp) from products group by category;

-- Q8
create table lowest_prices as
  select item, store, min(price) from inventory group by item;

-- Q9
create table shopping_list as
  select item, store from
  (select name, category from products group by category having min(msrp / rating)) temp, lowest_prices
  where item = name;

-- Q10
create table total_bandwidth as
  select sum(Mbs) from shopping_list as sh, stores as st where sh.store = st.store;

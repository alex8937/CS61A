create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  select name, size FROM dogs, sizes WHERE dogs.height > sizes.min AND dogs.height <= sizes.max;

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
    SELECT child from
    (select distinct d.name, height FROM dogs as d, parents as p WHERE d.name = p.parent) as a, parents
    where a.name = parent order by height desc;

-- Sentences about siblings that are the same size
create table sentences as
	select dog1 || ' and ' || dog2 || ' are ' || size || ' siblings' as sentence from
	(select dog1, dog2, s1.size as size from
	(select p1.child as dog1, p2.child as dog2 from parents p1, parents p2 where p1.parent = p2.parent and dog1 < dog2) as siblings,
	size_of_dogs as s1, size_of_dogs as s2 
	where dog1 = s1.name and dog2 = s2.name and s1.size = s2.size) as t;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";

-- non_parents is an optional, but recommended question
-- All non-parent relations ordered by height difference
create table non_parents as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";

create table ints as
    with i(n) as (
        select 1 union
        select n+1 from i limit 100
    )
    select n from i;

create table divisors as
    select "REPLACE THIS LINE WITH YOUR SOLUTION";

create table primes as
    select "REPLACE THIS LINE WITH YOUR SOLUTION";

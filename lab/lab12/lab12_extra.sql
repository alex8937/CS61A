.read lab12.sql

CREATE TABLE sp16favnum AS
  select number, count(*) as cnt from sp16students 
	group by number order by cnt DESC limit 1;

CREATE TABLE sp16favpets AS
  SELECT pet, COUNT(*) AS count FROM sp16students
    GROUP BY pet ORDER BY count DESC LIMIT 10;

CREATE TABLE fa16favpets AS
  select pet, count(*) as cnt from students 
	group by pet order by cnt DESC limit 10;

CREATE TABLE fa16dragon AS
  select pet, count(*) as cnt from students WHERE pet = 'dragon';

CREATE TABLE fa16alldragons AS
  select pet, count(*) as cnt from students where pet LIKE '%dragon%';


CREATE TABLE obedienceimage AS
  select seven, denero, count(*) as cnt from students where seven = '7' group by denero ;

CREATE TABLE smallest_int_count AS
  select smallest, count(*) as cnt from students where smallest >= 1 group by smallest order by smallest asc;

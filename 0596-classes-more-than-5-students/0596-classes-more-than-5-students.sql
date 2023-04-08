# Write your MySQL query statement below
select class from (

 select p.class, count(*) as s from courses as p
group by p.class
) as l
where l.s >= 5
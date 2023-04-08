# Write your MySQL query statement below
select s.score , DENSE_RANK() over (
order by s.score desc)
as "rank"
from Scores s;
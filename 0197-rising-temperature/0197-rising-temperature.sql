# Write your MySQL query statement below
select weather.id as Id 
from weather 
join weather as w on datediff(weather.recordDate, w.recordDate) = 1
and weather.temperature > w.temperature 
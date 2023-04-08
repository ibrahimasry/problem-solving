# Write your MySQL query statement below
select     player_id,
    event_date as first_login
 from
(select player_id , device_id , event_date , 
rank() over(partition by player_id order by event_date) as rn
from activity 
) as t
 where t.rn = 1
# Write your MySQL query statement below


select s.name as name from salesperson s where 
s.sales_id not in (
select o.sales_id from orders as o
 join company as c on o.com_id = c.com_id and c.name = "RED"


) 


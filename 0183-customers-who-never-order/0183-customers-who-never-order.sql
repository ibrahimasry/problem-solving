# Write your MySQL query statement below

select name  As Customers from Customers As b 
where b.id not in (select customerId from Orders)
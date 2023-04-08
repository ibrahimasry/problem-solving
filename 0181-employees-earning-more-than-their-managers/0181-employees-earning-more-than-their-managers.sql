# Write your MySQL query statement below
select  l1.name as Employee   from
Employee as l1 
left join Employee as l2 
on l2.id = l1.managerId  
where l2.salary <= l1.salary
# Write your MySQL query statement below

select d.name as Department,  e.name as Employee  ,
       Salary from Employee as e
join Department  as d on e.departmentId = d.id
where (e.departmentId , Salary) in (select departmentId, max(Salary) from Employee 
                                  
                                   group by departmentId
                                  )

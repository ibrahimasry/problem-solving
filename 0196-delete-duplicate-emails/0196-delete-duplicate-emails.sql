# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
delete from person
where person.id not in (
      select * from  ( SELECT 
            MIN(Id) AS Id
        FROM 
            Person
        GROUP BY
            Email	 ) As p
)
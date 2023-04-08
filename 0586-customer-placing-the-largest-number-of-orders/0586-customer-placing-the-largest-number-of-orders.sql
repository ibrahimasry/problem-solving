# Write your MySQL query statement below
select customer_number from (
select customer_number , count(*) as c from orders
group by customer_number
order by c desc
limit 1

    ) as ord

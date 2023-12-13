-- todas las llamadas
select * from calls;

-- todos los clientes
select * from customers;

-- todos los clientes con ocupación ingeniería
select * from customers where occupation like 'Engineer%';

-- todos las llamadas al cliente 839
select * from calls where customerid=839;

-- llamadas a los clientes con ocupación ingeniería
select 
	customerid, 
	count(callid) as numcalls, 
	sum(productsold) as totalsold 
from 
	calls 
where 
	customerid in (select customerid from customers where occupation like 'Engineer%')
group by 
	customerid;
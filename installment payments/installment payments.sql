declare 

cursor cont is
select *
from contracts;

math number (10,2);
n number(10):=1;
y number(1);
z number(2);
m date;
lst number(10,2);

begin

for x in cont loop

---check  the deposit 

 y :=0;
if  y = 0 then 

 lst := x.contract_total_fees - nvl(x.contract_deposit_fees,0);
 y := y+1;
 
 end if ; 
 
 ------check the pay method 
 
if x .contract_payment_type = 'ANNUAL' then 
  z := 12;
  elsif x .contract_payment_type = 'HALF_ANNUAL' then 
   z := 6;
  elsif x .contract_payment_type = 'QUARTER' then 
  z :=  3; 
  else
  z := 1;
 
 end if ; 
 
 ----check and insert on paymet 
 
 math := (lst/months_between(x.contract_enddate,x.contract_startdate))*z;
  m := x.contract_startdate;
 
while lst >0 loop
   
    insert into  INSTALLMENTS_PAID
    values(n,x.contract_id,m,math,0) ;
      n:=n+1;
      lst:=lst-math;
     m:=add_months(m,z);
      
 
 end loop;
 
end loop;

end;
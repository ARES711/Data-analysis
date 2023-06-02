---------create a table to put table names and primary keys columns for each table that its primary key not composite or varchar or char type  

create table ch_table AS
select table_name,count(position) as c
from all_cons_columns
where owner = 'HR' and position is not null and constraint_name like '%PK' 
group by table_name
order by table_name;

-------------------------

alter table ch_table add column_name varchar2(30);
alter table ch_table add data_type VARCHAR2(30);

--------- a cursor to add columns names to the check table

declare

cursor pk is
 select table_name ,column_name
 from all_cons_columns 
 where owner = 'HR'and position is not null and constraint_name like '%PK' ;

begin 

for x in pk loop 

update ch_table
set column_name = x.column_name
where  table_name= x.table_name;

end loop;

end;

---------a cursor to add columns types to the check table

declare

cursor dt is
 select data_type,column_name
 from user_tab_columns;
 
begin 

for x in dt loop 

update ch_table
set data_type = x.data_type
where  column_name= x.column_name;

end loop;

end;

---------a cursor to clean the check table from unwanted data types and keys 

declare

cursor ff is
 select *
 from ch_table;
 
begin 
 
for x in ff loop 

if x.c > 1 or x.data_type !='NUMBER' then 

delete from ch_table
where table_name= x.table_name;  
 
end if;

end loop;

end;

---------a cursor to drop the exidting sequences and  add a trigger sequence on  the remaining tables in check table 

declare
 
   cursor seq is 
   select table_name, column_name
    from ch_table;
    
 mx_pk number(8);
  v_sql varchar2(200);
   v_count_seq number(8) ;
  
begin
        
  for z in seq loop
  
  ---------check for seq
  
  select count(sequence_name)
  into v_count_seq 
  from all_sequences 
  where upper(sequence_name)=upper(z.table_name|| '_seq' ) and upper(sequence_owner)=upper('hr');
                                    
   if v_count_seq>0 then 
   execute immediate 'drop sequence ' || z.table_name|| '_seq' ;
   end if ;
   
  ---------
                                    
  execute immediate 'select max(' || z.column_name|| ')'|| ' from ' ||z.table_name INTO mx_pk;
  mx_pk :=nvl(mx_pk,0)+1;
    
  execute immediate 'create sequence hr.' || z.table_name || '_seq '||'start with '||mx_pk;
    
  execute immediate 'create or replace trigger ' || z.table_name|| '_trg' ||
  ' before insert on ' ||  z.table_name ||
  ' for each row ' || 
  
  'begin ' ||
  
  ' :new.'|| z.column_name ||' := ' ||z.table_name|| '_seq'||'.nextval;
  
   end;';
 
  end loop;
  
end;
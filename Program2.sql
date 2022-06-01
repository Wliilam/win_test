Create table If Not Exists Person (id int, email varchar(255))
Truncate table Person
insert into Person (id, email) values ('1', 'a@b.com')
insert into Person (id, email) values ('2', 'c@d.com')
insert into Person (id, email) values ('3', 'a@b.com')


select distinct(email)
from Person p
where exists (
    select *
    from (
        select email, count(id) as counter
        from Person
        group by email
    ) as temp
    where counter > 1 and p.email = temp.email
);
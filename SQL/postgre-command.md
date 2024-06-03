login database
`psql -p5432 sallyw`
create database: store, employees, france, world
`CREATE DATABASE name;` 
list up db
`\l`
load dump
`psql -h localhost -U sallyw -d store -f Store.sql`
`psql -h localhost -U sallyw -d employees -f Employees.sql`
`psql -h localhost -U sallyw -d france -f France.sql`
`psql -h localhost -U sallyw -d world -f World.sql`
list all the table 
`\dt`
change the database
`\c name`

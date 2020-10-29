# sb-miniproject4
Data Pipeline Mini Project - Event Ticket System Case Study

### Init Database
This project using MySQL 8.0 as the backend database.

MySQL installation guide for [Windows](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/windows-installation.html) and [Linux](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/linux-installation.html). 

* ***Create Database:*** Create a database named `ticket_event`
```
$ mysqladmin -u root -p create ticket_event
```
* ***Create tables:*** To create tables in `ticket_event` database:
```
$ mysql -u root -p ticket_event < sql/create_table.sql
``` 
## Testing

echo "Create dabase"
mysqladmin -u root -p create ticket_event

echo "Create table"
mysql -u root -p ticket_event < sql/create_table.sql

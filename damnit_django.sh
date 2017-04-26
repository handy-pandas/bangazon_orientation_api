find . -path "/bangazon_api/api/migrations/*.py" -not -name "__init__.py" -delete; #deletes all of the .py files in the migrations directory except for the __init__.py file.
find . -path "/bangazon_api/api/migrations/*.pyc"  -delete; #deletes all of the .pyc files in the migrations directory.
rm db.sqlite3; #deletes the database file.
python manage.py makemigrations api; #creates the migration.
python manage.py migrate; #runs the migration.  This will delete all of the data in your database.
python manage.py loaddata customer.json producttype.json paymenttype.json product.json order.json department.json employee.json computer.json training.json employeecomputer.json supportticket.json #loads the data from each .json file in sequential order.
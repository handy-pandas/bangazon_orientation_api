find . -path "/bangazon_api/api/migrations/*.py" -not -name "__init__.py" -delete; 
find . -path "/bangazon_api/api/migrations/*.pyc"  -delete; 
rm db.sqlite3; 
python manage.py makemigrations api; 
python manage.py migrate; 
python manage.py loaddata customer.json producttype.json paymenttype.json product.json order.json department.json employee.json computer.json training.json 

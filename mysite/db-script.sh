#This is a simple script that we are going to use whenever we start running our application
#so that we migrate the database and ensure that everything is set-up

sleep 10
python3 manage.py makemigrations
python3 manage.py migrate #we are migrating just that if we make any changes to the database that 
#automatically be applied. And when we do any new deployment the db we are connecting to will have those
#tabele created

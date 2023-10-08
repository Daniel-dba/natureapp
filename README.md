# natureapp

comandos para ejecutar:

py -m venv venv

.\venv\Scripts\activate	

pip install django

pip install djangorestframework

pip install drf-yasg

pip freeze > requirements.txt

django-admin startproject natureapp

cd natureapp

git init

python manage.py makemigrations     
python manage.py migrate
///migraciones

python manage.py createsuperuser

Usiario: admin

Direccion de correo electronico: admin@demo.org

Contraseña: 1234

web browser----	  
administrador de Django:   http://127.0.0.1:8000/admin

django REST Framework:   http://127.0.0.1:8000/inventario

Swagger: http://127.0.0.1:8000/apidoc/
			              

python manage.py shell 
// Comando para usar la consola interectiva

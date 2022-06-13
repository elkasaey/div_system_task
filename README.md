# Docker build & Run project
  * docker-compose up --build -d

# Migrate databases
 * docker exec -it django sh
 * python manage.py makemigrations
 * python manage.py Migrate

# Create User
 * http://localhost:8000/api/v1/user/create POST
 * body request is form-data
    Example:
    first_name:m
    last_name:k
    country_code:US
    gender:male
    birthdate:1997-01-01
    phone_number:+201000000000
    password:123456789
    email:mk@gmial.com

# Login User
  * http://localhost:8000/api/v1/user/login POST
  * body request is json
    Example {
          "phone_number":"+201000000000",
          "password":"123456789"
    }  
# Get all User with Auth
  * http://localhost:8000/api/v1/user GET
  * header request Bearer token

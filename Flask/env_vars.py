import os

SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

print(SECRET_KEY)
print(SQLALCHEMY_DATABASE_URI)
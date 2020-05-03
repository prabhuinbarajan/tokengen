import os

user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
host = os.environ['DB_HOST']
database = os.environ['MYSQL_DATABASE']
port = os.environ['MYSQL_PORT']

DATABASE_CONNECTION_URI = f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}'
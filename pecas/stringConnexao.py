import os
from dotenv import load_dotenv
load_dotenv()


def strSqlServer():
     server = os.environ.get('SQL_SERVER')
     database = os.environ.get('SQL_DATABASE')
     username = os.environ.get('SQL_USERNAME')
     password = os.environ.get('SQL_PASSWORD')
     driver = os.environ.get('SQL_DRIVER')
     return 'DRIVER={'+driver+'};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password +';TrustServerCertificate=Yes'





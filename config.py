import urllib
import pyodbc
import os
from urllib.parse import quote_plus
from urllib import parse
from dotenv import load_dotenv
from os import path

load_dotenv()
driver = os.getenv('driver')
server = os.getenv('Server')
database = os.getenv('Database')
usuario = os.getenv('UID')
password = os.getenv('PWD')
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))



#basedir = os.path.abspath(os.path.dirname(__file__))


UPLOADFOLDER = join_path = os.path.join(
            os.path.abspath(os.path.join(
                os.path.dirname(__file__)
                , os.path.pardir)))

print(UPLOADFOLDER,'uploadfolder')

TEMPLATE_FOLDER = os.path.abspath(os.path.dirname(__file__))



paramsdev = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};"

                                 "SERVER={server};"
                                 "DATABASE={database};"
                                 "UID={usuario};"
                                 "PWD={password}")

params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};"
                                 "SERVER={server};"
                                 "DATABASE={database};"
                                 "UID={usuario};"
                                 "PWD={password}")



SQLALCHEMY_DATABASE_URI= ("mssql+pyodbc:///?odbc_connect=%s" % params)


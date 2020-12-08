import psycopg2
from psycopg2 import errors
from model import * 
from view import *
import sys


def request():
    input_command = comand_identification()

    if(input_command=='1'):
        table_name = table()
        column_name = column()
        updt(table_name,column_name)
    elif(input_command=='2'):
        table_name = table()
        add_inf(table_name)
    elif(input_command=='3'):
        table_name = table()
        column_name = column()
        delete(table_name,column_name,Data())
    elif(input_command=='4'):
        table_name = table()
        random(table_name,Data())
    elif(input_command=='5'):
        Search()
    elif(input_command != '5'or'4'or'3'or'2'or'1'):
        comndErr()
        sys.exit()
        
    
    
menu()  

request()

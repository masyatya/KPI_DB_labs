import psycopg2
from psycopg2 import errors
import time
import sys
from view import *

def colmn_info(table_name,column_name):
	con = psycopg2.connect(
  	  database="MyData", 
  	  user="postgres", 
  	  password="", 
      host="localhost", 
  	  port="5432"
	)
	con.set_session(autocommit=True)
	curso_r=con.cursor()
	try:
		curso_r.execute(f"SELECT {column_name} FROM {table_name}")
		print(curso_r.fetchall())
	except psycopg2.Error as err:
		print(err.pgcode)
		print(f'WARNING:Error {err}')
	
	curso_r.close()
	con.close()

def random(table_name,n):
	con = psycopg2.connect(
  	  database="MyData", 
  	  user="postgres", 
  	  password="", 
      host="localhost", 
  	  port="5432"
	)
	con.set_session(autocommit=True)
	curso_r=con.cursor()
	if(table_name=='book'):
		try:	
			curso_r.execute(f"INSERT INTO book SELECT chr(trunc(65+random()*25)::int),chr(trunc(65 + random()*25)::int) FROM generate_series(1,{n})")
		except psycopg2.Error as err:
			print(err.pgcode)
			print(f'WARNING:Error {err}')

	elif(table_name=='book_fund'):
		try:
			curso_r.execute(f"WITH table_m AS(INSERT INTO book_fund SELECT trunc(random()*1000)::int, trunc(random()*1000)::int FROM generate_series(1,{n}) RETURNING id_of_librarian)INSERT INTO librarian SELECT id_of_librarian FROM table_m")
		except psycopg2.Error as err:
			print(err.pgcode)
			print(f'WARNING:Error {err}')

	elif(table_name=='librarian'):
		try:	
			curso_r.execute(f"WITH table_m AS(INSERT INTO librarian SELECT trunc(random()*1000)::int, chr(trunc(65+random()*25)::int), trunc(random()*1000)::int FROM generate_series(1,{n}) RETURNING id_of_librarian)INSERT INTO book_fund SELECT id_of_librarian FROM table_m")
		except psycopg2.Error as err:
			print(err.pgcode)
			print(f'WARNING:Error {err}')

	else:
		try:	
			curso_r.execute(f"INSERT INTO reader SELECT trunc(random()*1000)::int, chr(trunc(65+random()*25)::int) FROM generate_series(1,{n}) ")
		except psycopg2.Error as err:
			print(err.pgcode)
			print(f'WARNING:Error {err}')

	curso_r.close()
	con.close()

def delete(table_name,column,row):
	con = psycopg2.connect(
  	  database="MyData", 
  	  user="postgres", 
  	  password="", 
      host="localhost", 
  	  port="5432"
	) 
	
	con.set_session(autocommit=True)
	curso_r=con.cursor()
	
	colmn_info(table_name,column)
	if(table_name=='book'):
		try:
			curso_r.execute(f"delete FROM book WHERE {column} = '{row}'")
		except psycopg2.Error as err:
			print(err.pgcode)
			print(f'WARNING:Error {err}')
	elif(table_name=='book_fund'):
		try:
			curso_r.execute(f"WITH test AS(delete FROM book_fund WHERE {column}  = '{row} ')delete FROM librarian WHERE id_of_librarian = '{row}'")
		except psycopg2.Error as err:
			print(err.pgcode)
			print(f'WARNING:Error {err}')
	elif(table_name=='librarian'):
		try:
			curso_r.execute(f"WITH test AS(delete FROM librarian WHERE {column} = '{row}')delete FROM book_fund WHERE id_of_librarian = '{row}'")
		except psycopg2.Error as err:
			print(err.pgcode)
			print(f'WARNING:Error {err}')
	else:
		try:
			curso_r.execute(f"delete FROM reader WHERE {column} = '{row}'")
		except psycopg2.Error as err:
			print(err.pgcode)
			print(f'WARNING:Error {err}')

	curso_r.close()
	con.close()

def add_inf(table_name):
	con = psycopg2.connect(
  	  database="MyData", 
  	  user="postgres", 
  	  password="", 
      host="localhost", 
  	  port="5432"
	) 
	con.set_session(autocommit=True)
	curso_r=con.cursor()
	count=0
	mass=[]
	if(table_name=='librarian'):
		print("Enter 3 value :")
		while(count<3):
			value=input()
			mass.append(value)
			count+=1
		table_name2 = 'book_fund'
		try:
			curso_r.execute(f"WITH {table_name} AS ( INSERT INTO {table_name} VALUES ('{mass[0]} ','{mass[1]}','{mass[2]}')) INSERT INTO {table_name2} VALUES ('{mass[0]}')")
		except psycopg2.Error as err:
			print(err.pgcode)
			print(f'WARNING:Error {err}')
	elif(table_name == 'book_fund'):
		print("Enter 2 value :")
		while(count<2):
			value=input()
			mass.append(value)
			count+=1
		table_name2 = 'librarian'
		try:
			curso_r.execute(f"WITH {table_name} AS ( INSERT INTO {table_name} VALUES ('{mass[0]}','{mass[1]}')) INSERT INTO {table_name2} VALUES ('{mass[0]}')")
		except psycopg2.Error as err:
			print(err.pgcode)
			print(f'WARNING:Error {err}')
	elif(table_name == 'book'): 
		print("Enter 2 value :")
		while(count<2):
			value=input()
			mass.append(value)
			count+=1
		try:
			curso_r.execute(f"INSERT INTO {table_name} VALUES ('{mass[0]}','{mass[1]}')")  
		except psycopg2.Error as err:
			print(err.pgcode)
			print(f'WARNING:Error {err}')
	else:
		print("Enter 2 value :")
		while(count<2):
			key=input()
			mass.append(key)
			count+=1
		try:
			curso_r.execute(f"INSERT INTO {table_name} VALUES ('{mass[0]}','{mass[1]}')")
		except psycopg2.Error as err:
			print(err.pgcode)
			print(f'WARNING:Error {err}')
	curso_r.close()
	con.close()

def dbl_upd(name1,name2,column,old_value,new_value):
	con = psycopg2.connect(
  	  database="MyData", 
  	  user="postgres", 
  	  password="", 
      host="localhost", 
  	  port="5432"
	) 
	con.set_session(autocommit=True)
	curso_r=con.cursor()
	try:
		curso_r.execute(f"WITH {name1} AS (UPDATE {name1} SET {column} = '{new_value}' WHERE {column} = '{old_value}') UPDATE {name2} SET {column} = '{new_value}' WHERE {column} = '{old_value}'")
	except psycopg2.Error as err:
		print(err.pgcode)
		print(f'WARNING:Error {err}')
	curso_r.close()
	con.close()

def solo_upd(name1,column,old_name,new_name):
	con = psycopg2.connect(
  	  database="MyData", 
  	  user="postgres", 
  	  password="", 
      host="localhost", 
  	  port="5432"
	) 
	con.set_session(autocommit=True)
	curso_r=con.cursor()
	try:
		curso_r.execute(f"UPDATE {name1} SET {column} =  '{new_name}' WHERE {column} = '{old_name}'")
	except psycopg2.Error as err:
		print(err.pgcode)
		print(f'WARNING:Error {err}')
	curso_r.close()
	con.close()

def updt(table_name,column_name):
	con = psycopg2.connect(
  	  database="MyData", 
  	  user="postgres", 
  	  password="", 
      host="localhost", 
  	  port="5432"
	) 
	con.set_session(autocommit=True)
	curso_r=con.cursor()
	colmn_info(table_name,column_name)
	if(((table_name=='book_fund')or(table_name=='librarian'))and(column_name=='id_of_librarian')):
		try:
			dbl_upd('book_fund','librarian','id_of_librarian',OldData(),NewData())
		except psycopg2.Error as err:
			print(err.pgcode)
			print(f'ERROR: {err}')
	else:
		try:
			solo_upd(table_name,column_name,OldData(),NewData())
		except psycopg2.Error as err:
			print(err.pgcode)
			print(f'ERROR: {err}')
	curso_r.close()
	con.close()

def Search():
	con = psycopg2.connect(
  	  database="MyData", 
  	  user="postgres", 
  	  password="", 
      host="localhost", 
  	  port="5432"
	) 
	con.set_session(autocommit=True)
	curso_r=con.cursor()
	n = input("Input quantity of attributes to search by >>> ")
	n = int(n)
	column=[]
	for h in range(0,n):
		column.append(str(input(f"Input name of the attribute number {h+1} to search by >>> ")))
	print(column)
	tables = []
	types = [] 
	if n == 2:
		curso_names_str = f"SELECT table_name FROM INFORMATION_SCHEMA.COLUMNS WHERE information_schema.columns.column_name LIKE '{column[0]}' INTERSECT ALL SELECT table_name FROM information_schema.columns WHERE information_schema.columns.column_name LIKE '{column[1]}'"
	else:
		curso_names_str = "SELECT table_name FROM INFORMATION_SCHEMA.COLUMNS WHERE information_schema.columns.column_name LIKE '{}'".format(column[0])
	print("\ncol_names_str:", curso_names_str)
	curso_r.execute(curso_names_str)
	curso_names = (curso_r.fetchall())
	for tup in curso_names:
		tables += [tup[0]]
	for s in range(0,len(column)):
		for k in range(0,len(tables)):
			curso_r.execute(f"SELECT data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name='{tables[k]}' AND column_name ='{column[s]}'")
			type=(curso_r.fetchall())
			for j in type:
				types+=[j[0]]
	print(types)
	if n == 1:
		if len(tables) == 1:
			if types[0] == 'character varying':
				i_char = input(f"Input string for {column[0]} to search by >>> ")
				start_time=time.time()
				curso_r.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]} LIKE '{i_char}'")
				print(curso_r.fetchall())
				print("Time:%s seconds"%(time.time()-start_time))
			elif types[0] == 'integer':
				left_limits = input("Enter left limit")
				right_limits = input("Enter right limit")
				start_time=time.time()
				curso_r.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]}>='{left_limits}' AND {column[0]}<'{right_limits}'")
				print(curso_r.fetchall())
				print("Time:%s seconds"%(time.time()-start_time))

		elif len(tables) == 2:
			if types[0] == 'integer':
				left_limits = input("Enter left limit")
				right_limits = input("Enter right limit")
				start_time=time.time()
				curso_r.execute(f"SELECT {column[0]} FROM {tables[0]} WHERE {column[0]}>='{left_limits}' AND {column[0]}<'{right_limits}' UNION ALL SELECT {column[0]} FROM {tables[1]} WHERE {column[0]}>='{left_limits}' AND {column[0]}<'{right_limits}'")
				print(curso_r.fetchall())
				print("Time:%s seconds" % (time.time() - start_time))

	elif n == 2:
		if len(tables) == 1:
			if types[0] == 'character varying' and types[1] == 'character varying':
				i_char = input(f"Input string for {column[0]} to search by >>> ")
				o_char = input(f"Input string for {column[1]} to search by >>> ")
				start_time = time.time()
				curso_r.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]} LIKE '{i_char}' AND {column[1]} LIKE '{o_char}' ")
				print(curso_r.fetchall())
				print("Time:%s seconds" % (time.time() - start_time))
			elif types[0] == 'integer' and types[1] == 'integer':
				i_left_limits = input(f"Enter left limit for {column[0]}")
				i_right_limits = input(f"Enter right limit for {column[0]}")
				o_left_limits = input(f"Enter left limit for {column[1]}")
				o_right_limits = input(f"Enter right limit for {column[1]}")
				start_time = time.time()
				curso_r.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]}>='{i_left_limits}' AND {column[0]}<'{i_right_limits}' AND {column[1]}>='{o_left_limits}' AND {column[1]}<'{o_right_limits}' ")
				print(curso_r.fetchall())
				print("Time:%s seconds" % (time.time() - start_time))
			elif types[0] == 'integer' and types[1] == 'character varying':
				i_left_limits = input(f"Enter left limit for {column[0]}")
				i_right_limits = input(f"Enter right limit for {column[0]}")
				o_char = input(f"Input string for {column[1]} to search by >>> ")
				start_time = time.time()
				curso_r.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]}>='{i_left_limits}' AND {column[0]}<'{i_right_limits}' AND {column[1]} LIKE '{o_char}' ")
				print(curso_r.fetchall())
				print("Time:%s seconds" % (time.time() - start_time))
			elif types[0] == 'character varying' and types[1] == 'integer':
				i_char = input(f"Input string for {column[0]} to search by >>> ")
				o_left_limits = input(f"Enter left limit for {column[1]}")
				o_right_limits = input(f"Enter right limit for {column[1]}")
				start_time = time.time()
				curso_r.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]} LIKE '{i_char}' AND {column[1]}>='{o_left_limits}' AND {column[1]}<'{o_right_limits}' ")
				print(curso_r.fetchall())
				print("Time:%s seconds" % (time.time() - start_time))
	curso_r.close()
	con.close()





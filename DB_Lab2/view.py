import sys

def comndErr():
	print("You have to enter the command from 1 to 5 ERROR")


def comand_identification():
	return input('Enter command : ')
def table():
	print('Your table name: book , librarian , book_fund , reader ')
	return input('Enter table name ')

def column():
    return input('Enter column name ')

def OldData():
    return input('Enter old value ')

def NewData():
    return input('Enter new value ')
def Data():
    return input('Enter value: ')
def row():
	return int(input('Enter value: '))

def tablevalid():
	print('The table name is wrong ERROR')
	sys.exit()    

def menu():
    print("Update press 1")
    print("Add press 2")
    print("Delete press 3")
    print("Random press 4")
    print("Search press 5")
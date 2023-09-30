from file import *

def menu():
	print('[1] Add')
	print('[2] Remove')
	print('[3] Promote')
	print('[4] Display')
	print('[0] Exit')

menu()
choise = int(input('Enter option: '))
print()
while choise != 0:
	if choise == 1:
		name = input('Enter the name of the employee: ')
		department = input('Enter the name of the department: ')
		salary = input('Enter the salary of the employee: ')
		if department == 'sde':
			p1=sde(name,salary)
		elif department == 'backend':
			p1=backend(name,salary)
		elif department == 'frontend':
			p1=frontend(name,salary)
		else:
			print("\nError: such department do not not exist\nplease try again")
		
	elif choise == 2:
		name = input('Enter the name of the employee to remove: ')
		remove(name)



	elif choise == 3:
		name = input('Enter the name of the employee: ')
		department = input('Enter the name of the New department: ')
		salary = input('Enter the New salary of the employee: ')
		promote(name,department,salary)
	
	elif choise == 4:
		display()

	else:
		print('error in loop')
	
	print()
	menu()	
	choise = int(input('Enter option: '))
	print()

else:
	print('You have succesfully existed')

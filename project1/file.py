class sde:
    def __init__(self,name,salary,):
        self.name=name
        self.salary=salary
        department="SDE"
        try:
            add(name,department,salary,)
        except:
            print('\nError: updation in unsuccessfull')
                    
        
class frontend:
    
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        department="FrontEnd"
        try:
            add(name,department,salary)
        except:
            print('\nError: updation in unsuccessfull')

class backend:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        department="BackEnd"
        try:
            add(name,department,salary)
        except:
            print('\nError: updation in unsuccessfull')
    
def add(name,deptartment,salary):
    value1=name
    value2=deptartment
    value3=salary
    result=f"Name = {value1} Department = {value2} Salary = {value3}"
    with open('data.txt','a') as file:
        file.write(result+'\n')
        print('\nEmployee is added successfully')
        
def remove(name):
    with open('data.txt','r') as file:
        lines=file.read()
        if name in lines:
            with open("data.txt",'r') as file:
                lines = file.readlines()

            with open("data.txt",'w') as file:
                for line in lines:
        
                    if line.find(name) != -1:
                        pass
                    else:
                        file.write(line)
            print('\nEmployee is removed successfully')
        else:
            print('\nError: Such employee does not exist')

def promote(name,deptartment,salary):
    value1=name
    value2=deptartment
    value3=salary
    new=f"Name = {value1} Department = {value2} Salary = {value3}"
    with open ('data.txt','r') as file:
        for line in file:
            if value1 in line :
                line2 = line
                print(line2)
            
    with open('data.txt','r') as file:
        filedata=file.read()
        if value1 in filedata:
            data = line2
            filedata=filedata.replace(data,new)
            with open ('data.txt','w') as file:
                file.write(filedata+'\n')
                print('\nData updated successfully')
        else:
            print('\nError: Such employee does not exist')


def display():
    print('All the Employee present:-')
    with open('data.txt','r') as file:
        for line in file:
            print(line,end='')
    
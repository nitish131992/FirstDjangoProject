# Creating classes and object

class Employee:
	'common base class'
	empcount = 0;
	
	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
		Employee.empcount += 1
	
	def displaycount(self):
		print("total employee : ",Employee.empcount)
	
	def displayEmployee(self):
		print(self.name , self.salary)

emp1 = Employee("pk",2000)
emp2 = Employee("tk",4500)

emp1.displayEmployee()
emp1.displaycount()
emp2.displayEmployee()
print(Employee.empcount)

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)

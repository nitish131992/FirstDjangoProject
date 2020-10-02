# class inheritence
class Parent:
	parent_att = 10;
	def __init__(self):
		print("calling parent constructor")
	
	def parentmethod(self):
		print("calling parent method")
		
	def setattr(self,att):
		Parent.parent_att = att
	
	def getatt(self):
		print(Parent.parent_att)
		
	def mymethod(self):
		print("This is parent mymethod , no method overriding")

class Child(Parent): # defining parent class
	def __init__(self):
		print("calling child constructor")
		
	def childmethod(self):
		print("calling child method")
		
	def mymethod(self):
		print("This is child mymethod , so method overriding")


p = Parent()
c = Child()
print(p.parent_att)
c.childmethod()
c.parentmethod
print(c.parent_att)
c.setattr(200)
c.getatt()

print(p.parent_att)
p.mymethod()
c.mymethod()

	
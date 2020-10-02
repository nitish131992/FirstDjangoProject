# funtions
def printme(a):
    a.append([4,5,6])
    print(a)
	
b = [1,2,3]
printme(b)	  #calling function
printme(b)
print(b)

def callme(a,b=25): #default value
    print(a)
    print(b)
	
callme("tika",30)
callme("ramu")	

def info(arg,*vartuple): # variable length argument
	print(arg)
	for var in vartuple:
	    print(var)

info(10)
info(10,20,30,40)

sum = lambda p,q:p+q   # anomymous
print(sum(100,200))

def mul(a,b):
	total = a * b
	return total;

p = mul(20,30)
print(p)



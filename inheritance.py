#Single level inheritance

print('Single level Inheritance')

class A:
    def fariq(self):
        rollno=7084593
        marks=584
        print(rollno,marks)

class B(A):
    def buvanesh(self):
        rollno=7084588
        marks=503
        print(rollno,marks)
        
b=B()

b.buvanesh()
b.fariq()

print(end="\n")

#Multilevel inheritance

print('Multilevel Inheritance')

class A1:
    def fariq(self):
        rollno=7084593
        marks=584
        print(rollno,marks)

class A2(A1):
    def buvanesh(self):
        rollno=7084588
        marks=503
        print(rollno,marks)
        
class A3(A2):
    def mayish(self):
        rollno=7084593
        marks=584
        print(rollno,marks)

a3 = A3()

a3.fariq()     
a3.buvanesh()
a3.mayish()

print(end="\n")

#Multiple inheritance

print('Multiple Inheritance')

class a:
    def fariq(self):
        rollno=7084593
        marks=584
        print(rollno,marks)

class b:
    def buvanesh(self):
        rollno=7084588
        marks=503
        print(rollno,marks)
        
class c(a,b):
    def mayish(self):
        rollno=7084593
        marks=584
        print(rollno,marks)

c1= c()

c1.fariq()    
c1.buvanesh()

print(end="\n")

#Hierarchical inheritance

print('Hierarchical Inheritance')

class a1:
    def fariq(self):
        rollno=7084593
        marks=584
        print(rollno,marks)

class b1(a1):
    def buvanesh(self):
        rollno=7084588
        marks=503
        print(rollno,marks)
        
class c1(a1):
    def mayish(self):
        rollno=7084593
        marks=584
        print(rollno,marks)

b11=b1()
c11=c1()

b11.fariq()
c11.fariq()








#Single level inheritance

print('Single level Inheritance')

class A:
    def student1(self):
        rollno=7084593
        marks=584
        print(rollno,marks)

class B(A):
    def student2(self):
        rollno=7084588
        marks=503
        print(rollno,marks)
        
b=B()

b.student1()

print(end="\n")

#Multilevel inheritance

print('Multilevel Inheritance')

class A1:
    def student1(self):
        rollno=7084593
        marks=584
        print(rollno,marks)

class A2(A1):
    def student2(self):
        rollno=7084588
        marks=503
        print(rollno,marks)
        
class A3(A2):
    def student3(self):
        rollno=7084593
        marks=584
        print(rollno,marks)

a3 = A3()

a3.student1()     
a3.student2()
a3.student3()

print(end="\n")

#Multiple inheritance

print('Multiple Inheritance')

class a:
    def student1(self):
        rollno=7084593
        marks=584
        print(rollno,marks)

class b:
    def student2(self):
        rollno=7084588
        marks=503
        print(rollno,marks)
        
class c(a,b):
    def student3(self):
        rollno=7084593
        marks=584
        print(rollno,marks)

c1= c()

c1.student1()    
c1.student2()

print(end="\n")

#Hierarchical inheritance

print('Hierarchical Inheritance')

class a1:
    def student1(self):
        rollno=7084593
        marks=584
        print(rollno,marks)

class b1(a1):
    def student2(self):
        rollno=7084588
        marks=503
        print(rollno,marks)
        
class c1(a1):
    def student3(self):
        rollno=7084593
        marks=584
        print(rollno,marks)

b11=b1()
c11=c1()

b11.student1()
c11.student1()








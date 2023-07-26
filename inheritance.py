class fariq:
    def __init__(self,rollno,marks):
        self.rollno=rollno
        self.marks=marks
        print(rollno,marks)

class buvanesh(fariq):
    def __init__(self,rollno,marks):
        self.rollno=rollno
        self.marks=marks
        print(rollno,marks)

class mayish(buvanesh):
    def __init__(self,rollno,marks):
        self.rollno=rollno
        self.marks=marks
        print(rollno,marks)

object1= fariq(7084593,584)
object2= buvanesh(7084589,503)
object3= mayish(7084594,488)

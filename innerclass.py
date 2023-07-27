class student: #main class
    def __init__(self):
        Name='Fariq'
        Rollno=7084593
        
        print(Name)
        print(Rollno)
        
    class performance: #inner class
        def __init__(self):
            print("Good")
            
a=student()           
b=student.performance()

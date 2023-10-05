from numpy import *

matrix=array([[1,3,7],[5,6,9],[8,2,0]])
print(matrix)

to_find=int(input("Enter an element : "))
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if(to_find==matrix[i][j]):
            print("Row : ",i+1)
            print("Coloumn : ",j+1)
            break

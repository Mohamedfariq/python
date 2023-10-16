def calculator(operator):
    value1=int(input("Enter the value 1 :"))
    value2=int(input("Enter the value 2 :"))
    list1=["addition","subtraction","multiplication","division"]
    if operator==list1[0]:
        print(value1+value2)
    if operator==list1[1]:
        print(value1-value2)
    if operator==list1[2]:
        print(value1*value2)
    if operator==list1[3]:
        print(value1/value2)
calculator("addition")

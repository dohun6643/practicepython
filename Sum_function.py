# first, second = input("input two Number ?").split(',')
# print(int(first) + int(second))

#---------------------------------------함수
def sum(first, second):
    num1 = int(first)
    num2 = int(second)
    result = num1 + num2

    print("inside the function",int(first) +int(second))
    return num1, num2, result

#---------------------------------------

first, second =(24,14)      #input("input two Number ?").split(',')
r1, r2, r3 = sum(first, second)
print(r1,r2,r3)
# def sub(first, second):
#     print("inside the function",int(first) - int(second))
#     return

# first, second = input("input two Number ?").split(',')
# sub(first, second)


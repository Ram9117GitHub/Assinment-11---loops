"""Write a python script to calculate factorial of a given number"""
print("-----------------------------------------------------------------------------------------------------------------")
num = int(input("Enter a number :"))
fac = 1
i = 1
for i in range(1,num+1):
    fac = fac*i
print("The factorial number =",fac)
print("----------------------------------------------------------------------------------------------------------------")
num = int(input("Enter a number :"))
fac =1
i = 1
while i<= num:
    fac = fac*i
    i+=1
print("The factorial number =", num)
print("----------------------------------------------------------------------------------------------------------------")

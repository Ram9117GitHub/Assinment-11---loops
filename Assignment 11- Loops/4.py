"""Write a python script to calculate sum of first N odd natural numbers"""
print("----------------------------------------------------------------------------------------------------------------")
num = int(input("Enter a Natural number :"))
sum = 0
i = 1
for i in range(1,num+1):
    if i % 2 !=0:
        sum = sum+i
print("The sum of odd numbers is ",sum)
print("----------------------------------------------------------------------------------------------------------------")

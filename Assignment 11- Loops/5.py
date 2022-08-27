"""Write a python script to calculate sum of first N even natural numbers"""
num = int(input("Enter a Natural number :"))
sum = 0
i = 2
for i in range(1,num+1):
    if i % 2 ==0:
        sum = sum+i
print(sum)


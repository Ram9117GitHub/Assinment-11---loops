""" Write a python script to calculate sum of squares of first N natural numbers """
print("---------------------------------------------------------------------------------------------------------------")
num = int(input("Enter a Natural number :"))
sum = 0
while num>0:
    r = num**2
    sum +=r
    num-=1
print("The sum of squares is ",sum)
print("----------------------------------------------------------------------------------------------------------------")
num = int(input("Enter a Natural number :"))
sum = 0
for i in range(1,num+1):
    r = i**2
    sum += r
print("The sum of squares is ",sum)
print("----------------------------------------------------------------------------------------------------------------")

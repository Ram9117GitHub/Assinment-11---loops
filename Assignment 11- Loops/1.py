""" Write a python script to calculate sum of first N natural numbers """
print("----------------------------------------------------------------------------------------------------------------")
num = int(input("Enter a Natural numbers:"))
sum = 0
while num > 0:
    sum+=num
    num-=1
print("The sum is ", sum)
print("----------------------------------------------------------------------------------------------------------------")
num = int(input("Enter a Natural number :"))
sum = 0
for i in range(1,num+1):
    sum = sum +i
print("The sum is ",sum)
print("---------------------------------------------------------------------------------------------------------------")
num = int(input("Enter a Natural Number :"))
sum = num*(num+1)/2
print("The sum is ", sum)
print("---------------------------------------------------------------------------------------------------------------")

"""Write a python script to calculate sum of cubes of first N natural numbers"""
print("---------------------------------------------------------------------------------------------------------------")
num = int(input("Enter a Natural number :"))
sum = 0
while num >0:
    cub = num**3
    sum +=cub
    num-=1
print("The sum of cubes is ",sum)
print("----------------------------------------------------------------------------------------------------------------")
num = int(input('Enter a natural number :'))
sum =0
for i in range(1,num+1):
    cub = i**3
    sum +=cub
print("The sum of cubes is ",sum)
print("----------------------------------------------------------------------------------------------------------------")

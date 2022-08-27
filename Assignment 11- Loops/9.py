"""Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)"""
num = 6
while num >= 1:
    num = num//2
    print(num % 2, end='')
num+=1
"""""""""""""""""""""""""""output"""""""""
"""
110
"""


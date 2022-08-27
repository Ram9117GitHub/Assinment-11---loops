"""Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)"""
num = 13
q=num
octal=0
i=0
while q!=0:
    rem = q%8
    octal = octal + rem * (10**i)
    q = q // 8
    i+=1
print('Octal Number=', octal)
"""""""""""""""""""""""""""""""""""Output"""""""""""""""
"""
Octal Number= 15
"""
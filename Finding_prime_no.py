#This function returns a new list which is a sub-list
#and it only contains prime numbers

import math
def check_prime(n:int):
    count=0
    m=int(math.sqrt(n))
    for i in range(1,m+1):
        if(n%i==0):
            count += 1
    if(count==1 and n!=1):
        return True
    else:
        return False
    
def finding_prime_no(a:list):
    lst=[]
    for i in a:
        if(check_prime(i)):
            lst.append(i)
    return lst

list1=[i*2+3 for i in range(16)]
prime_list1=finding_prime_no(list1)
list2=[i for i in range(100)]
prime_list2=finding_prime_no(list2)
print(prime_list1)
print(len(prime_list1))
print(prime_list2)
print(len(prime_list2))
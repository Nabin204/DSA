#This function returns a new list which is a sub-list
#and it only contains square numbers

import math
def finding_sq_no(a:list):
    lst=[]
    for i in a:
        p=math.sqrt(i)
        q=int(p)
        if(p==q):
            lst.append(i)
    return lst

list1=[i*2+3 for i in range(16)]
square_list1=finding_sq_no(list1)
list2=[0,1.000000000001,1,4.0,8,999,323,243,729,12345654321,90]
square_list2=finding_sq_no(list2)
print(square_list1)
print(square_list2)
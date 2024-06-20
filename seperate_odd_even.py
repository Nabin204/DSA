def seperate_odd_even(l:list):
    even_lst=[]
    odd_lst=[]
    for i in l:
        if(i%2==0):
            even_lst.append(i)
        else:
            odd_lst.append(i)
    result=[even_lst,odd_lst]
    return result

list1=[6,4,9,0,1,3,5,8,12,34,71,84,90,34,3443]
list2=[i*3+1 for i in range(40)]

result1=seperate_odd_even(list1)
even_lst1=result1[0]
odd_lst1=result1[1]
print("Even list:",even_lst1)
print("Odd list:",odd_lst1)

result2=seperate_odd_even(list2)
even_lst2=result2[0]
odd_lst2=result2[1]
print("Even list:",even_lst2)
print("Odd list:",odd_lst2)
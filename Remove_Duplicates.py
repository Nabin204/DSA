# First Method
def remove_duplicates(a:list):
    return list(set(a))

# Second Method
def Remove_Duplicates(a:list):
    lst1=[]
    for i in a:
        if(i not in lst1):
            lst1.append(i)
    return lst1

list1=[1,3,2,5,4,0,3,5,8,2,3,1,4]
list2=remove_duplicates(list1)
list3=Remove_Duplicates(list1)
print(list2)
print(list3)
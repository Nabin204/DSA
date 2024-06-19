#Case1:If repeated element are counted more than once
def Kth_smallest_element(a:list,b:int):
    a.sort()
    kth_smallest_element=a[b-1]
    return kth_smallest_element

#Case1:If repeated element are counted only once
def Kth_Smallest_Element(a:list,b:int):
    a=list(set(a))
    a.sort()
    kth_smallest_element=a[b-1]
    return kth_smallest_element

list1=[1,2,3,4,5,8,9,11,67,1]
k1=3
list2=[8,0,5,11,45,23,32,54,31,78,65,72,73,74,55,47]
k2=5
print(Kth_smallest_element(list1,k1))
print(Kth_Smallest_Element(list1,k1))
print(Kth_smallest_element(list2,k2))
print(Kth_Smallest_Element(list2,k2))
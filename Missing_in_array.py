#Given an array of size n-1 such that it only contains distinct integers in the range of 1 to n. 
# Return the missing element.
def Missing_in_array(a:list,n:int):
    sum1=sum(a)
    sum2=n*(n+1)/2
    result=int(sum2-sum1)
    return result

list1=[1,4,2,7,3,5]
n1=7
print(Missing_in_array(list1,n1))
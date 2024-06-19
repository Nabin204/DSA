# First Method
def most_repeated(a:list):
    count=0
    for i in a:
        temp=a.count(i)
        if(temp>count):
            count=temp
            num=i
    print("The most repeated element is",num,f"which is repeated {count} times.")

# Second Method
import statistics
def Most_Repeated(a:list):
    result=statistics.mode(a)
    frequency=a.count(result)
    print("The most repeated element is",result,f"which is repeated {frequency} times.")

list1=[1,2,54,3,6,8,3,1,5,8,9,7,2,1,2,3,9,3]
most_repeated(list1)
Most_Repeated(list1)

#Note:If there are two most repeated elements in a list then the given functions prints the value that comes first in list
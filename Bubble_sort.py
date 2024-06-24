#Bubble Sort Algorithm 
def bubble_sort(arr):
    l=len(arr)
    for i in range(l):
        for j in range(0,l-1-i):
            if(arr[j]>arr[j+1]):
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
    return arr

a=[4,3,2,1,0,-1,-2,-3,0,0,1,2]
b=bubble_sort(a)
print(b)
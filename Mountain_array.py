'''Recall that arr is a mountain array if and only if:

1)arr.length >= 3
2)There exists some i with 0 < i < arr.length - 1 such that:
3)arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
4)arr[i] > arr[i + 1] > ... > arr[arr.length - 1] '''

def validMountainArray(arr: list[int]) -> bool:
    l=len(arr)
    if(l<3):
        return False
    else:
        p=q=0
        for i in range(l-1):
            if(arr[i+1]<=arr[i]):
                p=i
                break
        for j in range(p,l-1):
            if(arr[j+1]>=arr[j]):
                   q=j
                   break
        if(q==0 and p!=0):
            return True
        else:
            return False
lst = [1,2,3,4,5,4,3,2,1]
if(validMountainArray(lst)):
    print(True)
else:
    print(False)

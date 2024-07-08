def findMaxAverage(nums: list[int], k: int) -> float:
    l=len(nums)
    sum1=sum(nums[0:k])
    if(l==k):
        return sum(nums)/k
    else:
        for i in range(l-k+1):
            m=sum(nums[i:i+k])
            if(m>sum1):
                sum1=m
        return sum1/k

l=[6,7,1,-3,-5,3,5,9]
k=4
Max_average=findMaxAverage(l,k)
print(f"The maximum average of length {k} is {Max_average}.")
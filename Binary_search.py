def binary_search(nums : list[int],target : int):
    low = 0
    high = len(nums)-1
    while(low<=high):
        mid = low + (high-low)//2
        if(nums[mid]==target):
            return mid
        elif(nums[mid]<target):
            low = mid+1
        else:
            high = mid-1

#The array must be sorted in ascending order
list1=[-3,2,6,9,12,56,78,90,99]
target = 12
index=binary_search(list1,target)
print(f"The number {target} is located at index {index}.")
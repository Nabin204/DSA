# Method 1
def permutation(nums : list):
    l=len(nums)
    if(l==0):
        return []
    elif(l==1):
        return [nums]
    
    result=[]
    for i in range(l):
        m=nums[i]
        rem_list=nums[:i]+nums[i+1:l]
        for p in permutation(rem_list):
            result.append([m]+p)
    return result

lst = [1,2,3]
print(permutation(lst))

# Method 2
import itertools
print(list(itertools.permutations(lst)))
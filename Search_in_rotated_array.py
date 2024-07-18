#without using index() method search a number in a rotated array
def search(nums: list[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            if nums[l]==target:
                return l
            if nums[r]==target:
                return r
            if nums[mid]>=nums[l]:
                if nums[l]<target<nums[mid]:
                    l=l+1
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<target<nums[r]:
                    l=mid+1
                    r=r-1
                else:
                    r=mid-1
        return -1
a=[3,4,7,14,0,1,2]
target=2
print(f"Index of {target} is {search(a,target)}")
#You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

#Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b

def findMissingAndRepeatedValues(grid: list[list[int]]) -> list[int]:
        x=[]
        n=len(grid)
        l=n*n
        a=b=0
        for i in grid:
            for j in i:
                if(j in x):
                    a=j
                x.append(j)
        b = l*(l+1)//2-sum(list(set(x)))
        ret = [a,b]
        return ret
grid = [[1,3],[2,2]]
print(findMissingAndRepeatedValues(grid))
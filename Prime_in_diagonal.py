def diagonalPrime(nums: list[list[int]]) -> int:
        largest = 2
        def isprime(n):
            p=0
            for i in range(2,int(pow(n,0.5))+1):
                if(n%i==0):
                    p += 1
            if(p==0):
                return True
            else:
                return False
        l=len(nums)
        a=b=0
        for i in range(l):
            p=nums[i][i]
            q=nums[i][l-i-1]
            if(isprime(p) and p>=largest):
                a += 1
                largest = p
            if(isprime(q) and q>=largest):
                b += 1
                largest = q
        if(a==0 and b==0):
            return None
        else:
            return largest
list1 = [[2,645,309,559],[624,160,435,724],[770,483,95,695],[510,779,984,238]]
large1 = diagonalPrime(list1)
list2 = [[788,645,309,559],[624,160,435,724],[770,483,95,695],[510,779,984,238]]
large2 = diagonalPrime(list2)
print("The largest prime element in both diagonal is ",large1)
print("The largest prime element in both diagonal is ",large2)

#Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.

#Recall that the number of set bits an integer has is the number of 1's present when written in binary.

#For example, 21 written in binary is 10101, which has 3 set bits.

def countPrimeSetBits(left: int, right: int) -> int:
        primes = [2,3,5,7,11,13,17,19,23,29]
        count = 0
        for i in range(left,right+1):
            a = bin(i).replace("0b","")
            p=0
            for i in a:
                if(i=="1"):
                    p += 1
            if(p in primes):
                count += 1
        return count
print(countPrimeSetBits(4,12))
print(countPrimeSetBits(1,100))
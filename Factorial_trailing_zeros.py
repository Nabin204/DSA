# First count the number of twos(sum1) and fives(sum2) in the prime factorization 
# of n!.Then the minimum value of sum1 and sum2 is the number of trailing zeros
def trailingZeroes(n: int) -> int:
        two=n//2
        five=n//5
        sum1=sum2=0
        i=1
        while(two>=1):
            two=n//pow(2,i)
            i+=1
            sum1 += two
        i=1
        while(five>=1):
            five=n//pow(5,i)
            sum2 += five
            i+=1
        return min(sum1,sum2)
print("The number of trailing zeros in 26! =",trailingZeroes(26))
print("The number of trailing zeros in 50! =",trailingZeroes(50))
print("The number of trailing zeros in 4200! =",trailingZeroes(4200))
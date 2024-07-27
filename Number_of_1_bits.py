#Write a function that takes the binary representation of a positive integer and returns the number of 
#set bits
# it has (also known as the Hamming weight).

def hammingWeight(n: int) -> int:
        b = bin(n).replace("0b","")
        return b.count("1")
print(hammingWeight(4))
print(hammingWeight(127))
print(hammingWeight(1234))

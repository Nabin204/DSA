def mySqrt(x: int) -> int:
    for i in range(x+3):
        if(i*i>x):
            num=i
            break
    return (num-1)
num = int(input("Enter a number:"))
sqrt = mySqrt(num)
print("The integral part of square root is:",sqrt)
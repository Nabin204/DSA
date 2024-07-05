def roman_to_integer(s :str)->int:
    def roman(a):
        if(a == 'I'):
            x=1
        elif(a == 'V'):
            x=5
        elif(a == 'X'):
            x=10
        elif(a == 'L'):
            x=50
        elif(a == 'C'):
            x=100
        elif(a == 'D'):
            x=500
        elif(a == 'M'):
            x=1000
        return x
    l=len(s)
    b=[]
    for i in range(l):
        c=roman(s[l-i-1])
        b.append(c)
    sum=b[0]
    for i in range(l-1):
        if(b[i+1]>=b[i]):
            sum += b[i+1]
        else:
            sum -= b[i+1]
    return sum
roman = input("Enter the roman number:")
integer = roman_to_integer(roman.upper())
print(f"The corresponding integer is {integer}.")
def convertToBase7(num: int) -> str:
        x=""
        a=abs(num)
        while(a!=0):
            r=a%7
            x += str(r)
            a //=7
        l=len(x)
        if(num>0):
            return x[::-1]
        elif(num==0):
            return "0"
        else:
            y="-"+x[::-1]
            return y
print("-4500 in base 7 is equivalent to",convertToBase7(-4500))
print("1 in base 7 is equivalent to",convertToBase7(1))
print("9749319738 in base 7 is equivalent to",convertToBase7(9749319738))
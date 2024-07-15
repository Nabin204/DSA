#Given two non-negative integers, num1 and num2 represented as 
# string, return the sum of num1 and num2 as a string.
def addStrings(num1: str, num2: str) -> str:
        l1=len(num1)
        l2=len(num2)
        diff = abs(l1-l2)
        length = max(l1,l2)
        zeros = "0"*diff
        if(l1>l2):
            num2=zeros+num2
        else:
            num1=zeros+num1
        carry=0
        x=""
        for i in range(length-1,-1,-1):
            sum=int(num1[i])+int(num2[i])+carry
            carry=sum//10
            sum=sum % 10
            x += str(sum)
        if(carry!=0):
            x=x+str(carry)
        y=x[::-1]
        return y
print(addStrings("9999","10"))
print(addStrings("1234","9823"))

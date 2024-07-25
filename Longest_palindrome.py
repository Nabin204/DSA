#Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
#palindrome
# that can be built with those letters.

#Letters are case sensitive, for example, "Aa" is not considered a palindrome.

def longestPalindrome(s: str) -> int:
        count = 0
        p = 0
        lst=list(set(list(s)))
        for i in lst:
            if(s.count(i)%2==1):
                p += 1
            if(s.count(i)>1):
                count += s.count(i)//2
        if(p>0):
            return 2*count+1
        else:
            return 2*count
str1="Nabinbhat"
print(longestPalindrome(str1))
#Given a pattern and a string s, find if s follows the same pattern.

#Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

def wordPattern(pattern: str, s: str) -> bool:
        count=0
        a=s.split()
        l=len(pattern)
        l1=len(a)
        if(l==l1):
            for i in range(l):
                p=pattern.count(pattern[i])
                if(a.count(a[i])==p and a.index(a[i])==pattern.index(pattern[i])):
                    count += 1
            if(count == l):
                return True
            else:
                return False
        else:
            return False
pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern,s))
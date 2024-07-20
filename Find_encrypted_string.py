#You are given a string s and an integer k. Encrypt the string using the following algorithm:
#For each character c in s, replace c with the kth character after c in the string (in a cyclic manner).
#Return the encrypted string.
def getEncryptedString(s: str, k: int) -> str:
        x=""
        l=len(s)
        for i in range(l):
            x += s[(i+k)%l]
        return x
string1="mynameisnabinbhat"
k=4
print(getEncryptedString(string1,k))
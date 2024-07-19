import math
def validSquare(p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        p1p2=math.dist(p1,p2)
        p1p3=math.dist(p1,p3)
        p1p4=math.dist(p1,p4)
        p2p3=math.dist(p2,p3)
        p2p4=math.dist(p2,p4)
        p3p4=math.dist(p3,p4)
        lst = [p1p2,p1p3,p1p4,p2p3,p2p4,p3p4]
        a=b=0
        for i in lst:
            if(i==0):
                break
            elif(lst.count(i)==4):
                a += 1
            elif(lst.count(i)==2):
                b += 1
        if(a==4 and b==2):
            return True
        else:
            return False
#First test case
p1 = [0,0]
p2 = [1,1]
p3 = [1,0] 
p4 = [0,1]
print(validSquare(p1,p2,p3,p4))

#Second test case
q1 = [0,0]
q2 = [1,1]
q3 = [0,0]
q4 = [1,1]
print(validSquare(q1,q2,q3,q4))
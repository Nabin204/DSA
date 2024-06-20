def two_sum(a:list,target:int):
    index=[]
    value=[]
    l=len(a)
    for i in range(l-1):
        for j in range(i+1,l):
            if(a[i]+a[j]==target):
                index.append([i,j])
                value.append([a[i],a[j]])
    return [index,value]

lst1=[2,6,12,34,56,71,33,71,9,21,78,90]
target=92
index_result1=two_sum(lst1,target)[0]
value_result1=two_sum(lst1,target)[1]
print(index_result1)
print(value_result1)
    
    
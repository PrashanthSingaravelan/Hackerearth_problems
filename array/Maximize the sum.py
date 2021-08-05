t = int(input())
for i in range(t):
    n,k = input().split()
    k = int(k)
    n = int(n)
    list1 = list(map(int,input().strip().split()))[:n]    
    
    dict1 = {}
    count = 0
    sum1  = 0

    for i in range(len(list1)):
        for j in range(len(list1)):
            if (list1[j]==list1[i]):
                count = count + 1
        dict1.update({ list1[i]: count})
        count = 0

    list_temp = list(dict1.items())
    sum1 = []
    
    for i in range(len(dict1)):
        if list_temp[i][0]>=0:
            sum1.append(list_temp[i][0] * list_temp[i][1])
    sum1.sort(reverse=True)
    print(sum(sum1[:k]))

#### Discussion solution
'''
from collections import Counter
for i in range(int(input())):
    n,k=map(int,input().split())
    lst=list(map(int,input().split()))
    b=Counter(lst)
    arr=[]
    for i in b.keys():
        if i*b[i]>=0:
            arr.append(i*b[i])
        else:
            continue
    arr.sort(reverse=True)
    print(sum(arr[:k]))
'''
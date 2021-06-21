import numpy as np

n = int(input())
a = list(map(int, input().split()))

a = sorted(a)
ans = n*(n-1)/2
a_prior = a[0]
b = 1
for i in range(1,len(a)):
    if a_prior == a[i]:
        b += 1
    elif b != 1:
        ans = ans - b*(b-1)/2
        b = 1
        a_prior = a[i]
    else:
        b = 1
        a_prior = a[i]

if b != 1:
    ans = ans - b*(b-1)/2

print(int(ans))
    
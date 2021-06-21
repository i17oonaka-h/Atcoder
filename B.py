import numpy as np
import math

n = int(input())
n_ans = 0
for i in range(1,10**9):
    n_ans = n_ans+i
    if n_ans >= n:
        print(i)
        break
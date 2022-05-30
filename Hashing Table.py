import numpy as np
import random
import time
from timeit import default_timer as timer

def find_pair_naive_A1(numbers_list, target):
    for i in numbers_list:
        for j in numbers_list:
            if(i + j == target):
                return

def find_pair_hashing_A3(numbers_list, target):
    H = set()
    for i in numbers_list:
        if (target - i in H):
            return
        else:
            H.add(i)

def test(num_of_int, iterations):
    N = random.sample(range(1, 10**8), num_of_int)
    Target = (10**6)/2
    tAvg1 = [] 
    tAvg3 = []
    for i in range(iterations):
        start = timer()
        b_found = find_pair_naive_A1(N, Target)
        tAvg1.append(timer()-start)
        start = timer()
        b_found = find_pair_hashing_A3(N, Target)
        tAvg3.append(timer()-start)
    return np.mean(tAvg1), np.mean(tAvg3)

tAvg1, tAvg3 = test(2500, 25)

print(tAvg1, tAvg3)
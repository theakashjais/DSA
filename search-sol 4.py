#!/usr/bin/env python3

import random
import time

def binary_search_rec(arr, key): 
    def __binary_search_rec(arr, low, high, key):
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                return __binary_search_rec(arr, low, mid - 1, key)
            else:
                return __binary_search_rec(arr, mid + 1, high, key)
        else:
            return -1
    return __binary_search_rec(arr, 0, len(arr) - 1, key)

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1

def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high and key >= arr[low] and key <= arr[high]:
        mid = low + ((key - arr[low]) * (high - low) // (arr[high] - arr[low]))
        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1


funs = [linear_search, binary_search, interpolation_search]
arr = [random.randint(0, 10000000) for i in range(1000000)]
arr.sort()
keys = [arr[random.randint(0, 1000000)] for i in range(10)]
keys.extend(random.randint(0, 1000000)  for i in range(5))
for key in keys:
    for fun in funs:
        start = time.perf_counter_ns()
        found = fun(arr, key)
        end = time.perf_counter_ns()
        print(f"searching for {key} in arr[{len(arr)}] using {fun}: {found} in {(end-start)/1000000} ms")

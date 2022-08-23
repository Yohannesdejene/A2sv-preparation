
import math
import os
import random
import re
import sys


def insertionSort1(n, arr):
    target = arr[-1]
    index = n-2

    while (target < arr[index]) and (index >= 0):
        arr[index+1] = arr[index]
        print(*arr)
        index -= 1

    arr[index+1] = target
    print(*arr)

#check with array=arr
arr=[2,4,5,76,8,9];
n=6
insertionSort1(n, arr)
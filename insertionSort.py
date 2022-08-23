
import math
import os
import random
import re
import sys

def insertionSort1(arr):
  
    for x in range(len(arr)-1):
       target=arr[x+1];
       y=x
       while (target < arr[y]) and (y >= 0):
         arr[y+1] = arr[y]
         y-=1;

       arr[y+1] = target
   
arr=[2,4,5,76,5,4,-5,6,9];

insertionSort1(arr)
print(arr);
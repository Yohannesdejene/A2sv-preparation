
import math
import os
import random
import re
import sys


def gradingStudents(grades):
   
    counter=0
    for grade in grades:
        if grade < 38:
            grades[counter]=grade
        elif grade % 5 >= 3:
            grades[counter]+=(5-(grade % 5))
        counter+=1
    return grades
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()  
def countingSort(arr):
   output = [0] * (max(arr) + 1)
   for x in arr:
        print("x",x);
        output[x] += 1
        
   print(output)
#test with arr
arr=[1,3,5,7,9,0,3]
countingSort(arr);

list=[1,2,54,78,43]
def largestNumber(self, nums):
        temp = [str(i) for i in nums]
        temp.sort(cmp = lambda x, y: cmp(x+y, y+x), reverse = True)
        result = "".join(temp)
        if result[0] == "0":   
          return "0"      # All "0"s

print(x)
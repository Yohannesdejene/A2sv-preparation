def kthLargestNumber( nums, k):
        
       for i in range(0, len(nums)):
         nums[i] = int(nums[i]) 
       nums.sort();
       dic={}
       y=len(nums);
       for x in nums:
         dic[y]=x
         y-=1
       return str(dic[k])
#test with list
list=[3,6,7,8,9,10,3]
k=kthLargestNumber(list,4);
print(k)
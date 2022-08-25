def merge(intervals):
        if len(intervals) == 0 or len(intervals) == 1:
         return intervals
        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]
        print("list",intervals)
        print("result",result)
        print("r-",result[-1][1])
        for interval in intervals[1:]:
          print("interval",interval[0])
          if interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
          else:
            result.append(interval)
        return result
#try with inter
inter=[[1,3],[0,4],[7,9],[3,6]]
merge(inter);
x=merge(inter);
print(x)
     
    
# list=[[8,10],[2,6],[15,18],[1,3]];
# list.sort(key=lambda x:x[0])
# print(list)
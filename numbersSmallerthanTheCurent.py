list=[10,5,6,7];
secondList=[0]*len(list);
target=list[0]
for x in range(len(list)):
    target=list[x]
    for y in range(len(list)):
      if(target>list[y]):
          secondList[x]+=1;
return secondList
      
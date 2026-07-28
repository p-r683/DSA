# count frequency of items in dictionary as key:item and value:frequency
#method-1
num=[1,2,3,3,4,1,2,2,4,5]
frequency_map={}
for i in range(0,len(num)):
    if num[i] in frequency_map:
        frequency_map[num[i]]= frequency_map[num[i]] + 1
    else:
        frequency_map[num[i]]=1
print(frequency_map)

#method-2
hash_map={}
for i in range(0,len(num)):
    hash_map[num[i]]=hash_map.get(num[i],0)+1
print(hash_map)
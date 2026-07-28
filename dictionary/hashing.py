#find frequency of items of m in n 
'''constraints
1.1<=n[i]<=10
2.n can have 10^8 elements
3.m can have 10^8 elements''' 
n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
#method-1-brute force method(not optimal solution)
for num in m: # tc=O(m)
    count=0
    for x in n: # tc=O(n)
        if(x==num):
            count=count+1
    print(f"frequency of {num} is {count}") # final tc=O(m*n) ie 10^8 * 10^8=10^16 which exceeds the Time limit and throw TLE error 
    
#method-2 hash table 
hash_list=[0]*11 #len(n)+1=11
for num in n:
    hash_list[num]=hash_list[num]+1
        
for num in m:
    if num<1 or num>10:
        print(0)
    else:
        print(hash_list[num]) #final tc=O(m+n) i.e., 10^8 + 10^8= 2*10^8           
        
#method-3 dictionary 
frequency_map = {}

# Build frequency map
for num in n:
    if num in frequency_map:
        frequency_map[num] += 1
    else:
        frequency_map[num] = 1

# Print frequencies
for num in m:
    print(f"Frequency of {num} is {frequency_map.get(num, 0)}")
s = "Ba$rtT@ah$T" 
q = ['@','T', 'B', 'a', '$']  #constraints.. for mixed case
 
#method-1 - hash table
hash_list=[0]*128
for ch in s:
    ascii_value=ord(ch)
    index=ascii_value
    hash_list[index]=hash_list[index]+1
    
for ch in q:
    ascii_value=ord(ch)
    index=ascii_value
    print(f"frquency of character {ch} is {hash_list[index]}")
    
#method-2 dictinory
dict={}
for ch in s:
    if( ch in dict):
        dict[ch]=dict[ch]+1
    else:
        dict[ch]=1
        
for ch in q:
    print(f"Frequency of {ch} is {dict.get(ch, 0)}")
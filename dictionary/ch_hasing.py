s="azyxyyzaaaa"   #constraints.."a"<=s[i]<="z" only for lower case
q=["d","a","y","x"]  
#method-1 - hash table
hash_list=[0]*26
for ch in s:
    ascii_value=ord(ch)
    index=ascii_value-97  # ascii value a=97 and z=122
    hash_list[index]=hash_list[index]+1
    
for ch in q:
    ascii_value=ord(ch)
    index=ascii_value-97
    print(f"frquency of character {ch} is {hash_list[index]}")
    
#method-2 dictinory
dict={}
for ch in s:
    if( ch in dict):
        dict[ch]=dict[ch]+1
    else:
        dict[ch]=1
        
for ch in q:
    # print(f"Frequency of {ch} is {dict.get(ch, 0)}")
    if(ch in dict):
        print(dict[ch])
    else:
        print(0)    
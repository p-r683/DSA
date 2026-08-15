class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
           index=haystack.index(needle)
        else:
            index=-1
        return index    
                

# No.1/2019-06-05/56 ms/13.2 MB

class Solution:
    def romanToInt(self, s: str) -> int:
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result=0
        for i in range(len(s)):
            if i==len(s)-1 or dict[s[i]]>=dict[s[i+1]]:
                result+=dict[s[i]]
            else:
                result-=dict[s[i]]
        return result
        

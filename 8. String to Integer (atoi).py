# No.1/2019-06-04/40 ms/13.4 MB

class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str)==0 or str.isspace(): return 0
        string=str.lstrip()
        r=''
        if string[0]=='-' or string[0]=='+':
            r+=string[0]
            string=string[1:]
        if len(string)==0: return 0
        i=0
        while string[i].isdigit():
            r+=string[i]
            i+=1
            if i==len(string):
                break
        if i==0: 
            return 0
        else:
            r=int(r)
            if r>2**31-1: 
                return 2**31-1
            elif r<-2**31:
                return -2**31
            else:
                return r

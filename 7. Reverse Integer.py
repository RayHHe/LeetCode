#No.1/2019-06-03/36 ms/13.4 MB
class Solution:
    def reverse(self, x):
        s=str(x)
        l=len(s)
        flag=0
        r=''
        if x<0:
            flag=1
            r+='-'
        for i in range(l,flag,-1):
            r+=s[i-1]
        r=int(r)
        if r<-2**31 or r>2**31-1: r=0
        return r

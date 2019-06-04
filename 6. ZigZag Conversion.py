#No.1/2019-06-03/60 ms/13.4 MB

class Solution:
    def convert(self, s, numRows):
        r=''
        l=len(s)
        i=0
        for i in range(numRows):
            if numRows==1:
                return s
            elif i%(numRows-1)==0:
                j=i
                while j<l:
                    r+=s[j]
                    j+=2*(numRows-1)
            else:
                j=i
                while j<l:
                    r+=s[j]
                    k=j+2*(numRows-1-i)
                    if k<l:
                        r+=s[k]
                    j+=2*(numRows-1)
        return r

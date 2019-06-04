# No.1/2019-06-03/800 ms/13.3 MB

class Solution:
    def longestPalindrome(self, s):
        label=m=0
        l=len(s)
        for i in range(l):
            j=0
            while s[i]==s[i+j]:
                j+=1
                if i+j>l-1:
                    break
            k=0
            while s[i-k]==s[i+j-1+k]:
                k+=1
                if i<k or i+j+k>l:
                    break
            if m<2*(k-1)+j:
                label=i-k+1
                m=2*(k-1)+j
        return s[label:label+m]

# No.2/2019-06-03/1316 ms/13.1 MB
# Less Space, More Time
class Solution:
    def longestPalindrome(self, s):
        result=''
        m=0
        l=len(s)
        for i in range(2*l-1):
            j=i%2
            while s[(i-j)//2]==s[(i+j)//2]: #use // to avoid float
                j+=2
                if i<j or (i+j)/2>l-1:
                    break
            if m<j-1:
                result=s[(i-(j-2))//2:(i+j)//2]
                m=j-1
        return result

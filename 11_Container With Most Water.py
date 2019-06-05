# No.1/2019-06-04/64 ms/14.3 MB

class Solution:
    def maxArea(self, height):
        i=m=h1=h2=0
        j=1
        l=len(height)
        while i+j<l:
            if height[i]<h1:
                i+=1
                continue
            if height[-j]<h2:
                j+=1
                continue
            n=(l-i-j)*min(height[i],height[-j])
            if m<n:
                m=n
                h1=height[i]
                h2=height[-j]
            else:
                if height[i]<=height[-j]:
                    i+=1
                else:
                    j+=1
                continue
        return m

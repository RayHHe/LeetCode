# No.1/2019-06-03/80 ms/13.3 MB

class Solution:
    def lengthOfLongestSubstring(self, s):
        l=[]
        length=0
        for letter in s:
            if letter in l:
                l=l[l.index(letter)+1:]
            l.append(letter)
            if len(l)>length:
                length=len(l)
        return length

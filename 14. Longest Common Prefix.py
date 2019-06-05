# No.1/2019-06-05/36 ms/13.2 MB

class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs)==0 : return ''
        result=strs[0]
        for word in strs[1:]:
            for i,letter in enumerate(result):
                if i==len(word):
                    result=word
                    break
                if letter!=word[i]:
                    result=word[:i]
                    break
        return result

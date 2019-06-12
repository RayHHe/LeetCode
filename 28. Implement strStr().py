# No.1/2019-06-12/48 ms/13.4 MB

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0: return 0
        for j in range(len(haystack)):
            try:
                if haystack[j:j+len(needle)]==needle:
                    return j
            except:
                continue
        return -1

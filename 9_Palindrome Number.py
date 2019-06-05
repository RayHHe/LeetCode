# No.1/2019-06-04/64 ms/13.3 MB

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        for i in range(int(len(s)/2)):
            if s[i]!=s[-(i+1)]:
                return False
        return True

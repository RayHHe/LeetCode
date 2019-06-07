# No.1/2019-06-06/36 ms/13.1 MB

class Solution:
    def isValid(self, s: str) -> bool:
        flag=''
        dict={')':'(','}':'{',']':'['}
        for sign in s:
            if sign in ['(','{','[']:
                flag+=sign
            else:
                if len(flag)==0 or flag[-1]!=dict[sign]:
                    return False
                else:
                    flag=flag[:-1]
        if flag=='':
            return True
        else:
            return False
        

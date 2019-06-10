# No.1/2019-06-10/68 ms/13.3 MB

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l=['()']
        if n==0: return []
        for i in range(1,n):
            newl=[]
            for string in l:
                for index in range(len(string)//2+1):
                    temp=string[:index]+'()'+string[index:]
                    if temp not in newl: newl.append(temp)
            l=newl
        return l

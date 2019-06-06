# No.1/2019-06-06/44 ms/13.3 MB
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],
             '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],
             '8':['t','u','v'],'9':['w','x','y','z']}
        if len(digits)==0: return []
        result=['']
        for i in range(len(digits)):
            temp=[]
            for letter in dic[digits[-i-1]]:
                for r in result:
                    temp.append(letter+r)
            result=temp
        return result
                

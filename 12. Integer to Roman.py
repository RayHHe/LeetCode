#No.1/2019-06-04/56 ms/13.3 MB

class Solution:
    def intToRoman(self, num: int) -> str:
        Mod=[1000,500,100,50,10,5,1]
        Roman=['M','D','C','L','X','V','I']
        div=[]
        for M in Mod:
            div.append(num//M)
            num=num%M
        Result=[]
        for i in range(1,len(div)+1):
            if div[-i]==4:
                if div[-i-1]==0:
                    Result.insert(0,Roman[-i]+Roman[-i-1])
                else:
                    Result.insert(0,Roman[-i]+Roman[-i-2])
                    div[-i-1]=0
            else:
                Result.insert(0,Roman[-i]*div[-i])
        Result=''.join(Result)
        return Result

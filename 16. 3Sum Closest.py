# No.1/2019-06-06/108 ms/13 MB

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        flag=float('inf')
        for i in range(len(nums)-2):
            k=i+1; j=len(nums)-1              
            while k<j:
                t=nums[i]+nums[k]+nums[j]
                if abs(t-target)<flag:
                    result=t
                    flag=abs(t-target)
                if t>target:
                    j-=1
                elif t<target:
                    k+=1
                else:
                    return target
        return result

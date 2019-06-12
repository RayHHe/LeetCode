# No.1/2019-06-11/68 ms/14.6 MB

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,i=len(nums),0
        while i<l:
            if i>0 and nums[i]==nums[i-1]:
                del nums[i]
                l-=1
                continue
            i+=1

# No.1/2019-06-19/44 ms/13.1 MB

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=len(nums)-1
        while i > 0 and nums[i]<=nums[i-1]: i-=1
        head=i
        end=len(nums)-1
        while head<end:
            temp=nums[head]
            nums[head]=nums[end]
            nums[end]=temp
            head+=1
            end-=1
        if i>0:
            flag=i
            while nums[flag]<=nums[i-1]: flag+=1
            temp=nums[i-1]
            nums[i-1]=nums[flag]
            nums[flag]=temp

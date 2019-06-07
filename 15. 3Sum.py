#No.1/2019-06-06/724 ms/16.9 MB

class Solution:
    def threeSum(self, nums):
        nums.sort()
        result=[]
        if len(nums)<3: return result
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]: continue
            if nums[i]>0: break
            k=i+1; j=len(nums)-1
            if nums[j]<-nums[i]/2: continue                
            while k<j:
                target=nums[i]+nums[k]+nums[j]
                if target>0:
                    j-=1
                elif target<0:
                    k+=1
                else:
                    result.append([nums[i],nums[k],nums[j]])
                    while k<j and nums[j]==nums[j-1]: j-=1
                    while k<j and nums[k]==nums[k+1]: k+=1
                    j-=1; k+=1
        return result

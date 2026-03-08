class Solution(object):
    def twoSum(self, nums, target):
       map={}
       for i in range(len(nums)):
        c=target-nums[i]
        if c in map:
            return [map[c]+1,i+1]
        map[nums[i]]=i

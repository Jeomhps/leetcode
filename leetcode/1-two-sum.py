class Solution(object):
    def twoSum(self, nums, target):
        index=0

        for number in nums:
            
            for i in range(len(nums)):
                if index == i:
                    pass
                else:
                    if number + nums[i] == target:
                        return [nums.index(number),i]       

            index+=1

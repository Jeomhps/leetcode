class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        index=0

        for number in nums:
            
            for i in range(len(nums)):
                if index == i:
                    pass
                else:
                    if number + nums[i] == target:
                        return [nums.index(number),i]       

            index+=1

    nums = [2,7,11,15] 
    __import__('pprint').pprint(twoSum(1,nums,9))


        

class Solution(object):
    def majorityElement(self, nums):
        maxCount = 0
        maxNum = 0
        for i in set(nums):
            count = nums.count(i)
            if count >= maxCount:
                maxCount = count
                maxNum = i
        return maxNum
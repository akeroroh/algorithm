class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        arr = [-1] * (len(nums)+1)
        while i < len(nums):
            arr[nums[i]] = nums[i]
            i += 1

        for i in range(0, len(arr)):
            if arr[i] == -1:
                return i
        
        
# Leetcode 3471: Find the Largest Almost Missing Integer
# https://leetcode.com/problems/find-the-largest-almost-missing-integer/
# Solved on 18th of August, 2026
class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        """
        Finds the largest integer that appears in exactly one subarray of size k.
        Args:
            nums (List[int]): The input array of integers.
            k (int): The target subarray size.
        Returns:
            int: The maximum value appearing in exactly one contiguous subarray
                of size k, or -1 if no such integer exists.
        """
        numsLength = len(nums)

        if k == numsLength:
            return max(nums)

        if k == 1:
            freqMap = {}
            for numVal in nums:
                freqMap[numVal] = freqMap.get(numVal, 0) + 1
            maxVal = -1
            for numVal, countVal in freqMap.items():
                if countVal == 1 and numVal > maxVal:
                    maxVal = numVal
            return maxVal

        maxVal = -1
        if nums.count(nums[0]) == 1:
            maxval = max(maxVal, nums[0])
        if nums.count(nums[-1]) == 1:
            maxVal = max(maxVal, nums[-1])

        return maxVal
# Leetcode 3012: Minimize Length of Array Using Operations
# https://leetcode.com/problems/minimize-length-of-array-using-operations/
# Solved on 3rd of August, 2025
class Solution:
    def minimumArrayLength(self, nums: list[int]) -> int:
        """
        Calculates the minimum possible length of the array after applying a specific operation.
        The operation involves replacing two elements x and y with x % y.
        :param nums: A list of integers.
        :return: The minimum possible length of the array.
        """
        minVal = min(nums)

        for num in nums:
            if num % minVal > 0:
                return 1
            
        minCount = nums.count(minVal)

        return (minCount + 1) // 2
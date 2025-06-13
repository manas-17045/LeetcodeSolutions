# Leetcode 2616: Minimize the Maximum Difference of Pairs
# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
# Solved on 13th of June, 2025

class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        """
        Minimizes the maximum difference of p pairs in the given array.

        Args:
            nums: A list of integers.
            p: The number of pairs to form.

        Returns:
            The minimum possible value of the maximum difference among all p pairs.
        """
        if p == 0:
            return 0

        nums.sort()
        n = len(nums)

        def canFormPairs(maxDiff):
            pairCount = 0
            index = 0
            while index < (n - 1):
                if nums[index + 1] - nums[index] <= maxDiff:
                    pairCount += 1
                    index += 2
                else:
                    index += 1
                if pairCount >= p:
                    return True
            return False

        left = 0
        right = nums[n - 1] - nums[0]
        result = right

        while left <= right:
            mid = left + (right - left) // 2
            if canFormPairs(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
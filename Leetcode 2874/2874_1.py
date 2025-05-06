# Leetcode 2874: Maximum Value of an Ordered Triplet II
# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        """
        This function computes the maximum value of the triplet (nums[i] - nums[j]) * nums[k] from a
        given list of integers, where 0 <= i < j < k < len(nums). The function iterates through
        the list and maintains the maximum difference of nums[i] - nums[j] seen so far and the
        maximum nums[i] seen so far. These values are then used to calculate the result efficiently.

        :param nums: A list of integers representing the input array
        :type nums: list[int]

        :return: The maximum value of the triplet (nums[i] - nums[j]) * nums[k]
        :rtype: int
        """
        ans = 0
        maxDiff = 0     # This will track the maximum difference (nums[i] - nums[j]) so far.
        maxNum = 0      # This will track the maximum nums[i] seen so far.

        for num in nums:
            # Consider the current number as nums[k] and update the answer.
            ans = max(ans, maxDiff * num)
            # Update maxDiff: treat the current num as candidate for nums[j]
            maxDiff = max(maxDiff, maxNum - num)
            # Update maxNum to include the current element as a candidate for nums[i].
            maxNum = max(maxNum, num)

        return ans
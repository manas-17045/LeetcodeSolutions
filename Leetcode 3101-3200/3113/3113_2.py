# Leetcode 3113: Find the Number of Subarrays Where Boundary Elements Are Maximum
# https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/
# Solved on 5th of August, 2025
class Solution:
    def numberOfSubarrays(self, nums: list[int]) -> int:
        """
        Calculates the number of subarrays where the first element is the maximum.
        :param nums: A list of integers.
        :return: The total count of such subarrays.
        """
        ans = 0
        # Stack of [value, count_of_consecutive_value]
        stk: list[list[int]] = []

        for num in nums:
            # Pop all strictly smaller values
            while stk and stk[-1][0] < num:
                stk.pop()

            # If equal, extend count
            if stk and stk[-1][0] == num:
                stk[-1][1] += 1
                ans += stk[-1][1]
            else:
                # New value
                stk.append([num, 1])
                ans += 1

        return ans
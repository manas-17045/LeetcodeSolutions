# Leetcode 795: Number of Subarrays with Bounded Maximum
# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/
# Solved on 5th of August, 2025
class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        """
        Counts the number of subarrays where the maximum element is within the given bounds [left, right].
        :param nums: A list of integers.
        :param left: The lower bound for the maximum element in a subarray.
        :param right: The upper bound for the maximum element in a subarray.
        :return: The total count of valid subarrays.
        """
        # Helper function to count subarrays where every element <= k
        def count_leq(k: int) -> int:
            total = 0
            curr_len = 0
            for x in nums:
                if x <= k:
                    curr_len += 1
                    total += curr_len
                else:
                    curr_len = 0
            return total
        
        return count_leq(right) - count_leq(left - 1)
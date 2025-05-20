# Leetcode 2348: Number of Zero-Filled Subarrays
# https://leetcode.com/problems/number-of-zero-filled-subarrays/
# Solved on 20th of May, 2025

class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        """
        Counts the number of subarrays filled with zeros in a given list of integers. It iterates through the list,
        tracking consecutive zeros and calculating the number of subarrays formed by each run of zeros.
        """
        total = 0
        run = 0
        for x in nums:
            if x == 0:
                run += 1
            else:
                if run:
                    total += run * (run + 1) // 2
                    run = 0
        # Flush the last run if it ended at array's end
        if run:
            total += run * (run + 1) // 2
        return total
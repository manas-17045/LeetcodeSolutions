# Leetcode 2195: Append K Integers With Minimal Sum
# https://leetcode.com/problems/append-k-integers-with-minimal-sum/
# Solved on 5th of August, 2025
class Solution:
    def minimalKSum(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimal sum of k unique positive integers that are not present in `nums`.
        :param nums: A list of integers.
        :param k: The number of unique positive integers to sum.
        :return: The minimal sum.
        """
        # Remove duplicates and sort
        unique_nums = sorted(set(nums))
        total = 0
        prev = 0

        # Helper function to add arithmetic sequence sum from a to b inclusive
        def range_sum(a: int, b: int, cnt: int) -> int:
            return (a + b) * cnt // 2
        
        for x in unique_nums:
            # Size of gap between prev and x
            gap = x - prev - 1
            if gap > 0:
                if k <= gap:
                    # We only need k numbers: prev+1 ... prev+k
                    a, b = prev + 1, prev + k
                    total += range_sum(a, b, k)
                    return total
                # Take whole gap
                a, b = prev + 1, x - 1
                total += range_sum(a, b, gap)
                k -= gap
            prev = x
        
        # If we still need more after the largest element
        if k > 0:
            a, b = prev + 1, prev + k
            total += range_sum(a, b, k)
        
        return total
# Leetcode 1248: Count Number of Nice Subarrays
# https://leetcode.com/problems/count-number-of-nice-subarrays/
# Solved on 29th of August, 2025
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        """
        Counts the number of "nice" subarrays. A subarray is "nice" if it contains exactly k odd numbers.

        Args:
            nums (list[int]): The input array of integers.
            k (int): The target number of odd integers for a subarray to be considered "nice".

        Returns:
            int: The total number of nice subarrays.
        """
        def atMost(goal: int) -> int:
            count = 0
            left = 0
            oddCount = 0

            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    oddCount += 1

                while oddCount > goal:
                    if nums[left] % 2 == 1:
                        oddCount -= 1
                    left += 1

                count += right - left + 1

            return count

        return atMost(k) - atMost(k - 1)
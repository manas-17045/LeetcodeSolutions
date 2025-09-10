# Leetcode 1567: Maximum Length of Subarray With Positive Product
# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
# Solved on 10th of September, 2025
class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        """
        Finds the maximum length of a subarray whose product is positive.
        :param nums: A list of integers.
        :return: The maximum length of a subarray with a positive product.
        """
        n = len(nums)
        ans = 0
        i = 0

        while i < n:
            # Skip zeros
            if nums[i] == 0:
                i += 1
                continue

            # Find end of current zero-free segment [i, j)
            j = i
            neg_count = 0
            first_neg = -1
            last_neg = -1

            while j < n and nums[j] != 0:
                if nums[j] < 0:
                    if first_neg == -1:
                        first_neg = j
                    last_neg = j
                    neg_count += 1
                j += 1

            # If product of whole segment is positive (even negatives)
            if neg_count % 2 == 0:
                ans = max(ans, j - i)
            else:
                # Remove prefix up to and including first negative
                left_len = j - (first_neg + 1)
                # Or, remove suffix from last negative to end
                right_len = last_neg - i
                ans = max(ans, left_len, right_len)

            i = j

        return ans
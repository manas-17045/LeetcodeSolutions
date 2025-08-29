# Leetcode 2261: K Divisible Elements Subarrays
# https://leetcode.com/problems/k-divisible-elements-subarrays/
# Solved on 29th of August, 2025
class Solution:
    def countDistinct(self, nums: list[int], k: int, p: int) -> int:
        """
        Counts the number of distinct subarrays that satisfy certain conditions.
        :param nums: A list of integers.
        :param k: The maximum number of elements divisible by 'p' allowed in a subarray.
        :param p: The divisor.
        :return: The number of distinct subarrays satisfying the conditions.
        """
        n = len(nums)
        seen = set()

        for i in range(n):
            cnt_div = 0
            cur = []
            for j in range(i, n):
                if nums[j] % p == 0:
                    cnt_div += 1
                if cnt_div > k:
                    break
                cur.append(nums[j])
                # Store tuple (immutable) to ensure distinctness by content
                seen.add(tuple(cur))

        return len(seen)
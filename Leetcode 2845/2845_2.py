# Leetcode 2845: Count of Interesting Subarrays
# https://leetcode.com/problems/count-of-interesting-subarrays

from typing import List
from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)

        transformed = [1 if num % modulo == k else 0 for num in nums]

        prefix_sum = 0

        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1

        result = 0

        for num in transformed:
            prefix_sum += num
            target = (prefix_sum - k) % modulo
            result += prefix_counts[target]
            prefix_counts[prefix_sum % modulo] += 1

        return result
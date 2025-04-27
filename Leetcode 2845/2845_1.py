# Leetcode 2845: Count of Interesting Subarrays
# https://leetcode.com/problems/count-of-interesting-subarrays
from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        total_count = 0
        current_prefix_cnt = 0
        counts = {0: 1}

        for num in nums:
            if num % modulo == k:
                current_prefix_cnt += 1

            current_mod = current_prefix_cnt % modulo

            target_mod = (current_mod - k + modulo) % modulo

            total_count += counts.get(target_mod, 0)

            counts[current_mod] = counts.get(current_mod, 0) + 1

        return total_count
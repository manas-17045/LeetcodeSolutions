# Leetcode 3729: Count Distinct Subarrays Divisible by K in Sorted Array
# https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/
# Solved on 2nd of December, 2025
import collections


class Solution:
    def numGoodSubarrays(self, nums: list[int], k: int) -> int:
        """
        Counts the number of distinct subarrays whose sum is divisible by k.

        Args:
            nums (list[int]): The input array of integers.
            k (int): The divisor.
        Returns:
            int: The number of distinct subarrays whose sum is divisible by k.
        """

        n = len(nums)
        prefixMod = [0] * (n + 1)
        currentSum = 0
        for i in range(n):
            currentSum = (currentSum + nums[i]) % k
            prefixMod[i + 1] = currentSum

        events = [[] for _ in range(n + 2)]

        start = 0
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                events[start + 1].append(('head', start))
                if i - 1 > start:
                    if i + 1 <= n:
                        events[i + 1].append(('batch', start + 1, i - 1))
                start = i

        events[start + 1].append(('head', start))

        freq = collections.defaultdict(int)
        ans = 0

        for x in range(n, 0, -1):
            freq[prefixMod[x]] += 1
            if events[x]:
                for type, p1, *args in events[x]:
                    if type == 'head':
                        ans += freq[prefixMod[p1]]
                    else:
                        end = args[0]
                        for i in range(p1, end + 1):
                            ans += freq[prefixMod[i]]

        return ans
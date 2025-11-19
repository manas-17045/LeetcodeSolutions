# Leetcode 3434: Maximum Frequency After Subarray Operations
# https://leetcode.com/problems/maximum-frequency-after-subarray-operation/
# Solved on 19th of November, 2025
class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum frequency of an element after performing subarray operations.

        Args:
            nums: A list of integers.
            k: An integer representing the target value.
        Returns:
            The maximum frequency of an element after operations.
        """
        frequencyOfK = 0
        candidates = []
        seen = [False] * 52

        for num in nums:
            if num == k:
                frequencyOfK += 1
            elif not seen[num]:
                seen[num] = True
                candidates.append(num)

        maxGain = 0
        currentGains = [0] * 52

        for num in nums:
            if num == k:
                for val in candidates:
                    currentGains[val] -= 1
                    if currentGains[val] < 0:
                        currentGains[val] = 0
            else:
                currentGains[num] += 1
                if currentGains[num] > maxGain:
                    maxGain = currentGains[num]

        return frequencyOfK + maxGain
# Leetcode 3346: Maximum Frequency of an Element After Performing Operations I
# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/
# Solved on 23rd of September, 2025
import bisect


class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        """
        Calculates the maximum frequency of an element in the array after performing at most numOperations operations.
        An operation consists of increasing an element by 1.

        Args:
            nums: A list of integers.
            k: The maximum allowed difference between elements in a valid window.
            numOperations: The maximum number of operations allowed.

        Returns:
            The maximum possible frequency of an element.
        """
        n = len(nums)
        if n == 0:
            return 0

        nums.sort()

        # Create a new group from scratch using L operations
        maxLenFromOps = 0
        left = 0
        for right in range(n):
            # A window is valid if its range is <= 2k and its ;length <= numOperations
            while nums[right] - nums[left] > 2 * k:
                left += 1

            windowLen = right - left + 1
            if windowLen <= numOperations:
                maxLenFromOps = max(maxLenFromOps, windowLen)

        # Augment existing groups
        maxFreqFromAugment = 0
        if numOperations >= n:
            # If we can change every element, check if the whole array can be unified.
            if nums[n - 1] - nums[0] <= 2 * k:
                return n

        # Find max frequency from original array as a baseline
        if n > 0:
            maxFreqFromAugment = 1
            currentStreak = 1
            for i in range(1, n):
                if nums[i] == nums[i - 1]:
                    currentStreak += 1
                else:
                    currentStreak = 1
                maxFreqFromAugment = max(maxFreqFromAugment, currentStreak)

        # Check augmenting for each element
        i = 0
        while i < n:
            v = nums[i]

            # Find the contiguous block of the same element 'v'.
            vStart = i
            while i + 1 < n and nums[i + 1] == v:
                i += 1
            vEnd = i
            vCount = vEnd - vStart + 1

            # Find range of elements convertible to v: [v - k, v + k]
            # Left boundary index for v - k
            lIdx = bisect.bisect_left(nums, (v - k))
            # Right boundary index for v + k
            rIdx = bisect.bisect_right(nums, (v + k)) - 1

            totalElementsInRange = rIdx - lIdx + 1

            currentFreq = min(totalElementsInRange, (vCount + numOperations))
            maxFreqFromAugment = max(maxFreqFromAugment, currentFreq)

            i += 1

        return max(maxFreqFromAugment, maxLenFromOps)
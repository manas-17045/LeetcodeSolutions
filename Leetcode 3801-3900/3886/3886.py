# Leetcode 3886: Sum of Sortable Integers
# https://leetcode.com/problems/sum-of-portable-integers/
# Solved on 8th of April, 2026
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        """
        Calculates the sum of all integers k such that the array can be partitioned into
        blocks of size k, where each block is 'sortable' with at most one rotation.

        :param nums: A list of integers to be evaluated.
        :return: The sum of all valid block sizes k.
        """
        n = len(nums)
        pref = [0] * n

        for i in range(1, n):
            pref[i] = pref[i - 1] + (1 if nums[i - 1] > nums[i] else 0)

        totalSum = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            prevMax = -1
            isValid = True

            for i in range(0, n, k):
                lIdx = i
                rIdx = i + k - 1

                dropCount = pref[rIdx] - pref[lIdx]

                if dropCount == 0:
                    bMin = nums[lIdx]
                    bMax = nums[rIdx]
                elif dropCount == 1:
                    if nums[rIdx] > nums[lIdx]:
                        isValid = False
                        break

                    low = lIdx + 1
                    high = rIdx
                    dropIdx = -1

                    while low <= high:
                        mid = (low + high) // 2
                        if pref[mid] - pref[lIdx] >= 1:
                            dropIdx = mid
                            high = mid - 1
                        else:
                            low = mid + 1

                    bMax = nums[dropIdx - 1]
                    bMin = nums[dropIdx]
                else:
                    isValid = False
                    break

                if bMin < prevMax:
                    isValid = False
                    break

                prevMax = bMax

            if isValid:
                totalSum += k

        return totalSum
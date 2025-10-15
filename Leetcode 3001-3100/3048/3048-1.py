# Leetcode 3048: Earliest Second to Mark Indices I
# https://leetcode.com/problems/earliest-second-to-mark-indices-i/
# Solved on 15th of October, 2025
class Solution:
    def earliestSecondToMarkIndices(self, nums: list[int], changeIndices: list[int]) -> int:
        """
        Finds the earliest second by which all indices can be marked.

        :param nums: A list of integers representing the initial values of the indices.
        :param changeIndices: A list of integers representing the index that can be marked at each second.
        :return: The earliest second by which all indices can be marked, or -1 if it's not possible.
        """
        n = len(nums)
        m = len(changeIndices)

        def check(k: int) -> bool:
            lastAppearance = {}
            for i in range(k):
                lastAppearance[changeIndices[i]] = i + 1

            if len(lastAppearance) < n:
                return False

            decrementOpsAvailable = 0
            for i in range(k):
                second = i + 1
                idx = changeIndices[i]

                if second == lastAppearance.get(idx):
                    requiredDecrements = nums[idx - 1]
                    if decrementOpsAvailable < requiredDecrements:
                        return False
                    decrementOpsAvailable -= requiredDecrements
                else:
                    decrementOpsAvailable += 1

            return True

        low = 1
        high = m
        result = -1

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result
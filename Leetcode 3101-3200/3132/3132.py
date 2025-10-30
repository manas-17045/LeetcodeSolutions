# Leetcode 3132: Find the Integer Added to Array II
# https://leetcode.com/problems/find-the-integer-added-to-array-ii/
# Solved on 30th of October, 2025
class Solution:
    def minimumAddedInteger(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Finds the minimum possible integer `x` such that `nums2` can be obtained from `nums1`
        by removing two elements from `nums1` and adding `x` to all remaining elements.
        :param nums1: The first list of integers.
        :param nums2: The second list of integers.
        :return: The minimum valid integer `x`.
        """
        nums1.sort()
        nums2.sort()

        n = len(nums1)
        m = len(nums2)

        minValidX = float('inf')

        possibleCandidates = set()
        possibleCandidates.add(nums2[0] - nums1[0])
        possibleCandidates.add(nums2[0] - nums1[1])
        possibleCandidates.add(nums2[0] - nums1[2])

        for potentialX in possibleCandidates:
            p1 = 0
            p2 = 0
            removedCount = 0

            while p1 < n:
                if p2 < m and nums1[p1] + potentialX == nums2[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    p1 += 1
                    removedCount += 1

            if p2 == m and removedCount == 2:
                minValidX = min(minValidX, potentialX)

        return minValidX
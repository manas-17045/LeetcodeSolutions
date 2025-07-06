# Leetcode 1865: Finding Pairs With a Certain Sum
# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/
# Solved on 6th of July, 2025
from collections import Counter


class FindSumPairs:

    def __init(self, nums1: list[int], nums2: list[int]):
        self.numsOne = nums1
        self.numsTwo = nums2
        self.freqNumsTwo = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        oldVal = self.numsTwo[index]
        self.freqNumsTwo[oldVal] -= 1

        self.numsTwo[index] += val
        newVal = self.numsTwo[index]

        self.freqNumsTwo[newVal] = self.freqNumsTwo.get(newVal, 0) + 1

    def count(self, tot: int) -> int:
        totalPairs = 0
        for numOne in self.numsOne:
            target = tot - numOne
            totalPairs += self.freqNumsTwo.get(target, 0)
        return totalPairs
# Leetcode 1865: Finding Pairs With a Certain Sum
# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/
# Solved on 6th of July, 2025
from collections import Counter


class FindSumPairs:
    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old = self.nums2[index]
        new = old + val
        self.freq2[old] -= 1
        if self.freq2[old] == 0:
            del self.freq2[old]
        self.freq2[new] += 1
        self.nums2[index] = new

    def count(self, tot: int) -> int:
        cnt = 0
        f2 = self.freq2
        for x in self.nums1:
            cnt += f2.get(tot - x, 0)
        return cnt
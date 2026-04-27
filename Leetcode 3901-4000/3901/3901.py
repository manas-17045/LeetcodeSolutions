# Leetcode 3901: Good Subsequence Queries
# https://leetcode.com/problems/good-subsequence-queries/
# Solved on 27th of April, 2026
import math


class Solution:
    def countGoodSubseq(self, nums: list[int], p: int, queries: list[list[int]]) -> int:
        """
        Calculates the number of queries for which a 'good' subsequence exists after updates.

        :param nums: A list of integers representing the initial sequence.
        :param p: An integer divisor used to filter and transform elements.
        :param queries: A list of [index, value] pairs representing point updates on nums.
        :return: The total count of queries where the resulting sequence satisfies the 'good' criteria.
        """
        n = len(nums)
        m = 1
        while m < n:
            m *= 2

        treeGcd = [0] * (2 * m)
        treeCnt = [0] * (2 * m)

        for i in range(n):
            if nums[i] % p == 0:
                treeGcd[m + i] = nums[i] // p
                treeCnt[m + i] = 1

        for i in range(m - 1, 0, -1):
            treeGcd[i] = math.gcd(treeGcd[2 * i], treeGcd[2 * i + 1])
            treeCnt[i] = treeCnt[2 * i] + treeCnt[2 * i + 1]

        ans = 0

        for ind, val in queries:
            nums[ind] = val
            idx = m + ind

            if val % p == 0:
                treeGcd[idx] = val // p
                treeCnt[idx] = 1
            else:
                treeGcd[idx] = 0
                treeCnt[idx] = 0

            idx //= 2
            while idx > 0:
                treeGcd[idx] = math.gcd(treeGcd[2 * idx], treeGcd[2 * idx + 1])
                treeCnt[idx] = treeCnt[2 * idx] + treeCnt[2 * idx + 1]
                idx //= 2

            g = treeGcd[1]
            c = treeCnt[1]

            if c > 0 and g == 1:
                if c < n:
                    ans += 1
                else:
                    if n >= 7:
                        ans += 1
                    else:
                        canRemove = False
                        for i in range(n):
                            currentGcd = 0
                            for j in range(n):
                                if i != j:
                                    currentGcd = math.gcd(currentGcd, nums[j] // p)
                            if currentGcd == 1:
                                canRemove = True
                                break
                        if canRemove:
                            ans += 1

        return ans
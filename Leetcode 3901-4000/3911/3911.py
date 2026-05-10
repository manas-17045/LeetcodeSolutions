# Leetcode 3911: K-th Smallest Remaining Even Integer in Subarray Queries
# https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/
# Solved on 10th of May, 2026
import bisect


class Solution:
    def kthRemainingInteger(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        Finds the k-th smallest even integer remaining after removing even integers present in the subarray nums[l..r].

        :param nums: A list of integers.
        :param queries: A list of queries where each query is [l, r, k].
        :return: A list of integers representing the result for each query.
        """
        evenPos = [i for i, x in enumerate(nums) if x % 2 == 0]
        ansArr = []

        for l, r, k in queries:
            leftIdx = bisect.bisect_left(evenPos, l)
            rightIdx = bisect.bisect_right(evenPos, r) - 1

            if leftIdx > rightIdx:
                ansArr.append(k * 2)
                continue

            low = leftIdx
            high = rightIdx
            bestMid = -1

            while low <= high:
                mid = (low + high) // 2
                val = nums[evenPos[mid]]
                rem = (val // 2) - (mid - leftIdx + 1)

                if rem < k:
                    bestMid = mid
                    low = mid + 1
                else:
                    high = mid - 1

            if bestMid == -1:
                ansArr.append(k * 2)
            else:
                val = nums[evenPos[bestMid]]
                rem = (val // 2) - (bestMid - leftIdx + 1)
                ansArr.append(val + 2 * (k - rem))

        return ansArr
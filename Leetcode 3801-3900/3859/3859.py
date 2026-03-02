# Leetcode 3859: Count Subarrays With K Distinct Integers
# https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/
# Solved on 2nd of March, 2026
import collections
import heapq


class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        """
        Counts the number of subarrays that contain exactly k distinct integers,
        where each of those k integers appears at least m times in the subarray.

        :param nums: List of integers to search within.
        :param k: The required number of distinct integers.
        :param m: The minimum frequency required for each of the k distinct integers.
        :return: The total count of subarrays satisfying the criteria.
        """
        countOne = {}
        countTwo = {}
        leftOne = 0
        leftTwo = 0
        ans = 0

        indicesMap = collections.defaultdict(list)
        currentP = {}
        minHeap = []

        for r in range(len(nums)):
            x = nums[r]

            indicesMap[x].append(r)
            if len(indicesMap[x]) >= m:
                currentP[x] = indicesMap[x][-m]
            else:
                currentP[x] = -1

            heapq.heappush(minHeap, (currentP[x], x))

            countOne[x] = countOne.get(x, 0) + 1
            while len(countOne) > k:
                leftVal = nums[leftOne]
                countOne[leftVal] -= 1
                if countOne[leftVal] == 0:
                    del countOne[leftVal]
                leftOne += 1

            countTwo[x] = countTwo.get(x, 0) + 1
            while len(countTwo) > k - 1:
                leftVal = nums[leftTwo]
                countTwo[leftVal] -= 1
                if countTwo[leftVal] == 0:
                    del countTwo[leftVal]
                leftTwo += 1

            if len(countOne) == k:
                while minHeap:
                    p, val = minHeap[0]
                    if val not in countOne or currentP[val] != p:
                        heapq.heappop(minHeap)
                    else:
                        break

                if minHeap:
                    minR = minHeap[0][0]
                    ans += max(0, min(leftTwo - 1, minR) - leftOne + 1)

        return ans
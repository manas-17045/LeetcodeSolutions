# Leetcode 3321: Find X-Sum of All K-Long Subarrays II
# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/
# Solved on 5th of November, 2025
from sortedcontainers import SortedList


class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        """
        Calculates the X-sum for all k-long subarrays in the given list of numbers.
        :param nums: The input list of integers.
        :param k: The length of the subarrays.
        :param x: The number of largest distinct frequencies to consider for the X-sum.
        :return: A list of X-sums for each k-long subarray.
        """
        freqs = {}
        topX = SortedList()
        others = SortedList()
        valToContainer = {}

        currentXSum = 0
        totalSum = 0
        results = []

        def removeItem(item):
            nonlocal currentXSum
            val = item[1]
            freq = item[0]
            container = valToContainer.pop(val)

            if container is topX:
                topX.remove(item)
                currentXSum -= val * freq
                if len(others) > 0:
                    promoted = others.pop(-1)
                    promotedVal = promoted[1]
                    promotedFreq = promoted[0]
                    topX.add(promoted)
                    currentXSum += promotedVal * promotedFreq
                    valToContainer[promotedVal] = topX
            else:
                others.remove(item)

        def addItem(item):
            nonlocal currentXSum
            val = item[1]
            freq = item[0]

            topX.add(item)
            currentXSum += val * freq
            valToContainer[val] = topX

            if len(topX) > x:
                kicked = topX.pop(0)
                kickedVal = kicked[1]
                kickedFreq = kicked[0]
                currentXSum -= kickedVal * kickedFreq
                others.add(kicked)
                valToContainer[kickedVal] = others

        def addVal(val):
            nonlocal currentXSum, totalSum
            totalSum += val
            oldFreq = freqs.get(val, 0)
            newFreq = oldFreq + 1
            freqs[val] = newFreq

            if oldFreq > 0:
                removeItem((oldFreq, val))

            addItem((newFreq, val))

        def removeVal(val):
            nonlocal currentXSum, totalSum
            totalSum -= val
            oldFreq = freqs[val]
            newFreq = oldFreq - 1

            removeItem((oldFreq, val))

            if newFreq > 0:
                freqs[val] = newFreq
                addItem((newFreq, val))
            else:
                freqs.pop(val)

        for i in range(k):
            addVal(nums[i])

        if len(freqs) < x:
            results.append(totalSum)
        else:
            results.append(currentXSum)

        for i in range(k, len(nums)):
            removeVal(nums[i - k])
            addVal(nums[i])

            if len(freqs) < x:
                results.append(totalSum)
            else:
                results.append(currentXSum)

        return results
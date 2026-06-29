# Leetcode 3960: Frequency Balance Subarray
# https://leetcode.com/problems/frequency-balance-subarray/
# Solved on 29th of June, 2026
class Solution:
    def getLength(self, nums: list[int]) -> int:
        """
        Computes the length of the longest frequency-balanced subarray.
        A frequency-balanced subarray is a subarray where the count of each
        distinct element is equal to the square of some integer k, or the count
        of one element is double the count of another element.
        
        @param nums: The input array of integers.
        @return: The length of the longest frequency-balanced subarray.
        """
        maxLength = 1
        numElements = len(nums)
        for startIndex in range(numElements):
            elementCounts = {}
            freqCounts = {}
            for endIndex in range(startIndex, numElements):
                currentNum = nums[endIndex]
                if currentNum in elementCounts:
                    oldFreq = elementCounts[currentNum]
                    freqCounts[oldFreq] -= 1
                    if freqCounts[oldFreq] == 0:
                        del freqCounts[oldFreq]
                    elementCounts[currentNum] += 1
                else:
                    elementCounts[currentNum] = 1

                newFreq = elementCounts[currentNum]
                freqCounts[newFreq] = freqCounts.get(newFreq, 0) + 1

                if len(elementCounts) == 1:
                    if endIndex - startIndex + 1 > maxLength:
                        maxLength = endIndex - startIndex + 1
                elif len(freqCounts) == 2:
                    freqList = list(freqCounts.keys())
                    firstFreq = freqList[0]
                    secondFreq = freqList[1]
                    if firstFreq > secondFreq:
                        firstFreq, secondFreq = secondFreq, firstFreq
                    if secondFreq == 2 * firstFreq:
                        if endIndex - startIndex + 1 > maxLength:
                            maxLength = endIndex - startIndex + 1
        
        return maxLength
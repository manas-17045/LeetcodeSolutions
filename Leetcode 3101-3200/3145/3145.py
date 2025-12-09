# Leetcode 3145: Find Products of Elements of Big Array
# https://leetcode.com/problems/find-products-of-elements-of-big-array/
# Solved on 9th of December, 2025
class Solution:
    def findProductOfElements(self, queries: list[list[int]]) -> list[int]:
        """
        Finds the product of elements in a "big array" for given queries.
        :param queries: A list of queries, where each query is [startIdx, endIdx, mod].
        :return: A list of integers, where each element is the product modulo mod for the corresponding query.
        """
        def countSetBits(n):
            count = 0
            for i in range(55):
                block = 1 << (i + 1)
                half = 1 << i
                fullCycles = (n + 1) // block
                count += fullCycles * half
                remainder = (n + 1) % block
                if remainder > half:
                    count += remainder - half
            return count

        def sumPowers(n):
            totalSum = 0
            for i in range(55):
                block = 1 << (i + 1)
                half = 1 << i
                fullCycles = (n + 1) // block
                currCount = fullCycles * half
                remainder = (n + 1) % block
                if remainder > half:
                    currCount += remainder - half
                totalSum += currCount * i
            return totalSum

        def getNum(index):
            low, high = 1, 10 ** 15
            ans = 1
            while low <= high:
                mid = (low + high) // 2
                if countSetBits(mid) > index:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        res = []
        for startIdx, endIdx, mod in queries:
            startNum = getNum(startIdx)
            endNum = getNum(endIdx)

            totalPower = 0

            startNumBits = []
            for i in range(55):
                if (startNum >> i) & 1:
                    startNumBits.append(i)

            prevCountStart = countSetBits(startNum - 1)
            startOffset = startIdx - prevCountStart

            if startNum == endNum:
                endOffset = endIdx - prevCountStart
                for i in range(startOffset, endOffset + 1):
                    totalPower += startNumBits[i]
            else:
                for i in range(startOffset, len(startNumBits)):
                    totalPower += startNumBits[i]

                if endNum > startNum + 1:
                    totalPower += sumPowers(endNum - 1) - sumPowers(startNum)

                endNumBits = []
                for i in range(55):
                    if (endNum >> i) & 1:
                        endNumBits.append(i)

                prevCountEnd = countSetBits(endNum - 1)
                endOffset = endIdx - prevCountEnd
                for i in range(endOffset + 1):
                    totalPower += endNumBits[i]

            res.append(pow(2, totalPower, mod))

        return res
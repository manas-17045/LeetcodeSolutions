# Leetcode 3966: Count Good Integers in a Range
# https://leetcode.com/problems/count-good-integers-in-a-range/
# Solved on 9th of July, 2026
class Solution:
    def goodIntegers(self, l: int, r: int, k: int) -> int:
        """
        Returns the count of good integers in the range [l, r].
        A good integer is an integer where the absolute difference between any two
        adjacent digits is at most k.
        
        @param l The lower bound of the range (inclusive).
        @param r The upper bound of the range (inclusive).
        @param k The maximum allowed absolute difference between adjacent digits.
        @return The count of good integers in the range [l, r].
        """
        def countValid(numLimit: int) -> int:
            numStr = str(numLimit)
            strLen = len(numStr)
            cacheMap = {}

            def computeWays(currIdx: int, prevDigit: int, isBound: bool, isLeadingZero: bool) -> int:
                if currIdx == strLen:
                    return 1

                stateKey = (currIdx, prevDigit, isBound, isLeadingZero)
                if stateKey in cacheMap:
                    return cacheMap[stateKey]
                
                maxDigit = int(numStr[currIdx]) if isBound else 9
                validCount = 0

                for currentChoice in range(maxDigit + 1):
                    nextBound = isBound and (currentChoice == maxDigit)

                    if isLeadingZero:
                        if currentChoice == 0:
                            validCount += computeWays(currIdx + 1, -1, nextBound, True)
                        else:
                            validCount += computeWays(currIdx + 1, currentChoice, nextBound, False)
                    else:
                        if abs(currentChoice - prevDigit) <= k:
                            validCount += computeWays(currIdx + 1, currentChoice, nextBound, False)

                cacheMap[stateKey] = validCount
                return validCount

            return computeWays(0, -1, True, True)

        return countValid(r) - countValid(l - 1)
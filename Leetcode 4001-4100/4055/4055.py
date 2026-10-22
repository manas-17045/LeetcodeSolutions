# Leetcode 4055: Count Shadow Pairs II
# https://leetcode.com/problems/count-shadow-pairs-ii/
# Solved on 22nd of October, 2026
class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        """
        Calculates the total number of shadow pairs in the given integer array.

        Parameters:
            nums (list[int]): A list of integers.

        Returns:
            int: The total count of valid shadow pairs.
        """
        sortedUnique = sorted(set(nums))
        maxRank = len(sortedUnique)
        rankMap = {val: idx + 1 for idx, val in enumerate(sortedUnique)}
        mappedNums = [rankMap[val] for val in nums]

        bitShift = 17
        bitMask = (1 << bitShift) - 1

        minFenwick = [maxRank + 1] * (maxRank + 2)
        maxFenwick = [0] * (maxRank + 2)
        countFenwick = [0] * (maxRank + 2)

        def solve(left: int, right: int) -> int:
            if right - left <= 1:
                return 0
            if right - left == 2:
                return 1 if mappedNums[left] < mappedNums[left + 1] else 0

            mid = (left + right) >> 1
            totalPairs = solve(left, mid) + solve(mid, right)

            leftAdd = []
            leftRem = []

            for idx in range(mid - 1, left - 1, -1):
                currVal = mappedNums[idx]
                treePos = maxRank - currVal
                nextGreater = maxRank + 1
                while treePos > 0:
                    if minFenwick[treePos] < nextGreater:
                        nextGreater = minFenwick[treePos]
                    treePos &= treePos - 1

                treePos = maxRank - currVal + 1
                while treePos <= maxRank:
                    if currVal < minFenwick[treePos]:
                        minFenwick[treePos] = currVal
                    treePos += treePos & -treePos

                leftAdd.append((currVal << bitShift) | nextGreater)
                if nextGreater <= maxRank:
                    leftRem.append((nextGreater << bitShift) | currVal)

            for idx in range(left, mid):
                treePos = maxRank - mappedNums[idx] + 1
                while treePos <= maxRank:
                    if minFenwick[treePos] == maxRank + 1:
                        break
                    minFenwick[treePos] = maxRank + 1
                    treePos += treePos & -treePos

            rightItems = []

            for idx in range(mid, right):
                currVal = mappedNums[idx]
                treePos = currVal - 1
                prevSmaller = 0
                while treePos > 0:
                    if maxFenwick[treePos] > prevSmaller:
                        prevSmaller = maxFenwick[treePos]
                    treePos &= treePos - 1

                treePos = currVal
                while treePos <= maxRank:
                    if currVal > maxFenwick[treePos]:
                        maxFenwick[treePos] = currVal
                    treePos += treePos & -treePos

                rightItems.append((currVal << bitShift) | prevSmaller)

            for idx in range(mid, right):
                treePos = mappedNums[idx]
                while treePos <= maxRank:
                    if maxFenwick[treePos] == 0:
                        break
                    maxFenwick[treePos] = 0
                    treePos += treePos & -treePos

            leftAdd.sort()
            leftRem.sort()
            rightItems.sort()

            addIdx = 0
            remIdx = 0
            addLen = len(leftAdd)
            remLen = len(leftRem)
            activeCount = 0

            for packedItem in rightItems:
                currVal = packedItem >> bitShift
                lowerBound = packedItem & bitMask

                while addIdx < addLen and (leftAdd[addIdx] >> bitShift) < currVal:
                    treePos = leftAdd[addIdx] >> bitShift
                    while treePos <= maxRank:
                        countFenwick[treePos] += 1
                        treePos += treePos & -treePos
                    activeCount += 1
                    addIdx += 1

                while remIdx < remLen and (leftRem[remIdx] >> bitShift) < currVal:
                    treePos = leftRem[remIdx] & bitMask
                    while treePos <= maxRank:
                        countFenwick[treePos] -= 1
                        treePos += treePos & -treePos
                    activeCount -= 1
                    remIdx += 1

                if activeCount > 0:
                    if lowerBound <= 1:
                        totalPairs += activeCount
                    else:
                        lessCount = 0
                        treePos = lowerBound - 1
                        while treePos > 0:
                            lessCount += countFenwick[treePos]
                            treePos &= treePos - 1
                        totalPairs += activeCount - lessCount

            if addIdx > 0:
                lastVal = rightItems[-1] >> bitShift
                for idx in range(addIdx):
                    if (leftAdd[idx] & bitMask) >= lastVal:
                        treePos = leftAdd[idx] >> bitShift
                        while treePos <= maxRank:
                            countFenwick[treePos] -= 1
                            treePos += treePos & -treePos

            return totalPairs

        return solve(0, len(mappedNums))
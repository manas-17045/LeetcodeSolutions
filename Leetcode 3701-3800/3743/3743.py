# Leetcode 3743: Maximize Cyclic Partition Score
# https://leetcode.com/problems/maximize-cyclic-partition-score/
# Solved on 2nd of September, 2026
class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum cyclic partition score by partitioning nums into at
        most k subarrays and summing the range (maximum minus minimum) of each subarray.

        Parameters:
            nums (list[int]): The cyclic array of integers.
            k (int): The maximum number of contiguous subarrays allowed.

        Returns:
            int: The maximum possible total partition score.
        """
        totalElements = len(nums)
        maxPicks = min(2 * k, totalElements)
        maxScore = 0
        negInf = float("-inf")

        for startBalance in (0, 1, 2):
            currDp0 = [negInf] * (maxPicks + 1)
            currDp1 = [negInf] * (maxPicks + 1)
            currDp2 = [negInf] * (maxPicks + 1)

            if startBalance == 0:
                currDp0[0] = 0
            elif startBalance == 1:
                currDp1[0] = 0
            else:
                currDp2[0] = 0

            currMaxPicks = 0

            for currentVal in nums:
                currMaxPicks = min(maxPicks, currMaxPicks + 1)
                nextDp0 = list(currDp0)
                nextDp1 = list(currDp1)
                nextDp2 = list(currDp2)

                for pickCount in range(currMaxPicks):
                    val0 = currDp0[pickCount]
                    val1 = currDp1[pickCount]
                    val2 = currDp2[pickCount]
                    nextPick = pickCount + 1

                    if val0 != negInf:
                        cand = val0 + currentVal
                        if cand > nextDp1[nextPick]:
                            nextDp1[nextPick] = cand

                    if val1 != negInf:
                        cand0 = val1 - currentVal
                        if cand0 > nextDp0[nextPick]:
                            nextDp0[nextPick] = cand0
                        cand2 = val1 + currentVal
                        if cand2 > nextDp2[nextPick]:
                            nextDp2[nextPick] = cand2

                    if val2 != negInf:
                        cand = val2 - currentVal
                        if cand > nextDp1[nextPick]:
                            nextDp1[nextPick] = cand

                currDp0 = nextDp0
                currDp1 = nextDp1
                currDp2 = nextDp2

            finalDp = currDp0 if startBalance == 0 else (currDp1 if startBalance == 1 else currDp2)

            for pickCount in range(0, maxPicks + 1, 2):
                if finalDp[pickCount] > maxScore:
                    maxScore = finalDp[pickCount]

        return maxScore
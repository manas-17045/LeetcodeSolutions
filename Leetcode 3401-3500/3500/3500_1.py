# Leetcode 3500: Minimum Cost to Divide Array into Subarrays
# https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/
# Solved on 2nd of June, 2025
import collections


class Solution:
    def minimumCost(self, nums: list[int], cost: list[int], k: int) -> int:
        """
        Calculates the minimum cost to divide the array `nums` into `k` subarrays.

        The cost of dividing the array at index `i` is `cost[i]`. The total cost
        of a division is the sum of the costs of the division points.

        This problem can be solved using dynamic programming with convex hull trick
        optimization.

        Args:
            nums: A list of integers.
            cost: A list of integers representing the cost of dividing at each index.
            k: The number of subarrays to divide the array into.
        """
        N = len(nums)

        psNums = [0] * (N + 1)
        psCost = [0] * (N + 1)

        for i in range(N):
            psNums[i + 1] = psNums[i] + nums[i]
            psCost[i + 1] = psCost[i] + cost[i]

        dpPrev = [float('inf')] * (N + 1)
        dpPrev[0] = 0

        minTotalCostAtN = float('inf')

        for sCount in range(1, N + 1):
            dpCurr = [float('inf')] * (N + 1)
            dq = collections.deque()

            def addLineToDq(jNewIdx):
                bNew = dpPrev[jNewIdx]
                if bNew == float('inf'):
                    # This path is impossible, do not add line
                    return

                mNew = -psCost[jNewIdx]

                # main convex hull: remove lines that become non-optimal
                while len(dq) >= 2:
                    m1, b1 = dq[-2]
                    m2, b2 = dq[-1]

                    # Remove L2 if Intersection(L1, L2) >= Intersection(L2, L_new)
                    if (b2 - b1) * (m2 - mNew) >= (bNew - b2) * (m1 - m2):
                        dq.pop()
                    else:
                        break

                dq.append((mNew, bNew))

            def queryDq(xQuery):
                # Remove lines from front that are no longer optimal
                while len(dq) >= 2:
                    m1, b1 = dq[0]
                    m2, b2 = dq[1]

                    val1 = m1 * xQuery + b1
                    val2 = m2 * xQuery + b2

                    if val1 >= val2:
                        dq.popleft()
                    else:
                        break

                mOpt, bOpt = dq[0]
                return mOpt * xQuery + bOpt

            initialJForLine = sCount - 1
            addLineToDq(initialJForLine)

            for i in range(sCount, N + 1):
                xQuery = psNums[i] + k * sCount
                minValFromLines = queryDq(xQuery)

                dpCurr[i] = xQuery * psCost[i] + minValFromLines

                if i < N:
                    addLineToDq(i)

            if dpCurr[N] != float('inf'):
                minTotalCostAtN = min(minTotalCostAtN, dpCurr[N])

            dpPrev = dpCurr

        return minTotalCostAtN
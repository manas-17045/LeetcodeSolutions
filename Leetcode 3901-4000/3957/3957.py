# Leetcode 3957: Maximum Sum of M Non-Overlapping Subarrays II
# https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/
# Solved on 27th of June, 2026
import collections

class Solution:
    def maximumSum(self, nums: list[int], m: int, l: int, r: int) -> int:
        """
        This problem asks for the maximum sum of m non-overlapping subarrays, each of length between l and r (inclusive).

        @param nums: array of integers
        @param m: number of non-overlapping subarrays
        @param l: minimum length of each subarray
        @param r: maximum length of each subarray
        @return: maximum sum of m non-overlapping subarrays of length between l and r (inclusive)
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        singleDeque = collections.deque()
        maxSingleSum = -float('inf')
        for i in range(1, n + 1):
            j = i - l
            if j >= 0:
                while singleDeque and prefix[singleDeque[-1]] >= prefix[j]:
                    singleDeque.pop()
                singleDeque.append(j)
            while singleDeque and singleDeque[0] < i - r:
                singleDeque.popleft()
            if singleDeque:
                if prefix[i] - prefix[singleDeque[0]] > maxSingleSum:
                    maxSingleSum = prefix[i] - prefix[singleDeque[0]]

        if maxSingleSum <= 0:
            return int(maxSingleSum)

        def evaluatePenalty(penalty):
            dp = [0] * (n + 1)
            cnt = [0] * (n + 1)
            valArray = [0] * (n + 1)
            deque = collections.deque()

            for i in range(1, n + 1):
                j = i - l
                if j >= 0:
                    curVal = dp[j] - prefix[j]
                    valArray[j] = curVal
                    curCnt = cnt[j]
                    while deque:
                        backIdx = deque[-1]
                        if curVal > valArray[backIdx] or (curVal == valArray[backIdx] and curCnt <= cnt[backIdx]):
                            deque.pop()
                        else:
                            break
                    deque.append(j)
                    
                while deque and deque[0] < i - r:
                    deque.popleft()

                curDp = dp[i - 1]
                curCount = cnt[i - 1]

                if deque:
                    bestIdx = deque[0]
                    candVal = valArray[bestIdx] + prefix[i] - penalty
                    candCnt = cnt[bestIdx] + 1

                    if candVal > curDp or (candVal == curDp and candCnt < curCount):
                        curDp = candVal
                        curCount = curCount

                dp[i] = curDp
                cnt[i] = curCount

            return dp[n], cnt[n]

        valZero, cntZero = evaluatePenalty(0)
        if cntZero <= m:
            return valZero

        left = 0
        right = sum(x for x in nums if x > 0)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            val, count = evaluatePenalty(mid)
            if count <= m:
                ans = val + mid * m
                right = mid - 1
            else:
                left = mid + 1
                
        return ans
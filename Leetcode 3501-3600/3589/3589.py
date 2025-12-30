# Leetcode 3589: Count Prime-Gap Balanced Subarrays
# https://leetcode.com/problems/count-prime-gap-balanced-subarrays/
# Solved on 30th of December, 2025
import collections


class Solution:
    def primeSubarray(self, nums: list[int], k: int) -> int:
        """
        Counts the number of prime-gap balanced subarrays.

        A subarray is prime-gap balanced if the difference between the maximum and minimum prime numbers
        within the subarray is at most k.

        Args:
            nums: A list of integers.
            k: The maximum allowed difference between the maximum and minimum prime numbers in a subarray.

        Returns:
            The number of prime-gap balanced subarrays.
        """
        if not nums:
            return 0

        maxVal = max(nums)
        if maxVal < 2:
            return 0

        isPrime = [True] * (maxVal + 1)
        isPrime[0] = isPrime[1] = False
        for i in range(2, int(maxVal ** 0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, maxVal + 1, i):
                    isPrime[j] = False

        primes = []
        for i, x in enumerate(nums):
            if isPrime[x]:
                primes.append((x, i))

        m = len(primes)
        if m < 2:
            return 0

        leftGaps = [0] * m
        for i in range(m):
            prevIdx = -1 if i == 0 else primes[i - 1][1]
            leftGaps[i] = primes[i][1] - prevIdx

        prefixLeft = [0] * (m + 1)
        for i in range(m):
            prefixLeft[i + 1] = prefixLeft[i] + leftGaps[i]

        ans = 0
        left = 0
        minQ = collections.deque()
        maxQ = collections.deque()
        n = len(nums)

        for right in range(m):
            val = primes[right][0]

            while maxQ and primes[maxQ[-1]][0] <= val:
                maxQ.pop()
            maxQ.append(right)

            while minQ and primes[minQ[-1]][0] >= val:
                minQ.pop()
            minQ.append(right)

            while primes[maxQ[0]][0] - primes[minQ[0]][0] > k:
                left += 1
                if maxQ[0] < left:
                    maxQ.popleft()
                if minQ[0] < left:
                    minQ.popleft()

            if left < right:
                waysStart = prefixLeft[right] - prefixLeft[left]

                nextIdx = n if right == m - 1 else primes[right + 1][1]
                waysEnd = nextIdx - primes[right][1]

                ans += waysStart * waysEnd

        return ans
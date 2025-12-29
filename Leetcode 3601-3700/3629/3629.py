# Leetcode 3629: Minimum Jumps to Reach End via Prime Teleportation
# https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/
# Solved on 29th of December, 2025
import collections


class Solution:
    def minJumps(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of jumps required to reach the end of the array.

        Args:
            nums: A list of integers representing the values at each position.
        Returns:
            The minimum number of jumps to reach the end, or -1 if it's not possible.
        """
        n = len(nums)
        if n <= 1:
            return 0

        maxVal = 0
        for num in nums:
            if num > maxVal:
                maxVal = num

        spf = list(range(maxVal + 1))
        for i in range(2, int(maxVal ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, maxVal + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        primeGroups = [[] for _ in range(maxVal + 1)]
        for i, num in enumerate(nums):
            temp = num
            while temp > 1:
                p = spf[temp]
                primeGroups[p].append(i)
                while temp % p == 0:
                    temp //= p

        dist = [-1] * n
        dist[0] = 0
        queue = collections.deque([0])
        visitedPrimes = [False] * (maxVal + 1)

        while queue:
            u = queue.popleft()
            if u == n - 1:
                return dist[u]

            neighbors = []
            if u - 1 >= 0:
                neighbors.append(u - 1)
            if u + 1 < n:
                neighbors.append(u + 1)

            val = nums[u]
            if val > 1 and spf[val] == val:
                if not visitedPrimes[val]:
                    visitedPrimes[val] = True
                    for v in primeGroups[val]:
                        neighbors.append(v)

            for v in neighbors:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)

        return -1
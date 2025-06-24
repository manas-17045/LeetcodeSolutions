# Leetcode 2818: Apply Operations to Maximize Score
# https://leetcode.com/problems/apply-operations-to-maximize-score/
# Solved on 29th of March, 2025
import heapq

MOD = 10**9 + 7

class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum score based on given rules of frequencies and prime scores.
        It uses a heap to calculate the result efficiently. The function computes auxiliary
        structures like prime scores, previous greater or equal indexes, and next greater
        indexes to determine frequencies, followed by processing the data with a priority queue.

        :param nums: List of integers from which calculations are performed.
        :type nums: list[int]
        :param k: The target number of operations or the number of scores to consider.
        :type k: int
        :return: The calculated maximum score based on the given rules.
        :rtype: int
        """
        n = len(nums)

        def getPrimeScore(x: int) -> int:
            """
            A class that provides a method to compute the maximum score of a subarray
            in a list of integers based on a given scoring technique.

            This class includes an inner function to calculate the prime score of an
            integer, which is used in calculating the overall score.

            Attributes:
                None
            """
            if x < 2:
                return 0

            score = 0
            factor = 2
            while factor * factor <= x:
                if x % factor == 0:
                    score += 1
                    while x % factor == 0:
                        x //= factor
                factor += 1
            if x > 1:
                score += 1
            return score

        prime_scores = [getPrimeScore(x) for x in nums]

        next_greater = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and prime_scores[i] >= prime_scores[stack[-1]]:
                stack.pop()
            next_greater[i] = stack[-1] if stack else n
            stack.append(i)

        prev_greater_or_equal = [-1] * n
        stack = []

        for i in range(n):
            while stack and prime_scores[i] >= prime_scores[stack[-1]]:
                stack.pop()
            prev_greater_or_equal[i] = stack[-1] if stack else -1
            stack.append(i)

        freq = [
            (i - prev_greater_or_equal[i]) * (next_greater[i] - i) for i in range(n)
        ]

        heap = []
        for i in range(n):
            heapq.heappush(heap, (-nums[i], freq[i]))

        result = 1
        while k > 0 and heap:
            neg_val, count = heapq.heappop(heap)
            val = -neg_val
            take = min(k, count)
            result = (result * pow(val, take, MOD)) % MOD
            k -= take

        return result
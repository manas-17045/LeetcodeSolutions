# Leetcode 2818: Apply Operations to Maximize Score
# https://leetcode.com/problems/apply-operations-to-maximize-score/
# Solved on 24th of June, 2025
class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum score achievable by applying operations on a given array `nums`.

        The score is calculated by multiplying `k` chosen numbers, each raised to the power of
        how many times it is chosen. The operations involve selecting a subarray and choosing
        an index `i` within it. The number `nums[i]` can be chosen if its prime score is
        greater than or equal to the prime scores of all other elements in the chosen subarray.
        The prime score of a number is the count of its distinct prime factors.

        The problem asks to maximize the product of `k` chosen numbers, modulo 10^9 + 7.

        Args:
            nums: A list of integers.
            k: The number of operations to perform (i.e., the number of elements to choose).

        Returns:
            The maximum score achievable, modulo 10^9 + 7.
        """
        mod = 10**9 + 7
        n = len(nums)

        if n == 0:
            # According to typical interpretations, empty product is 1.
            return 1

        maxValInNums = 0
        for x in nums:
            if x > maxValInNums:
                maxValInNums = x

        smallestPrimeFactor = list(range(maxValInNums + 1))
        for i in range(2, int(maxValInNums**0.5) + 1):
            if smallestPrimeFactor[i] == i:
                for j in range(i * i, (maxValInNums + 1), i):
                    if smallestPrimeFactor[j] == j:
                        smallestPrimeFactor[j] = i

        primeScoreArr = [0] * (maxValInNums + 1)
        if maxValInNums >= 1:
            primeScoreArr[1] = 0

        for xVal in range(2, (maxValInNums + 1)):
            num = xVal
            distinctFactors = set()
            while num > 1:
                distinctFactors.add(smallestPrimeFactor[num])
                num //= smallestPrimeFactor[num]
            primeScoreArr[xVal] = len(distinctFactors)

        actualPrimeScores = [0] * n
        for i in range(n):
            actualPrimeScores[i] = primeScoreArr[nums[i]]

        prevGreaterEqualScores = [-1] * n
        stack = []
        for i in range(n):
            while stack and actualPrimeScores[stack[-1]] < actualPrimeScores[i]:
                stack.pop()
            if stack:
                prevGreaterEqualScores[i] = stack[-1]
            stack.append(i)

        nextGreaterScores = [n] * n
        stack = []
        for i in range((n - 1), -1, -1):
            while stack and actualPrimeScores[stack[-1]] <= actualPrimeScores[i]:
                stack.pop()
            if stack:
                nextGreaterScores[i] = stack[-1]
            stack.append(i)

        candidates = []
        for i in range(n):
            val = nums[i]
            leftChoices = i - prevGreaterEqualScores[i]
            rightChoices = nextGreaterScores[i] - i
            count = leftChoices * rightChoices

            if count > 0:
                candidates.append((val, count))

        candidates.sort(key=lambda x: x[0], reverse=True)

        score = 1
        remainingK = k
        for val, cnt in candidates:
            if remainingK == 0:
                break

            opsToMake = min(remainingK, cnt)

            term = pow(val, opsToMake, mod)
            score = (score * term) % mod
            remainingK -= opsToMake

        return score
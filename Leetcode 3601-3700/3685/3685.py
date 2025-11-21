# Leetcode 3685: Subsequence Sum After Capping Elements
# https://leetcode.com/problems/subsequence-sum-after-capping-elements/
# Solved on 22nd of November, 2025
class Solution:
    def subsequenceSumAfterCapping(self, nums: list[int], k: int) -> list[bool]:
        """
        Determines for each possible cap value `x` if there exists a subsequence of `nums`
        whose sum, after capping each element at `x`, equals `k`.
        :param nums: A list of integers.
        :param k: The target sum.
        :return: A list of booleans, where `answer[x-1]` is true if such a subsequence exists for cap `x`.
        """
        n = len(nums)
        freq = [0] * (n + 1)
        for num in nums:
            freq[num] += 1

        dp = 1
        mask = (1 << (k + 1)) - 1
        processedCount = 0
        answer = []

        for x in range(1, n + 1):
            cappedCount = n - processedCount
            possible = False

            limit = min(k, cappedCount * x)

            for val in range(0, limit + 1, x):
                rem = k - val
                if (dp >> rem) & 1:
                    possible = True
                    break

            answer.append(possible)

            count = freq[x]
            if count > 0:
                for _ in range(count):
                    dp |= (dp << x)
                dp &= mask

            processedCount += count

        return answer
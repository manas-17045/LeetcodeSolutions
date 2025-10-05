# Leetcode 3352: Count K-Reducible Numbers Less Than N
# https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/
# Solved on 5th of October, 2025
class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        """
        Counts the number of k-reducible binary numbers strictly less than the given binary string s.
        A number is k-reducible if the number of operations to reduce its set bits count to 1 is less than k.
        :param s: A string representing a binary number.
        :param k: An integer representing the maximum allowed operations for k-reducibility.
        :return: The count of k-reducible binary numbers strictly less than s, modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        n = len(s)

        # Precompute the number of operations needed to reduce each count to 1
        # Max set bits = 800 (length of s)
        max_bits = n
        ops = [0] * (max_bits + 1)

        for i in range(2, max_bits + 1):
            # Count set bits in i
            set_bits = bin(i).count('1')
            ops[i] = ops[set_bits] + 1

        # Memoization for digit DP
        memo = {}

        def dp(pos, cnt, tight):
            if pos == n:
                # We've formed a number with 'cnt' set bits
                # Check if it's positive (cnt > 0) and k-reducible
                if cnt == 0:
                    return 0
                return 1 if ops[cnt] < k else 0

            if (pos, cnt, tight) in memo:
                return memo[(pos, cnt, tight)]

            # Determine the maximum digit we can place at this position
            limit = int(s[pos]) if tight else 1

            result = 0
            for digit in range(0, limit + 1):
                new_tight = tight and (digit == limit)
                new_cnt = cnt + digit
                result = (result + dp(pos + 1, new_cnt, new_tight)) % MOD

            memo[(pos, cnt, tight)] = result
            return result

        # Start from position 0, with 0 set bits, and tight constraint
        # Subtract 1 because we need numbers less than n (not including n itself)
        answer = dp(0, 0, True)

        # We need to exclude n itself, so check if n is k-reducible
        n_setBits = s.count('1')
        if n_setBits > 0 and ops[n_setBits] < k:
            answer = (answer - 1 + MOD) % MOD

        return answer
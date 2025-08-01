# Leetcode 3463: Check If Digits Are Equal in String After Operations II
# https://leetcode.com/problems/check-if-digits-are-equal-after-operations-ii/
# Solved on 1st of August, 2025
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        """
        Determines if a given string `s` satisfies a specific mathematical condition related to its digits.

        Args:
            s (str): The input string consisting of digits.
        Returns:
            bool: True if the condition is met, False otherwise.
        """
        N = len(s)
        digits = [int(c) for c in s]

        if N < 3:
            return N == 2 and digits[0] == digits[1]
        
        n = N - 3

        sum_mod_2 = 0
        for j in range(n + 1):
            if (j & n) == j:
                term = (digits[j] - digits[j + 2])
                sum_mod_2 = (sum_mod_2 + term) % 2
                
        if sum_mod_2 != 0:
            return False
        
        C_mod5 = [[0] * 5 for _ in range(5)]
        for i in range(5):
            C_mod5[i][0] = 1
            for i in range(1, (i + 1)):
                C_mod5[i][j] = (C_mod5[i - 1][j - 1] + C_mod5[i - 1][j]) % 5

        def get_binom_mod_5(n_val: int, k_val: int) -> int:
            if k_val < 0 or k_val > n_val:
                return 0
            
            res = 1
            while n_val > 0 or k_val > 0:
                ni = n_val % 5
                ki = k_val % 5
                res = (res * C_mod5[ni][ki]) % 5
                n_val //= 5
                k_val //= 5

            return res
        
        sum_mod_5 = 0
        for j in range(n + 1):
            coeff = get_binom_mod_5(n, j)
            if coeff == 0:
                continue
            term = (digits[j] - digits[j + 2])
            sum_mod_5 = (sum_mod_5 + coeff * term) % 5

        if sum_mod_5 != 0:
            return False
        
        # If the condition holds for both mod 2 and mod 5, it holds for mod 10.
        return True
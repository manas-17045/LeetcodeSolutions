# Leetcode 3337: Toral Characters in String After Transformations II
# https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        """
        Calculates the total number of characters in a string after applying a series of transformations.

        Args:
            s: The input string consisting of lowercase English letters.
            t: The number of transformations to apply.
            nums: A list of 26 integers, where nums[i] represents the span for the transformation of the ith letter (a=0, b=1, ..., z=25).
                  A letter transforms into the next `span` letters in the alphabet (circularly).

        Returns:
            The total number of characters in the string after `t` transformations, modulo 10^9 + 7.

        """
        MOD = 10**9 + 7

        # If no transformations, length is just the original string length
        if t == 0:
            return len(s) % MOD

        # Build initial frequency vector of letters in s
        # f0[i] = count of chr(ord('a') + i) in s
        f0 = [0] * 26
        for ch in s:
            f0[ord(ch) - 97] += 1

        # Build the 26×26 transition matrix M
        # M[i][j] = number of times letter i appears when letter j is transfomed once
        M = [[0] * 26 for _ in range(26)]
        for j in range(26):
            span = nums[j]
            # letter j transforms into the next `span` letters in the cycle
            for k in range(1, span + 1):
                i = (j + k) % 26
                M[i][j] = 1

        # matrix multiplication (26×26 × 26×26)
        def mat_mult(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
            C = [[0] * 26 for _ in range(26)]
            for i in range(26):
                Ai = A[i]
                Ci = C[i]
                for k in range(26):
                    if Ai[k]:
                        aik = Ai[k]
                        Bk = B[k]
                        # Accumulate aik * Bk[j] into Ci[j]
                        for j in range(26):
                            Ci[j] = (Ci[j] + aik * Bk[j]) % MOD
            return C

        # matrix-vector multiplication (26×26 × 26)
        def mat_vec(mat: list[list[int]], vec: list[int]) -> list[int]:
            out = [0] * 26
            for i in range(26):
                total = 0
                Mi = mat[i]
                for j in range(26):
                    if Mi[j] and vec[j]:
                        total += Mi[j] * vec[j]
                out[i] = total % MOD
            return out

        # Fast exponentiation of matrix M^exp
        def mat_pow(mat: list[list[int]], exp: int) -> list[list[int]]:
            # Identity
            res = [[1 if i == j else 0 for j in range(26)] for i in range(26)]
            base = mat
            while exp > 0:
                if exp & 1:
                    res = mat_mult(res, base)
                base = mat_mult(base, base)
                exp >>= 1
            return res

        # Comput M^t
        Mt = mat_pow(M, t)

        # Apply to initial freq vector
        ft = mat_vec(Mt, f0)

        # Total length = sum of all letter-counts after t transformations
        return sum(ft) % MOD
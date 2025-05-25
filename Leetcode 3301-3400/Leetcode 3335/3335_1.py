# Leetcode 3335: Total Characters in String After Transformations I
# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/
# Solved on 13th of May, 2025

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        """
        Calculates the total number of characters in a string after applying a series of transformations.

        The transformation rule is as follows:
        - Each character in the string is shifted to the next character in the alphabet (a -> b, b -> c, ..., y -> z).
        - The character 'z' is replaced by the string "ab".

        Args:
            s: The initial string.
            t: The number of transformations to apply.
        """
        MOD = 10**9 + 7

        # edge-case: zero transformations leaves the string as is
        if t == 0:
            return len(s)

        # build initial frequency vector f0 of size 26
        f0 = [0] * 26
        for ch in s:
            f0[ord(ch) - 97] += 1

        # Build the 26×26 transition matrix M:
        # - For 0 <= j < 25: each letter j -> j + 1
        # - For j = 25 ('z'): it produces one 'a' (0) and one 'b' (1)
        M = [[0] * 26 for _ in range(26)]
        for j in range(25):
            M[j + 1][j] = 1
        M[0][25] = 1
        M[1][25] = 1

        # Matrix multiplication (26×26 × 26×26)
        def mat_mult(A, B):
            C = [[0] * 26 for _ in range(26)]
            for i in range(26):
                Ai = A[i]
                Ci = C[i]
                for k in range(26):
                    if Ai[k]:
                        aik = Ai[k]
                        Bk = B[k]
                        for j in range(26):
                            Ci[j] = (Ci[j] + aik * Bk[j]) % MOD
            return C

        # Matrix-vector multiply (26×26 × 26)
        def mat_vec(M, v):
            out = [0] * 26
            for i in range(26):
                s = 0
                Mi = M[i]
                for j in range(26):
                    if Mi[j] and v[j]:
                        s += Mi[j] * v[j]
                out[i] = s % MOD
            return out

        # Fast exponentiation of M^t
        def mat_pow(mat, exp):
            # Start with identity
            res = [[1 if i == j else 0 for j in range(26)] for i in range(26)]
            base = mat
            while exp > 0:
                if exp & 1:
                    res = mat_mult(res, base)
                base = mat_mult(base, base)
                exp >>= 1
            return res

        Mt = mat_pow(M, t)
        ft = mat_vec(Mt, f0)

        # Total length is sum of all letter-counts after t steps
        return sum(ft) % MOD
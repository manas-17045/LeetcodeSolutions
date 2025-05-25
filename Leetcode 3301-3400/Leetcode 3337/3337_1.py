# Leetcode 3337: Total Characters in String After Transformations II
# https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

class Solution:
    N_CONST = 26
    MOD_CONST = 10**9 + 7

    def _multiply_matrices(self, A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
        C = [[0] * self.N_CONST for _ in range(self.N_CONST)]
        for i in range(self.N_CONST):
            for j in range(self.N_CONST):
                current_sum = 0
                # Calculate C[i][j] = sum(A[i][k_loop] * B[k_loop][j]) for k_loop from 0 to N_CONST - 1
                for k_loop in range(self.N_CONST):
                    current_sum = (current_sum + A[i][k_loop] * B[k_loop][j])
                C[i][j] = current_sum % self.MOD_CONST  # Apply modulo after adding all products for C[i][j]
        return C

    def _matrix_power(self, M: list[list[int]], p: int) -> list[list[int]]:
        # Initialize result as identity matrix
        res = [[0] * self.N_CONST for _ in range(self.N_CONST)]
        for i in range(self.N_CONST):
            res[i][i] = 1

            base = M    # Current power of M (starts at M^1)
            exponent = p

            while exponent > 0:
                if exponent % 2 == 1:   # If exponent is odd, multiply result by current base
                    res = self._multiply_matrices(res, base)
                # Square the base for the next iteration
                base = self._multiply_matrices(base, base)
                # Halve the exponent for the next iteration
                exponent //= 2
        return res

    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        """
        Calculates the total length of the string after applying transformations t times.

        Args:
            s: The initial string.
            t: The number of transformations to apply.
            nums: A list where nums[i] represents the number of characters that the i-th character (0-indexed) transforms into.

        Returns:
            The total length of the string after t transformations, modulo MOD_CONST.
        """

        if t == 0:
            # Length of s can be up to 10^5, MOD_CONST is 10^9 + 7
            # So, len(s) % MOD_CONST == len(s).
            return len(s)

        # Construct transformation matrix Tr
        # Tr[i][j] = number of times char j (target) is produced when char i (source) transforms once
        Tr = [[0] * self.N_CONST for _ in range(self.N_CONST)]
        for i in range(self.N_CONST):   # For each source character i (0 for 'a', etc.)
            num_chars_produced_by_i = nums[i]
            # current_char_code = i
            # This is the 0-indexed alphaber code of source char i

            # For each of the num_chars_produced_by_i characters that source char i turns into:
            for k_th_offset in range(num_chars_produced_by_i):
                # The k_th_offset character (0-indexed) in the sequence produced by char i
                # is the (i + 1 + k_th_offset)-th character in the alphabet (0-indexed, with wrap-around).
                target_char_idx = (i + 1 + k_th_offset) % self.N_CONST

                # Increment the count for Tr[source_char_idx][target_char_idx]
                Tr[i][target_char_idx] = (Tr[i][target_char_idx] + 1) % self.MOD_CONST

        # Calculate Tr^t using matrix exponentiation
        Tr_pow_t = self._matrix_power(Tr, t)

        # dp_t_lengths[i] will store L_t[i]: length from char i after t transformations.
        # L_t[i] is the sum of the i-th row of Tr_pow_t (because L_0 vector is all is).
        dp_t_lengths = [0] * self.N_CONST
        for i in range(self.N_CONST):
            # For each starting character i
            row_sum = 0
            # Sum elements of row i in Tr_pow_t
            for j in range(self.N_CONST):
                row_sum = (row_sum + Tr_pow_t[i][j]) % self.MOD_CONST
            dp_t_lengths[i] = row_sum

        # Calculate final total length by summing contributions from characters in the initial string s\
        total_final_length = 0
        for char_in_s in s:
            char_idx = ord(char_in_s) - ord('a')
            total_final_length = (total_final_length + dp_t_lengths[char_idx]) % self.MOD_CONST

        return total_final_length
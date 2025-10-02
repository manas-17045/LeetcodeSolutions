# Leetcode 3677: Count Binary Palindromic Numbers
# https://leetcode.com/problems/count-binary-palindromic-numbers/
# Solved on 1st of October, 2025
class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        """
        Counts the number of binary palindromes less than or equal to n.
        :param n: An integer.
        :return: The count of binary palindromes.
        """
        # Reverse the lowest `bits` bits of x
        def reverse_bits(x: int, bits: int) -> int:
            r = 0
            for _ in range(bits):
                r = (r << 1) | (x & 1)
                x >>= 1
            return r

        # Build a palindrome of total length L from a prefix (which is ceil(L/2) bits)
        def make_palindrome(prefix: int, L: int) -> int:
            if L == 1:
                return 1  # prefix is 1
            if L % 2 == 0:
                half = L // 2
                # Prefix is half bits
                return (prefix << half) | reverse_bits(prefix, half)
            else:
                half = (L + 1) // 2  # prefix size
                # Drop last (middle) bit when mirroring
                left_without_middle = prefix >> 1
                return (prefix << (half - 1)) | reverse_bits(left_without_middle, half - 1)

        # Special case for 0
        if n == 0:
            return 1

        count = 1  # include 0

        Lmax = n.bit_length()  # maximum bit length to consider (leading '1' at position Lmax-1)

        # Count all palindromes of lengths strictly less than Lmax
        for L in range(1, Lmax):
            prefix_size = (L + 1) // 2
            # Number of prefixes with MSB 1 and prefix_size bits = 2^(prefix_size-1)
            count += 1 << (prefix_size - 1)

        # For length == Lmax, we must count how many prefixes produce palindromes <= n
        p = (Lmax + 1) // 2  # prefix size for the top length
        # Get top p bits of n (the prefix)
        top_prefix = n >> (Lmax - p)
        pal_from_top = make_palindrome(top_prefix, Lmax)
        base = 1 << (p - 1)  # smallest prefix (MSB 1)
        if pal_from_top <= n:
            count += top_prefix - base + 1
        else:
            count += top_prefix - base

        return count
# Leetcode 2081: Sum of k-Mirror Numbers
# https://leetcode.com/problems/sum-of-k-mirror-numbers/
# Solved on 23rd of June, 2025
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        """
        Finds the sum of the `n` smallest "k-mirror" numbers.

            A k-mirror number is a positive integer that is a palindrome in both base-10 and base-k.

            Args:
                k (int): The base for the second palindrome check (2 <= k <= 9).
                n (int): The number of k-mirror numbers to find (1 <= n <= 30).
            Returns:
                int: The sum of the `n` smallest k-mirror numbers.
        """

        def is_pal_in_base(x: int, base: int) -> bool:
            """
            Checks if a given integer `x` is a palindrome when represented in the specified `base`.

            Args:
                x (int): The integer to check.
                base (int): The base for the palindrome check.
            Returns:
                bool: True if `x` is a palindrome in the given base, False otherwise.
            """
            # Convert x to digits in 'base' and check palindrome
            digs = []
            while x:
                digs.append(x % base)
                x //= base
            return digs == digs[::-1]

        ans = 0
        count = 0

        # Generate palindromes by length in Base-10, in ascending numeric order
        length = 1
        while count < n:
            # Determine how many digits we take as the "prefix"
            prefix_len = (length + 1) // 2
            start = 10**(prefix_len - 1)
            end = 10**prefix_len

            if prefix_len == 1:
                start = 1
                end = 10

            for prefix in range(start, end):
                s = str(prefix)
                # Build the full palindrome
                if length % 2 == 0:
                    pal = int(s + s[::-1])
                else:
                    # Skip the middle digit once
                    pal = int(s + s[-2::-1])

                # Check in Base-K
                if is_pal_in_base(pal, k):
                    ans += pal
                    count += 1
                    if count == n:
                        return ans

            length += 1

        return ans
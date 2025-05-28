# Leetcode 3272: Find the Count of Good Integers
# https://leetcode.com/problems/find-the-count-of-good-integers/
from collections import Counter


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        """
        Calculates the total number of good integers with specified conditions. A "good"
        integer is defined as an integer that is a palindrome with `n` digits and is
        divisible by `k`.

        The function generates all palindromic integers with `n` digits, checks the divisibility
        condition for each, and computes the count of unique valid digit permutations.

        :param n: The number of digits in the palindrome, must be a positive integer.
        :param k: The integer divisor, must be a positive integer.
        :return: The count of distinct "good integer" permutations that satisfy the conditions.

        """
        # Basic input validation
        if n <= 0:
            # No integers with 0 or negative digits exist in the standard manner.
            return 0

        if k <= 0:
            # Divisibility by 0 or negative numbers is often undefined or treated specially.
            # Assuming k must be positive based on typical programming contest constraints.
            # If k=0 is allowed, the behavior might need clarification (e.g., only 0 is divisible by 0?).
            return 0    # Or raise ValueError("k must be positive")

        # Precompute factorials up to n to use in permutation calculation
        # Python's integers handle arbitrary size, so overflow is not an issue for value,
        # but performance for extremely large n could be. Assume n is within resonable limits
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i

        # Helper function to calculate distinct permutations of a multiset of digits.
        # Formula: length! / (count_digits_0! * count_digit_1! * ...)
        def count_perms(counts: Counter, length: int) -> int:
            """
            Calculates distinct permutations of a multiset represented by counts.
            """
            # Validate input length
            if length < 0:
                return 0
            # Base case: There's 1 way to arrange 0 items (the empty sequence)/
            if length == 0:
                # Check if counts are also empty or all zero for consistency
                return 1 if not counts or all(c == 0 for c in counts.values()) else 0

            # Calculate numerator (length!)
            # Ensure length is within the bounds of our precomputed factorials.
            if length >= len(fact):
                #This indicates an unexpected length value, possibly a logic error elsewhere.
                return 0

            numerator = fact[length]

            # Calculate denominator (product of factorials of counts for each digit)
            denominator = 1
            actual_sum_counts = 0   # Keep track of the sum of counts for validation
            for digit_count in counts.values():
                # Validate individual counts
                if digit_count < 0:
                    return 0    # Cannot have negative counts
                # Ensure count is within precomputed factorial bounds
                if digit_count >= len(fact):
                    return 0

                current_fact = fact[digit_count]
                # Denominator should not be zero if counts are non-negative.
                # fact[0] is 1. If current_fact is 0, something is wrong.
                if current_fact == 0 and digit_count > 0:
                    return 0    # Error state

                denominator *= current_fact
                actual_sum_counts += digit_count

            # Validate consistency: The sum of digit counts must be equal to the specified length.
            if actual_sum_counts != length:
                # If mismatch, the input `counts` and `length` are inconsistent
                return 0

            # Final check to prevent division by zero, although denominator should be positive.
            if denominator == 0:
                return 0

            # Perform integer division to get the number of permutations.
            # Numerator should always be non-negative (factorial of non-negative length).
            if numerator < 0:
                return 0
            return numerator // denominator

        # --- Main Logic ---
        # Use a set to store the unique multisets of digits encountered
        # for k-divisible palindromes. Represent each multiset as a
        # frozenset of (digit, count) pairs for hashability.
        found_digit_multisets = set()

        # Determine the range for iterating thriugh the first half 'h' of the palindrome.
        # The length of 'h' determines the structure.
        if n == 1:
            half_len = 1
            start_half = 1 # Palindromes are single sigits 1-9
        else:
            # half_len is ceil(n/2)
            half_len = (n + 1) // 2
            # The first half 'h' must be at least half_len digits long
            # and cannot start with 0 (since the palindrome cannot start with 0).
            start_half = 10 ** (half_len - 1)

        # The end of the range is exclusive: 10**half_len
        end_half = 10**half_len

        # Iterate through all possible first halves 'h'
        for h in range(start_half, end_half):
            h_str = str(h)

            # Construct the second half based on whether n is odd or even.
            if n % 2 == 1:  # Odd length n
                # The middle digit is the last digit of h_str.
                # The second half is the reverse of h_str excluding the last digit.
                if half_len > 0:
                    # Safety check for edge cases like n = 0.
                    second_half = h_str[:-1][::-1]
                else:
                    second_half = ""
            else:  # Even length n
                # The second half is the reverse of the entire first half h_str.
                second_half = h_str[::-1]

            # Combine to form the full palindrome string 'y_str'.
            y_str = h_str + second_half

            # Ensure that the generated palindrome string has the correct length n.
            if len(y_str) != n:
                continue

            # Convert the palindrome string to an integer 'y'.
            y = int(y_str)

            # Check if the palindrome 'y' is divisible by 'k'.
            if y % k == 0:
                # If it is, find the multiset of its digits.
                counts = Counter(y_str)

                # Create a hashable representation of the multiset.
                multiset_representation = frozenset(counts.items())

                # Add this unique multiset representation to our set.
                # If it's already present, the set remains unchanged.
                found_digit_multisets.add(multiset_representation)

        # --- Calculate total good count from the unique multisets ---
        total_good_count = 0

        # Iterate through each unique dgit multiset that corresponds to at least one k-divisible palindrome.
        for multiset_repr in found_digit_multisets:
            # Reconstruct the Counter object for the current multiset.
            counts = Counter(dict(multiset_repr))

            # Calculate the total number of distinct premutations of these digits.
            total_p = count_perms(counts, n)

            # Calculate the number of permutations that start with '0'.
            # These are invalid for n-digit numbers (unless n=1 and the number is 0).
            # Since our palindromes y start with non-zero digits, n must be >= 1.
            # If n=1, the only palindrome starting with 0 is 0 itself, which is handled if needed.
            # But our loop starts from h=1, so y is never 0.
            invalid_p = 0

            # Check if the digit '0' is present in the multiset
            if counts.get('0', 0) > 0:
                # If '0' exists, calculate permutations starting with '0'.
                # Conceptually, fix '0' at the start and permute the remaining n-1 digits.
                # Create a temporary copy of the counter to modify.
                temp_counts = counts.copy()

                # Decrement the count of '0' as one '0' is used at the start.
                temp_counts['0'] -= 1

                # if the count of '0' becomes zero, remove the '0' key entirely from the temp counter.
                if temp_counts['0'] == 0:
                    del temp_counts['0']

                # Calculate permutations for thr remaining (n - 1) digits using the modified counts.
                # The length for this sub-permutation is (n - 1).
                invalid_p = count_perms(temp_counts, n - 1)

            # The number of valid (n-digit, not starting with 0 if n > 1) permutations
            # for the current multiset is total permutations minus invalid ones.
            valid_permutations_count = total_p - invalid_p
            # Add the valid count to the overall total.
            total_good_count += valid_permutations_count

        # Return the total count of good integers.
        return total_good_count
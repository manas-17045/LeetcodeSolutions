# Leetcode 3556: Sum of Largest Prime Substrings
# https://leetcode.com/problems/sum-of-largest-prime-substrings/
# Solved on 30th of May, 2025
import math


class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        """
        Calculates the sum of the largest unique prime numbers found as substrings of the input string `s`.
        It considers all possible substrings, converts them to integers, checks for primality,
        and then sums the top 3 largest unique prime numbers found.

        Args:
            s: A string consisting of digits.

        Returns:
            The sum of the largest unique prime numbers found as substrings.
            If fewer than 3 unique primes are found, it sums all of them.
            If no prime substrings are found, it returns 0.
        """
        # memo_is_prime stores results of primality tests to avoid redundant computations.
        # It is defined inside sumOfLargestPrimes, so it's fresh for each cell to the method,
        # which is good practice if the Solution object is reused for multiple independent problems.
        memo_is_prime = {}

        def isPrimeLocal(numVal: int) -> bool:
            # Check if result is already memoized
            if numVal in memo_is_prime:
                return memo_is_prime[numVal]

            # Basic primality conditions
            if numVal <= 1:     # Numbers less than or equal to 1 are not prime
                result = False
            elif numVal == 2:   # 2 is the ony even prime number
                result = True
            elif numVal % 2 == 0:   # All other even numbers are not prime
                result = False
            else:
                # Test divisibility by odd numbers up to sqrt(numVal)
                isP = True
                # Calculate the integer part of the square root as the limit for trial division
                limit = int(math.sqrt(numVal))
                for i in range(3, limit + 1, 2):    # Iterate over odd numbers from 3 up to the limit
                    if numVal % i == 0:
                        isP = False     # Found a divisor, so not prime
                        break
                result = isP

            # Store the result in memo before returning
            memo_is_prime[numVal] = result
            return result

        sLen = len(s)
        uniquePrimes = set()    # Use a set to store unique prime numbers found

        # Generate all substrings
        for i in range(sLen): # Start index of substring
            for j in range(i, sLen):    # End index of substring
                substring = s[i:j + 1]  # Extract substring s[i...j]

                # Convert substring to an integer. Python's int() handles leading zeros correctly.
                num = int(substring)

                # Check if the number id prime and add to the set if it is
                if isPrimeLocal(num):
                    uniquePrimes.add(num)

        # If no primes were found, return 0 as per the problem statement
        if not uniquePrimes:
            return 0

        # Convert the set of unique primes to a list and sort it in descending order to easily access the largest
        # primes.
        sortedPrimes = sorted(list(uniquePrimes), reverse=True)

        # Determine how many of the largest primes to sum.
        # This will be the top 3, or fewer if less than 3 unique primes were found.
        numToSum = min(3, len(sortedPrimes))

        # Sum the required number of largest primes using list slicing
        return sum(sortedPrimes[:numToSum])
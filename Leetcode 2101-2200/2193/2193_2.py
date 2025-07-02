# Leetcode 2193: Minimum Number of Moves to Make Palindrome
# https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/
# Solved on 2nd of July, 2025
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        """
        Calculates the minimum number of moves required to make a given string a palindrome.

        A move consists of swapping two adjacent characters.
        The string is guaranteed to be a permutation of a palindrome.

        The algorithm uses a two-pointer approach (l and r) starting from the ends of the string.
        It tries to match arr[l] with arr[r].

        If arr[l] and arr[r] already match, both pointers move inward.
        If they don't match, it searches for a character arr[k] from the right side (k > l)
        that matches arr[l].
        - If no such character is found (k == l), it means arr[l] is the unique middle character
          (for odd length palindromes) and it's moved one step towards the center.
        - If a match arr[k] is found, arr[k] is moved to the position of arr[r] by
          repeatedly swapping it with its right neighbor.
        """
        # Work on a list, so we can swap in-place
        arr = list(s)
        n = len(arr)
        l, r = 0, (n - 1)
        moves = 0

        while l < r:
            # If the two ends already match, move inward
            if arr[l] == arr[r]:
                l += 1
                r -= 1
                continue

            # Try to find a matching partner for arr[l] from the right side
            k = r
            while k > l and arr[k] != arr[l]:
                k -= 1

            if k == l:
                # No match found: aee[l] must be unique middle char.
                # Swap it one step toward center and count 1 move.
                arr[l], arr[l + 1] = arr[l + 1], arr[l]
                moves += 1
            else:
                # Bring arr[k] to arr[r] by swapping it rightwards one step at a time
                for i in range(k, r):
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    moves += 1
                # Now, that arr[r] matches arr[l], move both pointers
                l += 1
                r -= 1

        return moves
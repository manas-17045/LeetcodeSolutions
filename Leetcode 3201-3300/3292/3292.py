# Leetcode 3292: Minimum Number of Valid Strings to Form Target II
# https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/
# Solved on 22nd of November, 2025
class Solution:
    def minValidStrings(self, words: list[str], target: str) -> int:
        """
        Calculates the minimum number of valid strings from `words` needed to form the `target` string.
        Uses a greedy approach with rolling hashes to efficiently find valid prefixes.
        :param words: A list of strings that can be used to form the target.
        :param target: The target string to be formed.
        :return: The minimum number of strings required, or -1 if it's impossible.
        """
        # Use a large Mersenne prime for the rolling hash modulus to prevent collisions
        MOD = 2 ** 61 - 1
        # Use a random base to protect against specific anti-hash test cases
        BASE = 31337

        # A set to store tuples of (length, hash) for all valid prefixes from words
        valid_prefixes = set()
        # Track the maximum length of any word to optimize binary search upper bound
        max_word_len = 0

        # Precompute hashes for all prefixes of all words
        for w in words:
            current_hash = 0
            length = 0
            max_word_len = max(max_word_len, len(w))
            for char in w:
                # Rolling hash update: hash = (hash * base + char_code) % mod
                current_hash = (current_hash * BASE + ord(char)) % MOD
                length += 1
                valid_prefixes.add((length, current_hash))

        n = len(target)
        # Precompute powers of BASE to enable O(1) substring hash calculation
        pow_base = [1] * (n + 1)
        for i in range(1, n + 1):
            pow_base[i] = (pow_base[i - 1] * BASE) % MOD

        # Precompute prefix hashes for the target string
        target_hash = [0] * (n + 1)
        for i in range(n):
            target_hash[i + 1] = (target_hash[i] * BASE + ord(target[i])) % MOD

        # Helper function to get hash of target[i:j] in O(1)
        def get_hash(i, j):
            # Formula: (H[j] - H[i] * BASE^(j-i)) % MOD
            return (target_hash[j] - target_hash[i] * pow_base[j - i]) % MOD

        # Variables for the Greedy (Jump Game) approach
        jumps = 0  # Number of strings used
        cur_end = 0  # The end index of the current concatenated string range
        farthest = 0  # The farthest index we can reach using the next string

        # Iterate through the target to find the minimum segments
        for i in range(n):
            # If we can't even reach the current index i, it's impossible to form target
            if i > farthest:
                return -1

            # Only compute the longest match if we are within the reachable range
            # Binary search for the longest valid prefix match starting at target[i]
            low, high = 1, min(n - i, max_word_len)
            best_len = 0

            while low <= high:
                mid = (low + high) // 2
                # Check if the substring target[i:i+mid] exists in our valid prefixes
                if (mid, get_hash(i, i + mid)) in valid_prefixes:
                    best_len = mid
                    low = mid + 1
                else:
                    high = mid - 1

            # Update the farthest point we can reach from current position i
            farthest = max(farthest, i + best_len)

            # If we have reached the end of the current jump range
            if i == cur_end:
                # If we haven't moved forward at all, we are stuck
                if i == farthest:
                    return -1
                # Take a jump (use another string)
                jumps += 1
                cur_end = farthest
                # Optimization: If we already cover the whole target, break early
                if cur_end >= n:
                    return jumps

        # Final check to ensure we covered the entire string
        return jumps if cur_end >= n else -1
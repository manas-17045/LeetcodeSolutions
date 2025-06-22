# Leetcode 2138: Divide a String Into Groups of Size k
# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/
# Solved on 22nd of June, 2025
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        """
        Divides a string `s` into chunks of size `k`. If the last chunk is
        shorter than `k`, it is padded with the `fill` character.

        Args:
            s (str): The input string.
            k (int): The desired chunk size.
            fill (str): The character used for padding.
        Returns:
            list[str]: A list of strings, where each string is a chunk of size `k`.
        """
        res = []
        n = len(s)
        # Process each block of size k
        for i in range(0, n, k):
            chunk = s[i:(i + k)]
            # If chunk is shorter than k, pad on the right with fill
            if len(chunk) < k:
                chunk += fill * (k - len(chunk))
            res.append(chunk)
        return res
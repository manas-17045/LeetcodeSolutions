# Solved on 29th of May, 2025

class Solution:
    def maximumStrongPairXor(self, nums: list[int]) -> int:
        """
        Given a 0-indexed integer array nums, return the maximum XOR of any
        strong pair (x, y) where x and y are elements from the array, and
        |x - y| <= min(x, y).

        A pair (x, y) is called a strong pair if |x - y| <= min(x, y).

        The solution uses a sliding window approach with a Trie to efficiently
        find the maximum XOR value for each element within its valid range.
        The numbers are sorted first to facilitate the sliding window.
        """
        nums.sort()
        n = len(nums)
        if n < 2:
            return 0

        # Determine bit-width from the largest number
        B = nums[-1].bit_length()

        # Trie implemented with parallel arrays for child 0, child 1, and subtree counts
        child0, child1, cnt = [], [], []
        def new_node():
            child0.append(-1)
            child1.append(-1)
            cnt.append(0)
            return len(cnt) -1

        root = new_node()

        def insert(x: int) -> None:
            node = root
            cnt[root] += 1
            for k in range(B - 1, -1, -1):
                bit = (x >> k) & 1
                if bit == 0:
                    if child0[node] == -1:
                        child0[node] = new_node()
                    node = child0[node]
                else:
                    if child1[node] == -1:
                        child1[node] = new_node()
                    node = child1[node]
                cnt[node] += 1

        def delete(x: int) -> None:
            node = root
            cnt[root] -= 1
            for k in range(B - 1, -1, -1):
                bit = (x >> k) & 1
                node = child1[node] if bit else child0[node]
                cnt[node] -= 1

        def maxXorWith(x: int) -> int:
            node = root
            # If trie empty, xor is 0
            if cnt[node] == 0:
                return 0
            res = 0
            for k in range(B - 1, -1, -1):
                bit = (x >> k) & 1
                # Prefer to go opposite bit if available
                if bit == 0:
                    nxt = child1[node]
                    if nxt != -1 and cnt[nxt] > 0:
                        res |= (1 << k)
                        node = nxt
                    else:
                        node = child0[node]
                else:
                    nxt = child0[node]
                    if nxt != -1 and cnt[nxt] > 0:
                        res |= (1 << k)
                        node = nxt
                    else:
                        node = child1[node]
            return res

        ans = 0
        r = 0
        # Slide l from 0 to (n - 1), expand r to include all nums[r] <= 2 * nums[l]
        for l in range(n):
            while r < n and nums[r] <= 2 * nums[l]:
                insert(nums[r])
                r += 1
            # Query best XOR partner for nums[l]
            ans = max(ans, maxXorWith(nums[l]))
            # Remove nums[l] before moving l forward
            delete(nums[l])

        return ans
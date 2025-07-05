# Leetcode 2122: Recover the Original Array
# https://leetcode.com/problems/recover-the-original-array/
# Solved on 5th of July, 2025
from collections import Counter


class Solution:
    def recoverArray(self, nums: list[int]) -> list[int]:
        """
        Recovers the original array `orig` from a given array `nums`,
        where `nums` is formed by taking each element `x` from `orig`,
        and adding `x - k` and `x + k` to `nums` for some positive integer `k`.

        The problem states that `nums` contains `2 * n` elements, where `n` is
        the length of the original array.

        Args:
            nums: A list of integers representing the shuffled and transformed array.

        Returns:
            A list of integers representing the recovered original array.
        """
        nums.sort()
        n2 = len(nums)
        n = n2 // 2
        cnt0 = Counter(nums)

        # Try pairing nums[0] with each nums[j] to get a candidate k.
        for j in range(1, n2):
            diff = nums[j] - nums[0]
            # k must be positive and diff must be even (since diff = 2*k)
            if diff > 0 and diff % 2 == 0:
                k = diff // 2
                cnt = cnt0.copy()
                orig = []
                valid = True

                # Process in increasing order
                for x in nums:
                    if cnt[x] == 0:
                        continue
                    # We need a matching higher value (x + 2*k).
                    y = x + 2*k
                    if cnt[y] <= 0:
                        valid = False
                        break
                    # Take one from x and one from y, and record the elephant (x + k)
                    cnt[x] -= 1
                    cnt[y] -= 1
                    orig.append(x + k)

                if valid and len(orig) == n:
                    return orig

        # By problem guarantee, there is always at least one solution.
        return []
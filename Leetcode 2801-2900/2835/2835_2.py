# Leetcode 2835: Minimum Operations to Form Subsequence With Target Sum
# https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/
# Solved on 18th of June, 2025

class Solution:
    def minOperations(self, nums: list[int], target: int) -> int:
        """
        Calculates the minimum number of operations to make the sum of elements in nums equal to target.

        An operation consists of taking an element x from nums and replacing it with two elements x/2.
        This is only possible if x is even.

        Args:
            nums: A list of integers, where each element is a power of 2.
            target: The target sum.

        Returns:
            The minimum number of operations required.
            Returns -1 if it's impossible to reach the target sum.
        """
        # Count how many of each 2^b we have
        # We size our count array to cover all bits in nums and target
        maxb = max(max(nums).bit_length(), target.bit_length())
        cnt = [0] * (maxb + 1)
        total = 0
        for x in nums:
            b = x.bit_length() - 1
            cnt[b] += 1
            total += x

        # If total sum is less than target, impossible
        if total < target:
            return -1

        ops = 0
        # Process from LSB to MSB
        for i in range(maxb + 1):
            # If target requires a 2^i bit
            if (target >> i) & 1:
                # If we have one, use it
                if cnt[i] > 0:
                    cnt[i] -= 1
                else:
                    # Otherwise, find the nearest larger bit to break down
                    j = i + 1
                    while j <= maxb and cnt[j] == 0:
                        j += 1
                    # No larger bit to break => impossible
                    if j > maxb:
                        return -1
                    # Break one 2^j down step-by-step to 2^i.
                    while j > i:
                        cnt[j] -= 1
                        cnt[j - 1] += 2
                        ops += 1
                        j -= 1
                    # Use one of the newly created 2^i.
                    cnt[i] -= 1

            # Merge any leftovers at this bit into the next bit.
            if i + 1 <= maxb:
                cnt[i + 1] += cnt[i] // 2

        return ops
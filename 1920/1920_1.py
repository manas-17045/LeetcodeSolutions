# Leetcode 1920: Build Array from Permutation
# https://leetcode.com/problems/build-array-from-permutation/

class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        """
        Reconstruct an array such that result[i] = nums[nums[i]]. The input array is
        encoded and decoded internally to achieve the result without requiring extra
        space for another array. This method mutates the input array `nums` directly.

        The function uses two passes:
        1. Encoding Pass: Each element is encoded with its original value and the
           mapped value in a single integer.
        2. Decoding Pass: The encoded values are decoded back to just the mapped
           values.

        :param nums: List of integers where the target indices and their respective
            mapped values will be derived.
        :type nums: list[int]
        :return: List of integers, where each element is the result of
            `nums[nums[i]]` computation as per the problem's requirements.
        :rtype: list[int]
        """
        n = len(nums)

        # Encoding Pass: Store original and final value
        # nums[i] becomes original_nums[i] + n * original_nums[original_nums[i]]
        for i in range(n):
            # Get original value from target index nums[i]
            # Need to use nums[nums[i] % n] % n because nums[nums[i]] might already be > n
            target_val_orig = nums[nums[i] % n] % n     # This tricky - let's re-verify standard method.

            # Standard method confirmed:
            # Encode target value (a = nums[nums[i]] % n) into nums[i]
            # Note: nums[nums[i]] % n works because even if nums[nums[i]] is encoded,
            # its original value is nums[nums[i]] % n.
            a = nums[nums[i] % n] % n   # Correctly finds original value at target index
            nums[i] += n * a    # Add n * target_value to original value

        # Decoding Pass: Extract the target value
        for i in range(n):
            nums[i] //= n   # Divide by n to get the stored target value

        return nums
# Leetcode 1432: Max Difference You Can Get From Changing an Integer
# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/
# Solved on 15th of June, 2025

class Solution:
    def maxDiff(self, num: int) -> int:
        s = list(str(num))
        """
        Given an integer num, you will apply the following rules to get two integers a and b.
        For integer a, you choose the first digit that is not 9 in the number "num",
        and replace all occurrence of this digit in the number "num" with the digit 9.
        For integer b, if the first digit of num is not 1, you choose the first digit of num
        and replace all occurrence of this digit in the number in num with the digit 1.
        Otherwise, you choose the first digit of num which is not 0 or 1, and replace all
        occurrence of this digit in the number in num with the digit 0.
        Return the difference between the maximum and minimum values you can get.
        """

        # Build the maximum value a by turning the first non-'9' into '9'
        a = s[:]
        for i, ch in enumerate(a):
            if ch != '9':
                old = ch
                for j in range(len(a)):
                    if a[j] == old:
                        a[j] = '9'
                break

        # Build the minimum value b by turning the first non-'1' or '0' into '0'
        b = s[:]
        if b[0] != '1':
            old = b[0]
            for j in range(len(b)):
                if b[j] == old:
                    b[j] = '1'
        else:
            for i in range(1, len(b)):
                if b[i] not in ['0', '1']:
                    old = b[i]
                    for j in range(len(b)):
                        if b[j] == old:
                            b[j] = '0'
                    break

        return int(''.join(a)) - int(''.join(b))
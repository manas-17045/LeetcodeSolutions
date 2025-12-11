# Leetcode 2117: Abbreviating the Product of a Range
# https://leetcode.com/problems/abbreviating-the-product-of-a-range/
# Solved on 11th of December, 2025
class Solution:
    def abbreviationProduct(self, left: int, right: int) -> str:
        """
        Calculates the abbreviated product of a range of numbers [left, right].

        Args:
            left (int): The starting number of the range.
            right (int): The ending number of the range.
        Returns:
            str: The abbreviated product in the format "prefix...suffix(eN)" or "product(eN)".
        """
        count2 = 0
        count5 = 0
        suffix = 1
        prefix = 1.0
        curr = 1
        checkLimit = True
        limit = 100000000000000

        for x in range(left, right + 1):
            prefix *= x
            if prefix >= 1e100:
                prefix *= 1e-100

            temp = x
            zeros2 = (temp & -temp).bit_length() - 1
            count2 += zeros2
            temp >>= zeros2

            while temp % 5 == 0:
                temp //= 5
                count5 += 1

            suffix = (suffix * temp) % 100000

            if checkLimit:
                curr *= x
                while curr % 10 == 0:
                    curr //= 10
                if curr >= limit:
                    checkLimit = False

        totalZeros = min(count2, count5)

        if checkLimit:
            strCurr = str(curr)
            if len(strCurr) <= 10:
                return f"{strCurr}e{totalZeros}"

        while prefix >= 100000:
            prefix /= 10
        while prefix < 10000:
            prefix *= 10

        finalPrefix = int(prefix)

        rem2 = count2 - totalZeros
        rem5 = count5 - totalZeros
        finalSuffix = (suffix * pow(2, rem2, 100000) * pow(5, rem5, 100000)) % 100000

        return f"{finalPrefix}...{str(finalSuffix).zfill(5)}e{totalZeros}"
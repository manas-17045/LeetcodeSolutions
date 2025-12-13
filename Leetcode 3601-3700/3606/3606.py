# Leetcode 3606: Coupon Code Validator
# https://leetcode.com/problems/coupon-code-validator/
# Solved on 13th of December, 2025
import re


class Solution:
    def validateCoupons(self, code: list[str], businessLine: list[str], isActive: list[bool]) -> list[str]:
        """
        Validates a list of coupon codes based on several criteria:
        1. The coupon must be active.
        2. The business line must be one of the predefined valid business lines.
        3. The coupon code must not be empty.
        4. The coupon code must match a specific regex pattern:
           - Starts with 1 to 10 uppercase letters.
           - Followed by 1 to 10 digits.
           - Ends with 1 to 10 uppercase letters.
        The valid coupons are then sorted first by their business line (according to a predefined order) and then alphabetically by the coupon code.

        Args:
            code (list[str]): A list of coupon codes.
            businessLine (list[str]): A list of business lines corresponding to each coupon code.
            isActive (list[bool]): A list of booleans indicating whether each coupon is active.

        Returns:
            list[str]: A sorted list of valid coupon codes.
        """
        validCoupons = []

        validBusinessLines = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        regexPattern = re.compile(r'^[A-Z]{1,10}\d{1,10}[A-Z]{1,10}$')

        n = len(code)

        for i in range(n):
            currentCode = code[i]
            currentBusiness = businessLine[i]
            currentActive = isActive[i]

            if not currentActive:
                continue

            if currentBusiness not in validBusinessLines:
                continue

            if not currentCode:
                continue

            if not regexPattern.match(currentCode):
                continue

            validCoupons.append((currentCode, currentBusiness))

        validCoupons.sort(key=lambda x: (validBusinessLines[x[1]], x[0]))

        result = [coupon[0] for coupon in validCoupons]

        return result
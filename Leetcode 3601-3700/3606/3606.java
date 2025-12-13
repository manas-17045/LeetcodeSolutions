// Leetcode 3606: Coupon Code Validator
// https://leetcode.com/problems/coupon-code-validator/
// Solved on 13th of December, 2025
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    /**
     * Validates a list of coupon codes based on various criteria and returns a sorted list of valid codes.
     * @param code An array of coupon codes.
     * @param businessLine An array indicating the business line for each coupon code.
     * @param isActive An array indicating whether each coupon code is active.
     * @return A list of valid and sorted coupon codes.
     */
    public List<Sting> validateCoupons(String code, String[] businessLine, boolean[] isActive) {
        int n = code.length;
        Map<String, Integer> priorityMap = new HashMap<>();
        priorityMap.put("electronics", 1);
        priorityMap.put("grocery", 2);
        priorityMap.put("pharmacy", 3);
        priorityMap.put("restaurant", 4);

        List<Integer> validIndices = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            if (!isActive[i]) {
                continue;
            }

            String currentBusiness = businessLine[i];
            if (!priorityMap.containsKey(currentBusiness)) {
                continue;
            }

            String currentCode = code[i];
            if (currentCode == null || currentCode.isEmpty()) {
                continue;
            }

            boolean isValidCode = true;
            for (char c : currentCode.toCharArray()) {
                if (!Character.isLetterOrDigit(c) && c != '_') {
                    isValidCode = false;
                    break;
                }
            }

            if (isValidCode) {
                validIndices.add(i);
            }
        }

        Collections.sort(validIndices, (a, b) -> {
            int priorityA = priorityMap.get(businessLine[a]);
            int priorityB = priorityMap.get(businessLine[b]);

            if (priorityA != priorityB) {
                return Integer.compare(priorityA, priorityB);
            } else {
                return code[a].compareTo(code[b]);
            }
        });

        List<String> result = new ArrayList<>();
        for (int index : validIndices) {
            result.add(code[index]);
        }

        return result;
    }
}
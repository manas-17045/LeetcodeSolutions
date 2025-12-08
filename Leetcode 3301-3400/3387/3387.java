// Leetcode 3387: Maximize Amount After Two Days of Conversions
// https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/
// Solved on 8th of December, 2025
import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Queue;

class Solution {
    /**
     * Maximizes the amount of initial currency after two days of conversions.
     *
     * @param initialCurrency The starting currency.
     * @param pairs1 A list of currency pairs for day 1 conversions.
     * @param rates1 An array of conversion rates for day 1.
     * @param pairs2 A list of currency pairs for day 2 conversions.
     * @param rates2 An array of conversion rates for day 2.
     * @return The maximum amount achievable after two days.
     */
    public double maxAmount(String initialCurrency, List<List<String>> pairs1, double[] rates1, List<List<String>> pairs2, double[] rates2) {
        Map<String, Double> day1Rates = getRates(initialCurrency, pairs1, rates1);
        Map<String, Double> day2Rates = getRates(initialCurrency, pairs2, rates2);

        double maxVal = 1.0;

        for (String currency : day1Rates.keySet()) {
            if (day2Rates.containsKey(currency)) {
                double rate1 = day1Rates.get(currency);
                double rate2 = day2Rates.get(currency);
                maxVal = Math.max(maxVal, rate1 / rate2);
            }
        }

        return maxVal;
    }

    private Map<String, Double> getRates(String start, List<List<String>> pairs, double[] rates) {
        Map<String, Map<String, Double>> graph = new HashMap<>();
        for (int i = 0; i < pairs.size(); i++) {
            String u = pairs.get(i).get(0);
            String v = pairs.get(i).get(1);
            double rate = rates[i];

            graph.putIfAbsent(u, new HashMap<>());
            graph.putIfAbsent(v, new HashMap<>());

            graph.get(u).put(v, rate);
            graph.get(v).put(u, 1.0 / rate);
        }

        Map<String, Double> visited = new HashMap<>();
        visited.put(start, 1.0);
        Queue<String> queue = new ArrayDeque<>();
        queue.add(start);

        while (!queue.isEmpty()) {
            String curr = queue.poll();
            double currRate = visited.get(curr);

            if (graph.containsKey(curr)) {
                for (Map.Entry<String, Double> entry : graph.get(curr).entrySet()) {
                    String next = entry.getKey();
                    double weight = entry.getValue();

                    if (!visited.containsKey(next)) {
                        visited.put(next, currRate * weight);
                        queue.add(next);
                    }
                }
            }
        }

        return visited;
    }
}
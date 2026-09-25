// Leetcode 1096: Brace Expansion II
// https://leetcode.com/problems/brace-expansion-ii/ 
// Solved on 23rd of September, 2026
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    /**
     * Parses the given brace expansion expression and evaluates the set of words
     * it represents under the grammar rules, returning them in lexicographical order.
     *
     * @param expression the brace expansion expression to evaluate
     * @return the sorted list of distinct words represented by the expression
     */
    public List<String> braceExpansionII(String expression) {
        int[] index = new int[1];
        Set<String> wordSet = parseExpression(expression, index);
        List<String> sortedWords = new ArrayList<>(wordSet);
        Collections.sort(sortedWords);
        return sortedWords;
    }

    private Set<String> parseExpression(String expression, int[] index) {
        Set<String> expressionSet = new HashSet<>();
        while (true) {
            expressionSet.addAll(parseTerm(expression, index));
            if (index[0] < expression.length() && expression.charAt(index[0]) == ',') {
                index[0]++;
            } else {
                break;
            }
        }
        return expressionSet;
    }

    private Set<String> parseTerm(String expression, int[] index) {
        Set<String> termSet = new HashSet<>();
        termSet.add("");
        while (index[0] < expression.length()) {
            char currentChar = expression.charAt(index[0]);
            if (currentChar >= 'a' && currentChar <= 'z') {
                StringBuilder wordBuilder = new StringBuilder();
                while (index[0] < expression.length() && expression.charAt(index[0]) >= 'a' && expression.charAt(index[0]) <= 'z') {
                    wordBuilder.append(expression.charAt(index[0]));
                    index[0]++;
                }
                termSet = multiply(termSet, Collections.singleton(wordBuilder.toString()));
            } else if (currentChar == '{') {
                index[0]++;
                Set<String> subExpressionSet = parseExpression(expression, index);
                index[0]++;
                termSet = multiply(termSet, subExpressionSet);
            } else {
                break;
            }
        }
        return termSet;
    }

    private Set<String> multiply(Set<String> firstSet, Set<String> secondSet) {
        Set<String> productSet = new HashSet<>();
        for (String firstWord : firstSet) {
            for (String secondWord : secondSet) {
                productSet.add(firstWord + secondWord);
            }
        }
        return productSet;
    }
}
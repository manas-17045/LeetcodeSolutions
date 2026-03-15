// Leetcode 1622: Fancy Sequence
// https://leetcode.com/problems/fancy-sequence/
// Solved on 15th of March, 2026
class Fancy {
    
    long[] values;
    int length;
    long multiplier;
    long addition;
    long modValue;

    public Fancy() {
        values = new long[100005];
        length = 0;
        multiplier = 1;
        addition = 0;
        modValue = 1000000007;
    }

    public void append(int val) {
        long current = val;
        current = (current - addition % modValue + modValue) % modValue;
        current = (current * getInverse(multiplier)) % modValue;
        values[length] = current;
        length++;
    }

    public void addAll(int inc) {
        addition = (addition + inc) % modValue;
    }

    public void multAll(int m) {
        multiplier = (multiplier * m) % modValue;
        addition = (addition * m) % modValue;
    }

    public int getIndex(int idx) {
        if (idx >= length) {
            return -1;
        }
        long result = (values[idx] * multiplier) % modValue;
        result = (result + addition) % modValue;
        return (int) result;
    }

    private long getInverse(long num) {
        return getPower(num, modValue - 2);
    }

    private long getPower(long base, long exponent) {
        long answer = 1;
        base = base % modValue;
        while (exponent > 0) {
            if (exponent % 2 == 1) {
                answer = (answer * base) % modValue;
            }
            exponent = exponent / 2;
            base = (base * base) % modValue;
        }
        return answer;
    }
}
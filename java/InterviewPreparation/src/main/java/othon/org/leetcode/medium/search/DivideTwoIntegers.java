package othon.org.leetcode.medium.search;

import lombok.extern.slf4j.Slf4j;
import lombok.var;

/**
 * Link:https://leetcode.com/problems/divide-two-integers/
 * <p>
 * TODO:
 */

@Slf4j
public class DivideTwoIntegers {
    public static void main(String[] args) {
        Solution s = new Solution();
        log.info("{}", s.divide(93706, 157));
        log.info("{}", s.divide2(93706, 157));
    }

    static class Solution {
        // exponential search
        public int divide(int dividend, int divisor) {
            // handle negatives
            int negatives = 2;
            if (dividend<0) {
                negatives -= 1;
                dividend = -dividend;
            }
            if (divisor<0) {
                negatives -= 1;
                divisor = -divisor;
            }
            // now all numbers are positive
            // solve it by doing an exponential search
            // The exponent is how many times we can double up the divisor without passing the dividen
            int quotient = 0;
            while (divisor <= dividend) {
                int value = divisor;
                int powersOfTwo =  1;
                // double up the value
                while ( value + value < dividend) {
                    value += value;
                    powersOfTwo += powersOfTwo;
                }
                // once they don 't fit anymore we substract it
                quotient += powersOfTwo;
                dividend -= value;
            }
            return negatives ==1? -quotient: quotient;
        }

        // exponential search
        public int divide2(int dividend, int divisor) {
            // handle negatives
            int negatives = 2;
            if (dividend<0) {
                negatives -= 1;
                dividend = -dividend;
            }
            if (divisor<0) {
                negatives -= 1;
                divisor = -divisor;
            }

            int highestDouble = divisor; // increment the maximum value
            int powersOfTwo = 1;
            while (highestDouble+highestDouble<=dividend) {
                highestDouble += highestDouble;
                powersOfTwo += powersOfTwo;
            }

            int quotient = 0;
            while (divisor <= dividend) {
                if (dividend>=highestDouble) { // dividing
                    quotient += powersOfTwo; // add the reuslt of the division
                    dividend -= highestDouble;
                }
                // divided the numbers
                highestDouble >>= 1;
                powersOfTwo >>= 1;
            }
            return negatives ==1? -quotient: quotient;
        }
    }
}

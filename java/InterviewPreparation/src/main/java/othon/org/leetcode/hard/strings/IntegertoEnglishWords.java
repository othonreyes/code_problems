package othon.org.leetcode.hard.strings;

import lombok.extern.slf4j.Slf4j;
import lombok.var;

import java.util.HashMap;
import java.util.Map;

/**
 * Link:
 * <p>
 * TODO: https://leetcode.com/problems/integer-to-english-words/
 *
 * Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
 *
 *
 * Input: 123
 * Output: "One Hundred Twenty Three"
 */

@Slf4j
public class IntegertoEnglishWords {
    public static void main(String[] args) {
        Solution s = new Solution();
        var input = 123;
        log.info("{}", s.numberToWords(input));
    }

    static class Solution {

        Map<Integer, String> units = new HashMap<>();
        Map<Integer, String> decs = new HashMap<>();
        Map<Integer, String> teens = new HashMap<>();

        public Solution() {
            units.put(1, "One");
            units.put(2, "Two");
            units.put(3, "Three");
            units.put(4, "Four");
            units.put(5, "Five");
            units.put(6, "Six");
            units.put(7, "Seven");
            units.put(8, "Eight");
            units.put(9, "Nine");

            decs.put(2, "Twenty");
            decs.put(3, "Thirty");
            decs.put(4, "Fourty");
            decs.put(5, "Fifty");
            decs.put(6, "Sixty");
            decs.put(7, "Seventy");
            decs.put(8, "Eighty");
            decs.put(9, "Ninety");

            teens.put(10, "Ten");
            teens.put(11, "Eleven");
            teens.put(12, "Twelve");
            teens.put(13, "Thirteen");
            teens.put(14, "Fourteen");
            teens.put(15, "Fifteen");
            teens.put(16, "Sixteen");
            teens.put(17, "Seventeen");
            teens.put(18, "Eightteen");
            teens.put(19, "Nineteen");
        }


        public String numberToWords(int num) {
            if (num == 0) {
                return "Zero";
            }
            int billion  = 10 * 9;
            int million  = 10 * 6;
            int thousand  = 10 * 3;
            StringBuffer sb = new StringBuffer();

            int billionNum = num / billion;
            num = num % billion;
            int millionNum = num / million;
            num = num % million;
            int thousandNum = num / thousand;
            num = num % thousand;
            if (billionNum > 0) {
                sb.append(converNum(billionNum));
                sb.append(" Billion");
            }
            if (millionNum > 0) {
                if (billionNum > 0) {
                    sb.append(" ");
                }
                sb.append(converNum(millionNum));
                sb.append(" Million");
            }
            if (thousandNum > 0) {
                if (millionNum > 0 || billionNum > 0) {
                    sb.append(" ");
                }
                sb.append(converNum(thousandNum));
                sb.append(" Thousand");
            }
            if (num > 0) {
                if (billionNum > 0 || millionNum > 0 || thousandNum > 0) {
                    sb.append(" ");
                }
                sb.append(converNum(num));
            }
            return sb.toString();
        }

        String converNum(int num) {
            StringBuffer sb = new StringBuffer();
            if (num>99) {
                sb.append(units.get(num/100));
                sb.append(" Hundred");
                num = num % 100;

            }
            if (num > 0) {
                sb.append(" ");
            }
            if (num > 19) {
                sb.append(decs.get(num/10));
            } else if (num > 9) {
                sb.append(teens.get(num));
                return sb.toString();
            }
            if (num > 9) {
                sb.append(" ");
            }
            num = num % 10;
            sb.append(units.get(num));
            return sb.toString();
        }
    }
}

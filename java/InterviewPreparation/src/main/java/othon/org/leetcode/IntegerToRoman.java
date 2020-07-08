package othon.org.leetcode;

import lombok.extern.slf4j.Slf4j;
import sun.awt.Symbol;

import java.util.HashMap;
import java.util.Map;

/**
 * https://leetcode.com/problems/integer-to-roman/solution/
 * 12. Integer to Roman
 */
@Slf4j
public class IntegerToRoman {

    public static void main(String[] args) {
        Solution s = new Solution();
        log.info("{}", s.intToRoman(54) );
        log.info("{}", s.intToRoman(58) );
    }

    static class Solution {
        static Map<Integer, String> symbols = new HashMap<>();
        static {
            symbols.put(1, "I");
            symbols.put(4, "IV");
            symbols.put(5, "V");
            symbols.put(9, "IX");
            symbols.put(10, "X");
            symbols.put(40, "XL");
            symbols.put(50, "L");
            symbols.put(90, "XC");
            symbols.put(100, "C");
            symbols.put(400, "CD");
            symbols.put(500,"D");
            symbols.put(900,"CM");
            symbols.put(1000, "M");
        }
        public String intToRoman(int num) {
            int pow = num>=1000?3:num>=100?2:num>=10?1:0;
            StringBuilder result = new StringBuilder();
            // Accurate but way too complex.
            while (num>0) {
                int exp = (int) Math.pow(10, pow);
                int temp = num / exp;
                temp = temp * exp;
                num -= temp;
                String symbol = symbols.get(exp);
                String acc = "";
                while (temp>0) {
                    if (symbols.containsKey(temp)) {
                        exp = temp;
                        symbol = symbols.get(temp);
                    }
                    temp -= exp;
                    acc = symbol + acc;
                }
                result.append(acc);
                pow -= 1;
            }
            return result.toString();
        }
    }
}

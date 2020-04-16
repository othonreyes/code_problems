package othon.org.leetcode;

import java.util.HashMap;
import java.util.Map;

public class number_to_english {

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.numberToWords(123));
        System.out.println(s.numberToWords(12345));
        System.out.println(s.numberToWords(1234567));
        System.out.println(s.numberToWords(101));
        System.out.println(s.numberToWords(1000000));
    }

    static class Solution {
        Map<Integer, String> numberName;
        Map<Integer, String> sufix;
        Solution() {
            numberName = new HashMap<>();
            numberName.put(0, "Zero");
            numberName.put(1, "One");
            numberName.put(2, "Two");
            numberName.put(3, "Three");
            numberName.put(4, "Four");
            numberName.put(5, "Five");
            numberName.put(6, "Six");
            numberName.put(7, "Seven");
            numberName.put(8, "Eight");
            numberName.put(9, "Nine");
            numberName.put(10, "Ten");
            numberName.put(11, "Eleven");
            numberName.put(12, "Twelve");
            numberName.put(13, "Thirteen");
            numberName.put(14, "Fourteen");
            numberName.put(15, "Fifteen");
            numberName.put(16, "Sixteen");
            numberName.put(17, "Seventeen");
            numberName.put(18, "Eighteen");
            numberName.put(19, "Nineteen");
            numberName.put(20, "Twenty");
            numberName.put(30, "Thirty");
            numberName.put(40, "Forty");
            numberName.put(50, "Fifty");
            numberName.put(60, "Sixty");
            numberName.put(70, "Seventy");
            numberName.put(80, "Eighty");
            numberName.put(90, "Ninety");

            sufix = new HashMap<>();
            sufix.put(100, "Hundred");
            sufix.put(1000, "Thousand");
            sufix.put(1_000_000, "Million");
            sufix.put(1_000_000_000, "Billion");
        }


        public String numberToWords(int num) {
            if (num == 0) {
                return numberName.get(0);
            }
            // first we need to know the size of the number
            int size = String.valueOf(num).length();
            int exp = exponent(size);

            StringBuilder sb = new StringBuilder();
            while (exp >= 0) {
                int d = num / (int)Math.pow(10, exp);
                num = num - d * (int)Math.pow(10, exp);

                generateNumber(d, sb);
                if ( exp > 0) {
                    sb.append(" ");
                    sb.append(sufix.getOrDefault((int)Math.pow(10, exp), ""));
                    if (num > 0) {
                        sb.append(" ");
                    } else {
                        break;
                    }
                }
                exp -= 3;
            }
            return sb.toString();
        }

        int exponent(int size) {
            if (10 <= size && size <= 12) {
                return 9;
            } else if (7 <= size && size <= 9) {
                return 6;
            } else if (4 <= size && size <= 6) {
                return 3;
            } else if (1 <= size && size <= 3) {
                return 0;
            }
            return -1;
        }

        void generateNumber(int d, StringBuilder sb) {
            int h = d / (int)Math.pow(10, 2);
            boolean hundredsAdded = false;
            if ( h > 0) {
                sb.append(numberName.get(h));
                sb.append(" ");
                sb.append(sufix.get(100));
                d = d - h * 100;
                hundredsAdded = true;
            }
            int rest = d / 1;
            if (rest>=10 && rest <=19) {
                if (hundredsAdded) {
                    sb.append(" ");
                }
                sb.append(numberName.get(rest));
                return;
            }
            boolean decAdded = false;
            int dec = rest / 10;
            if (dec > 0) {
                if (hundredsAdded) {
                    sb.append(" ");
                }
                sb.append(numberName.get(dec * 10));
                decAdded = true;
                rest = rest - dec * 10;
            }
            rest = rest / 1;
            if (rest > 0) {
                if (decAdded || hundredsAdded) {
                    sb.append(" ");
                }
                sb.append(numberName.get(rest));
            }

        }
    }
}

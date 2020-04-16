package othon.org.leetcode;

import java.util.HashMap;
import java.util.Map;

public class LongestPalindrome {

    public static void main(String[] args) {
        Solution s = new Solution();
        long n = System.nanoTime();
        String palindrome = s.longestPalindrome("babad");
        System.out.println((System.nanoTime() - n)/1000000);
        System.out.println(palindrome);
        n = System.nanoTime();
        palindrome = s.longestPalindrome("babaddtattarrattatddetartrateedredividerb");
        System.out.println((System.nanoTime() - n)/1000000);

        n = System.nanoTime();
        palindrome = s.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth");
        System.out.println((System.nanoTime() - n)/1000000);

    }

    static class Solution {
        public String longestPalindrome(String s) {
            if (s.length() == 1) {
                return s;
            }

            int e = s.length() - 1;
            int st = 0;
            Map<String, String> m = new HashMap<>();
            return largestPalindrome(s,st, e, m);
        }

        String largestPalindrome(String s, int st, int e, Map<String, String> m) {
            if (st == s.length() || e < 0) {
                return "";
            }
            String sub = s.substring(st, e + 1);
            if (st == e) {
                return sub;
            }
            if (m.get(sub) != null) {
                return m.get(sub);
            }
            if (isPalindrome(sub)) {
                m.put(sub, sub);
                return sub;
            } else {
                m.put(sub, "");
            }
            String left = largestPalindrome(s, st, e - 1, m);
            String right = largestPalindrome(s, st + 1, e, m);
            boolean lb = left.length() > 0;
            boolean rb = right.length() > 0;
            if (left.length() > right.length() && lb) {
                return left;
            } else if (left.length() <= right.length() && (rb || lb)) {
                return rb ? right : (lb? left: "");
            }
            return "";
        }

        boolean isPalindrome(String s) {
            return isPalindrome(s, 0, s.length() - 1);
        }

        boolean isPalindrome(String s, int st, int e) {
            if (e < st || s.length() == 0 || e >= s.length() || st < 0 ) {
                return false;
            }

            while (st<=e) {
                if (s.charAt(st) != s.charAt(e)) {
                    return false;
                }
                st++;
                e--;
            }
            return true;
        }


        // public String longestPalindrome(String s) {
        //     int ix = 0;
        //     int st = 0;
        //     String largest = "";
        //     while (ix < s.length()) {
        //         ix += 1;
        //         String possible = s.substring(st, ix);
        //         if (isPalindrome(possible)) {
        //             if (possible.length() > largest.length()) {
        //                 largest = possible;
        //             }
        //         } else {
        //             possible = s.substring(st + 1, ix);
        //             if (isPalindrome(possible)) {
        //                 if (possible.length() > largest.length()) {
        //                     largest = possible;
        //                     st += 1;
        //                 }
        //             }
        //         }
        //     }
        //     return largest;
        // }

        // this doesn't check palindromes but permutations of palindromes
        // public boolean isPalindrome(String s) {
        //     Map<Character, Integer> map = new HashMap<>();
        //     for(int i= 0; i< s.length(); i ++) {
        //         Integer count = map.get(s.charAt(i));
        //         if (count == null) {
        //             map.put(s.charAt(i), 1);
        //         } else {
        //             count -= 1;
        //             if (count == 0) {
        //                 map.remove(s.charAt(i));
        //             }
        //         }
        //     }
        //     return map.size() <=1;
        // }

        // public boolean isPalindrome(String s) {
        //     Map<Character, Integer> map = new HashMap<>();
        //     for(int i= 0; i< s.length(); i ++) {
        //         Integer count = map.getOrDefault(s.charAt(i), 0) + 1;
        //         map.put(s.charAt(i), count);
        //     }
        //     int oddCount = 0;
        //     for(int i= 0; i< s.length(); i ++) {
        //         if (map.get(s.charAt(i)) % 2 !=0) {
        //             oddCount += 1;
        //         }
        //     }
        //     return oddCount <=1;
        // }

    }
}

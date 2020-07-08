package othon.org.gfg.divideandconquer;

import lombok.extern.slf4j.Slf4j;

// https://www.geeksforgeeks.org/longest-common-prefix-using-divide-and-conquer-algorithm/

/**
 *
 * Given a set of strings, find the longest common prefix.
 *
 * Input  : {“geeksforgeeks”, “geeks”, “geek”, “geezer”}
 * Output : "gee"
 */
@Slf4j
public class LongestCommonPrefix {
    public static void main(String[] args) {
        String[] input = new String[] {"geeksforgeeks", "geeks", "geek", "geezer"};
        log.info("Prefix {} ", commonPrefix(input));
    }

    private static String commonPrefix(String[] input) {
        int left = 0;
        int right = input.length - 1;
        return commonPrefix(input, left, right);
    }

    private static String commonPrefix(String[] input, int left, int right) {
        if (left == right)
            return input[left];
        int mid = (left + right) / 2;
        String leftPrefix = commonPrefix(input, left, mid);
        String rightPrefix = commonPrefix(input, mid + 1, right);
        return prefix(leftPrefix, rightPrefix);
    }

    private static String prefix(String leftPrefix, String rightPrefix) {
        int i = 0;
        int j = 0;
        while (i<leftPrefix.length() && j <rightPrefix.length()) {
            if (leftPrefix.charAt(i) != rightPrefix.charAt(j)) {
                break;
            }
            i += 1;
            j += 1;
        }
        return leftPrefix.substring(0, i);
    }
}

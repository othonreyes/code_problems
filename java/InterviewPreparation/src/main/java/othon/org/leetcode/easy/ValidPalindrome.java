package othon.org.leetcode.easy;

import lombok.extern.slf4j.Slf4j;

@Slf4j
public class ValidPalindrome {
    public static void main(String[] args) {
        log.info("{}",isPalindrome("race a car"));
    }

    public static boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        while (left<right) {
            char cLeft = s.charAt(left);
            if (!Character.isLetterOrDigit(cLeft)) {
                left += 1;
                continue;
            }
            char cRight = s.charAt(right);
            if (!Character.isLetterOrDigit(cRight)) {
                right -= 1;
                continue;
            }
            cLeft = Character.isLetter(cLeft) && Character.isUpperCase(cLeft)? Character.toLowerCase(cLeft):cLeft;
            cRight = Character.isLetter(cRight) && Character.isUpperCase(cRight)? Character.toLowerCase(cRight):cRight;
            if (cLeft!=cRight) {
                return false;
            }
            left += 1;
            right -= 1;
        }
        return true;
    }
}

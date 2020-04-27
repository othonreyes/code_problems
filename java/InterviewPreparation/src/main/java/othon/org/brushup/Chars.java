package othon.org.brushup;

import lombok.extern.slf4j.Slf4j;

@Slf4j
public class Chars {
    public static void main(String[] args) {
//        String s = "A very intersting String with 1234 @!@#$";
////        for (int i = 0; i < s.length(); i++) {
////            Character c = s.charAt(i);
////            c.eq
////            log.info("{} - {}", c, Character.isDigit(c), Character.isLetter(c), Character.isWhitespace(c), Character.isUpperCase(), Character.isAlphabetic(), Character.)
////        }

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

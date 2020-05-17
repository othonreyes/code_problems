package othon.org.brushup;

import lombok.extern.slf4j.Slf4j;

import java.io.CharConversionException;

@Slf4j
public class Chars {
    public static void main(String[] args) {
        String s = "A v 1234 @!@#$";
        log.info("Character | isDigit |  isLetter | isWhitespace| " +
                "isUpperCase |, isAlphabetic | isLetterOrDigit |");
        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            log.info("{} | isDigit {} | isLetter {}| isWhitespace{}| " +
                    "isUpperCase {}|, isAlphabetic {}| isLetterOrDigit {}|",
                    c, Character.isDigit(c), Character.isLetter(c), Character.isWhitespace(c),
                    Character.isUpperCase(c), Character.isAlphabetic(c), Character.isLetterOrDigit(c));
        }

        log.info("Can you coonvert a number to lowercase {}", Character.toLowerCase('1'));

    }
}

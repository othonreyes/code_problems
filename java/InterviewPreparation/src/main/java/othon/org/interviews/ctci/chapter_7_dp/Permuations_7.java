package othon.org.interviews.ctci.chapter_7_dp;

import java.util.ArrayList;
import java.util.List;

public class Permuations_7 {

    public static void main(String[] args) {
        String text = "abc";
        List<String> permutatios = perm(text);
        permutatios.forEach(System.out::println);

        System.out.println();

        List<String> permutations = perm2(text);
        permutations.forEach(System.out::println);
    }

    /**
     * The trick is to remove the character and then send the remaining part.
     * @param text
     * @return
     */
    private static List<String> perm(String text) {
        List<String> results = new ArrayList<>();
        if (text.length() == 1) {
            results.add(text);
            return results;
        }
        for (int i = 0; i < text.length(); i++) {
            char letter = text.charAt(i);
            String left = text.substring(0,i);
            String right = text.substring(i+1);
            List<String> subresults = perm(left + right);
            for (String r : subresults) {
                results.add(letter + r);
            }
        }
        return results;
    }


    private static List<String> perm2(String text) {
        List<String> results = new ArrayList<>();
        perm("", text, results);
        return results;
    }
    /**
     * Using memoization. Sort of
     * @param prefix
     * @param reminder
     * @param results
     */
    private static void perm(String prefix, String reminder, List<String> results) {
        if (reminder.length() == 0) {
            results.add(prefix);
            return;
        }

        for (int i = 0; i < reminder.length(); i++) {
            char letter = reminder.charAt(i);
            String left = reminder.substring(0,i);
            String right = reminder.substring(i+1);
            perm(prefix + letter, left + right, results);
        }
    }
}

package othon.org.brushup;

import java.util.Arrays;

public class Sorting {
    public static void main(String[] args) {
        // Sort an array
        String a = "anagram";
        String b = "nagrama";
        char[] aArray = a.toCharArray();
        char[] bArray = b.toCharArray();
        Arrays.sort(aArray);
        Arrays.sort(bArray);
        System.out.println( Arrays.equals(aArray,bArray));

    }
}

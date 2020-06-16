package othon.org.leetcode.utils;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Deserializer {
    public static int[] toIntArray(String input) {
        if (input == null || input.length()==0 || input.equals("[]")) {
            return new int[0];
        }

        String[] n = input.substring(1, input.length() - 1).split(",");
        int[] numbers = new int[n.length];
        for (int i = 0; i < n.length; i++) {
            numbers[i] = Integer.parseInt(n[i].replace("\"",""));
        }
        return numbers;
    }
    public static int[][] toIntMatrix(String input) {
        //[["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
        if (input.charAt(0) != '[' || input.charAt(input.length()-1) != ']'){
            return null;
        }
        input = input.substring(1, input.length()-1);
        List<int[]> result  = new ArrayList<>();
        int i =0;
        int start = 0;
        while (i<input.length()) {
            start = input.indexOf("[");
            i = input.indexOf("]");

            result.add(toIntArray(input.substring(start,i+1)));
            if (i+2 < input.length())
                input = input.substring(i+2);
            else
                break;
            i = 0;
        }
        return result.toArray(new int[result.size()][]);
    }

    public static List<String> toStringList(String input) {
        if (input == null || input.length()==0 || input.equals("[]")) {
            return Collections.emptyList();
        }
        String[] strings = input.substring(1, input.length() - 1).split(",");
        List<String> result = new ArrayList<>();
        for (String s: strings) {
            result.add(s.replace("\"",""));
        }
        return result;
    }
}

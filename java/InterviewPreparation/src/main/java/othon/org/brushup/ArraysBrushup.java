package othon.org.brushup;

import java.util.Arrays;
import java.util.stream.Collectors;

public class ArraysBrushup {
    public static void main(String[] args) {
        int[] alp = new int[26];
        Arrays.fill(alp, 0);
        //        Arrays.stream(alp).collect(Collectors.toList());
        Arrays.asList(alp);

        int[][] mem = new int[26][20];

        int sum = Arrays.stream(alp).sum();
    }
}

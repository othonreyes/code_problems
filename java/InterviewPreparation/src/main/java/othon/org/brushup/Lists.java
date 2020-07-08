package othon.org.brushup;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;

public class Lists {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        // convert list to array
        list.toArray(new int[list.size()][]);


        int[] a = new int[2];
        List<Integer> b = Arrays.stream(a).boxed().collect(Collectors.toList());

        LinkedList<Integer> nodes = new LinkedList<>();
        nodes.addLast(1);
        nodes.removeLast();
    }
}

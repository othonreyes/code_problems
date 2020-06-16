package othon.org.brushup;

import lombok.extern.slf4j.Slf4j;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

@Slf4j
public class Sets {
    public static void main(String[] args) {
        Set<Integer> set = new HashSet<>();

        set.add(1);
        if (set.contains(1)) {
            log.info("Hello world");
        }
//        set.toArray(new int[set.size()]);

        Set<String> treeset = new TreeSet<>();
        treeset.add("bxcvb");
        treeset.add("asdf");
        treeset.add("xcv");
        log.info("{}", treeset);
        treeset.stream().filter(x -> x.startsWith("a")); // returns a stream
        //treeset.stream().

        // Can't do Arrays.asList with in[]
//        Set<List<Integer>> set2 = new HashSet<>();
//        int[] nums = new int [0];
//        List<Integer> asList = Arrays.asList(nums);
//        set2.add(asList);

        Set<int[]> set3 = new HashSet<>();
        int[] nums = {0,0};
        set3.add(nums);
        set3.remove(nums);
        set3.contains(nums);
//        set3.add

        // Set to list
        Set<Integer> sourceSet = new HashSet<>();
        sourceSet.add(5);
        List<Integer> targetList = new ArrayList<>(sourceSet);

        // clone a set
        new HashSet<Integer>(set);
    }
}

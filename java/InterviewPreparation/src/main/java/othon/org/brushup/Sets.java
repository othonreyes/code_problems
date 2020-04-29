package othon.org.brushup;

import lombok.extern.slf4j.Slf4j;

import java.util.HashSet;
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

        Set<String> treeset = new TreeSet<>();
        treeset.add("bxcvb");
        treeset.add("asdf");
        treeset.add("xcv");
        log.info("{}", treeset);
        treeset.stream().filter(x -> x.startsWith("a")); // returns a stream
    }
}

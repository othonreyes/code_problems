package othon.org.brushup;

import lombok.extern.slf4j.Slf4j;

import java.util.HashSet;
import java.util.Set;

@Slf4j
public class Sets {
    public static void main(String[] args) {
        Set<Integer> set = new HashSet<>();

        set.add(1);
        if (set.contains(1)) {
            log.info("Hello world");
        }
    }
}

package othon.org.brushup;

import java.util.HashMap;
import java.util.Map;

public class Maps {

    public static void main(String[] args) {
        Map<String, Integer> map = new HashMap<>();
        int a = map.computeIfAbsent("a", x -> 0) + 1;
        int b = map.putIfAbsent("b", 1 ) + 1;

        map.entrySet();
    }
}

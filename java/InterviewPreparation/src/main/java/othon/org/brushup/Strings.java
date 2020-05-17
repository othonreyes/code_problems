package othon.org.brushup;

import lombok.extern.slf4j.Slf4j;

@Slf4j
public class Strings {
    public static void main(String[] args) {
        String hello = "hello world";
        System.out.println(hello.lastIndexOf('a'));
        hello.toCharArray();

        StringBuffer sb =  new StringBuffer();
        sb.append("hello");

        log.info("{} = ", sb.reverse().toString());
    }
}

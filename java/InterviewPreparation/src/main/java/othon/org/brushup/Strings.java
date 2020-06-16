package othon.org.brushup;

import lombok.extern.slf4j.Slf4j;

@Slf4j
public class Strings {
    public static void main(String[] args) {
        String hello = "hello world";
        log.info("{}", hello.lastIndexOf('a'));
        log.info("{}", hello.indexOf('a'));
        hello.toCharArray();

        /** Copy a string buffer  **/
        StringBuffer sb =  new StringBuffer();
        sb.append("hello");

        log.info("{} = ", sb.reverse().toString());

        // Copy a string buffer
        StringBuffer sb2 = new StringBuffer(sb);

        //split
        String[] a = "2001:0db8:85a3:0:0:8A2E:0370:7334:".split(":");
        a.
    }
}

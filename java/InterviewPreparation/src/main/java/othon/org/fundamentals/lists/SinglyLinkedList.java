package othon.org.fundamentals.lists;

import lombok.val;

public class SinglyLinkedList {
    public static void main(String[] args) {

    }

    class Node {
        int val;
        Node next;

        Node(int v) {
            val = v;
        }
    }

    void addNode(Node head, int v) {
        Node n = head;
        while (n.next != null) {
            n = n.next;
        }
        n.next = new Node(v);
    }

    Node remove(Node head, int ix) {
        if( ix==0) {
            Node n = head.next;
            head.next = null;
            return n;
        }
        Node runner = head;
        Node prev = null;
        int i=0;
        while (i<ix) {
            prev = runner;
            runner = runner.next;
            i ++;
        }
        prev.next = runner.next;
        runner.next = null;
        return prev.next.next;
    }

}

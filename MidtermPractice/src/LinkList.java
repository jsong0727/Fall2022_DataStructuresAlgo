public class LinkList<T> {
    public Node<T> head;
    public Node<T> tail;

    public int length = 0;

    public LinkList() {
        head = null;
        tail = null;
    }

    public void addNodeToHead(T data) {
        Node<T> addNode = new Node<>(data);
        addNode.next = head;
        head = addNode;
        if (head.next == null) {
            tail = head;
        }
        length++;
    }
    

}

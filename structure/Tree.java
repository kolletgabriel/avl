import java.util.ArrayList;


public class Tree {

    private ArrayList<Node> nodes;
    private Node root;


    public Tree(Node root) {

        this.root = root;
        this.nodes = new ArrayList<Node>();
        this.addNode(root);
    }


    public Node getRoot() {

        return this.root;
    }


    public void setRoot(Node root) {

        this.root = root;
    }


    public ArrayList<Node> getNodes() {

        return this.nodes;
    }


    public void addNode(Node node) {

        this.nodes.add(node);
    }


    public int getSize() {

        return this.nodes.size();
    }


    private boolean insert(Node node1, Node node2) {

        if (node1.getValue() != node2.getValue()) {

            if (node2.getValue() > node1.getValue()) {

                if (node1.getRightSon() == null) {
                    node1.setRightSon(node2);
                    node2.setFather(node1);
                    this.addNode(node2);
                }
                else {
                    return insert(node1.getRightSon(), node2);
                }
            }
            else {

                if (node1.getLeftSon() == null) {
                    node1.setLeftSon(node2);
                    node2.setFather(node1);
                    this.addNode(node2);
                }
                else {
                    return insert(node1.getLeftSon(), node2);
                }
            }
        }

        return false;
    }


    public boolean insert(Node node) {

        return this.insert(this.root, node);
    }


    private boolean fetch(Node node, int val) {
        
        if (node != null) {

            if (val == node.getValue()) {
                return true;
            }
            else if (val > node.getValue()) {
                return fetch(node.getRightSon(), val);
            }
            else {
                return fetch(node.getLeftSon(), val);
            }
        }

        return false;
    }


    public boolean fetch(int val) {

        return this.fetch(this.root, val);
    }


    public static void main(String[] args) {

        Node[] nodes = {
            new Node(2),
            new Node(5),
            new Node(6),
            new Node(7),
            new Node(8),
            new Node(15),
            new Node(18),
        };

        Tree tree = new Tree(nodes[3]);

        for (Node node : nodes) {
            tree.insert(node);
        }

        System.out.println(tree.getRoot());

        System.out.println(tree.fetch(5));
    }
}
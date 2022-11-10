public class Node {

    private int value;
    private Node father;
    private Node leftSon;
    private Node rightSon;
    private int balanceFactor;
    private int level;


    public Node(int value, Node father) {

        this.value = value;
        this.father = father;
        this.leftSon = null;
        this.rightSon = null;
        this.balanceFactor = 0;
        this.level = father.getLevel()+1;
    }


    public Node(int value) { //root

        this.value = value;
        this.father = null;
        this.leftSon = null;
        this.rightSon = null;
        this.balanceFactor = 0;
        this.level = 0;
    }


    public int getValue() {

        return this.value;
    }


    public void setValue(int value) {

        this.value = value;
    }


    public Node getFather() {

        return this.father;
    }


    public void setFather(Node father) {

        this.father = father;
    }


    public Node getLeftSon() {

        return this.leftSon;
    }


    public void setLeftSon(Node leftSon) {

        this.leftSon = leftSon;
    }


    public Node getRightSon() {

        return this.rightSon;
    }


    public void setRightSon(Node rightSon) {

        this.rightSon = rightSon;
    }


    public int getBalanceFactor() {

        return this.balanceFactor;
    }


    public void setBalanceFactor(int balanceFactor) {
    
        this.balanceFactor = balanceFactor;
    }


    public int getLevel() {

        return this.level;
    }


    public void setLevel(int level) {

        this.level = level;
    }


    public String toString() {

        return String.format("%d", this.value);
    }
}
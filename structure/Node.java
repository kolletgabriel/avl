package structure;


public class Node {

    private int value;
    private Node father;
    private Node leftSon;
    private Node rightSon;


    public Node(int value) {

        this.value = value;
    }


    public     int getValue()                { return this.value;        }
    public   Node getFather()                { return this.father;       }
    public  Node getLeftSon()                { return this.leftSon;      }
    public Node getRightSon()                { return this.rightSon;     }

    public    void setValue( int value     ) { this.value = value;       }
    public   void setFather( Node father   ) { this.father = father;     }
    public  void setLeftSon( Node leftSon  ) { this.leftSon = leftSon;   }
    public void setRightSon( Node rightSon ) { this.rightSon = rightSon; }


    public boolean isLeaf() {

        if (this.leftSon == null  &&  this.rightSon == null) {
            return true;
        }

        return false;
    }


    public String toString() {

        return String.format("%d", this.value);
    }
}
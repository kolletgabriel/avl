class Node:

    def __init__(self, key: int,
                 parent: 'Node | None' = None,
                 lchild: 'Node | None' = None,
                 rchild: 'Node | None' = None) -> None:
        self.key = key
        self.parent = parent
        self.lchild = lchild
        self.rchild = rchild

    def __str__(self) -> str:
        return f'{self.key}'

    def __repr__(self) -> str:
        return f'Node(key={self.key},\
                parent={self.parent},\
                lchild={self.lchild},rchild={self.rchild})'

    def __eq__(self, other) -> bool:
        if isinstance(other, int):
            return self.key == other
        return self.key == other.key

    def __gt__(self, other) -> bool:
        if isinstance(other, int):
            return self.key > other
        return self.key > other.key

    def __ge__(self, other) -> bool:
        if isinstance(other, int):
            return self.key >= other
        return self.key >= other.key

    def __lt__(self, other) -> bool:
        if isinstance(other, int):
            return self.key < other
        return self.key < other.key

    def __le__(self, other) -> bool:
        if isinstance(other, int):
            return self.key <= other
        return self.key <= other.key


if __name__ == '__main__':
    ...

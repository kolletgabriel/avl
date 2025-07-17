class Node:
    def __init__(self, key: int,
                 parent: 'Node | None' = None,
                 lchild: 'Node | None' = None,
                 rchild: 'Node | None' = None) -> None:
        self.key = key
        self.__parent = parent
        self.__lchild = lchild
        self.__rchild = rchild

    def __str__(self) -> str:
        return f'{self.key}'

    def __repr__(self) -> str:
        return f'Node({self.key},{self.parent},{self.lchild},{self.rchild})'

    @property
    def parent(self) -> 'Node | None':
        return self.__parent

    @parent.setter
    def parent(self, new_parent: 'Node | None') -> None:
        self.__parent = new_parent

    @property
    def lchild(self) -> 'Node | None':
        return self.__lchild

    @lchild.setter
    def lchild(self, new_lchild: 'Node | None') -> None:
        self.__lchild = new_lchild

    @property
    def rchild(self) -> 'Node | None':
        return self.__rchild

    @rchild.setter
    def rchild(self, new_rchild: 'Node | None') -> None:
        self.__rchild = new_rchild

    @property
    def isroot(self) -> bool:
        return self.__parent is None

    @property
    def isleaf(self) -> bool:
        return self.__lchild is None and self.__rchild is None

    @property
    def height(self) -> int:
        h: int = 1
        parent: 'Node | None' = self.parent
        while parent is not None:
            parent = parent.parent
            h += 1
        return h


if __name__ == '__main__':
    ...

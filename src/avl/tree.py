from avl.node import Node


class Tree:
    def __init__(self, root: Node | None = None) -> None:
        self.__root = root

    @property
    def root(self) -> Node | None:
        return self.__root

    def _recursive_find(self, key: int, curr_node: Node) -> bool:
        if key < curr_node.key:
            if curr_node.lchild is None:
                return False
            self._recursive_find(key, curr_node.lchild)
        if key > curr_node.key:
            if curr_node.rchild is None:
                return False
            self._recursive_find(key, curr_node.rchild)
        return True

    def find(self, key: int) -> bool:
        if self.__root is None:
            return False
        return self._recursive_find(key, self.__root)

    def _recursive_insert(self, key: int, curr_node: Node) -> bool:
        if key < curr_node.key:
            if curr_node.lchild is None:
                curr_node.lchild = Node(key)
                return True
            self._recursive_insert(key, curr_node.lchild)
        if key > curr_node.key:
            if curr_node.rchild is None:
                curr_node.rchild = Node(key)
                return True
            self._recursive_insert(key, curr_node.rchild)
        return False

    def insert(self, key: int) -> bool:
        if self.__root is None:
            self.__root = Node(key)
            return True
        return self._recursive_insert(key, self.__root)

    def _recursive_preorder(self, node: Node | None, keys: list[int]) -> None:
        if node is None:
            return None
        keys.append(node.key)
        self._recursive_preorder(node.lchild, keys)
        self._recursive_preorder(node.rchild, keys)

    def _recursive_inorder(self, node: Node | None, keys: list[int]) -> None:
        if node is None:
            return None
        self._recursive_inorder(node.lchild, keys)
        keys.append(node.key)
        self._recursive_inorder(node.rchild, keys)

    def _recursive_postorder(self, node: Node | None, keys: list[int]) -> None:
        if node is None:
            return None
        self._recursive_postorder(node.lchild, keys)
        self._recursive_postorder(node.rchild, keys)
        keys.append(node.key)

    def traverse(self, order:str) -> list[int]:
        result: list[int] = []
        if order == 'preorder':
            self._recursive_preorder(self.__root, result)
        elif order == 'inorder':
            self._recursive_inorder(self.__root, result)
        elif order == 'postorder':
            self._recursive_postorder(self.__root, result)
        else:
            raise ValueError('Order must be: preorder, inorder or postorder.')
        return result


if __name__ == '__main__':
    ...

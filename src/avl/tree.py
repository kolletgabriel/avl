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
            return self._recursive_find(key, curr_node.lchild)
        if key > curr_node.key:
            if curr_node.rchild is None:
                return False
            return self._recursive_find(key, curr_node.rchild)
        return True

    def find(self, key: int) -> bool:
        if self.__root is None:
            return False
        return self._recursive_find(key, self.__root)

    def _recursive_insert(self, key: int, curr_node: Node) -> bool:
        if key < curr_node.key:
            if curr_node.lchild is None:
                curr_node.lchild = Node(key)
                curr_node.lchild.parent = curr_node
                return True
            return self._recursive_insert(key, curr_node.lchild)
        if key > curr_node.key:
            if curr_node.rchild is None:
                curr_node.rchild = Node(key)
                curr_node.rchild.parent = curr_node
                return True
            return self._recursive_insert(key, curr_node.rchild)
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

    def _get_successor(self, node: Node) -> Node | None:
        curr: Node | None = node.rchild
        while curr is not None and curr.lchild is not None:
            curr = curr.lchild
        return curr

    def _recursive_delete(self, key: int, curr_node: Node) -> bool:
        if key < curr_node.key:
            if curr_node.lchild is None:
                return False
            return self._recursive_delete(key, curr_node.lchild)
        if key > curr_node.key:
            if curr_node.rchild is None:
                return False
            return self._recursive_delete(key, curr_node.rchild)
        # When it has both children:
        if curr_node.lchild is not None and curr_node.rchild is not None:
            successor: Node | None = self._get_successor(curr_node)
            if successor is not None:
                curr_node.key = successor.key
                return self._recursive_delete(successor.key, successor)
        # When it has right child only:
        if curr_node.lchild is None and curr_node.rchild is not None:
            curr_node.key = curr_node.rchild.key
            return self._recursive_delete(curr_node.rchild.key, curr_node.rchild)
        # When it has left child only:
        if curr_node.rchild is None and curr_node.lchild is not None:
            curr_node.key = curr_node.lchild.key
            return self._recursive_delete(curr_node.lchild.key, curr_node.lchild)
        # When it's a leaf:
        if curr_node.parent is not None:
            if curr_node.key < curr_node.parent.key:
                curr_node.parent.lchild = None
                curr_node.parent = None
            else:
                curr_node.parent.rchild = None
                curr_node.parent = None
        else:
            self.__root = None
        return True

    def delete(self, key: int) -> bool:
        if self.__root is None:
            return False
        return self._recursive_delete(key, self.__root)

    def _recursive_height(self, node: Node | None) -> int:
        if node is None:
            return 0
        lsubtree_height: int = self._recursive_height(node.lchild)
        rsubtree_height: int = self._recursive_height(node.rchild)
        height: int = max(lsubtree_height, rsubtree_height) + 1
        return height

    @property
    def height(self) -> int:
        return self._recursive_height(self.__root)

    def _recursive_balance_factor(self, node: Node | None) -> int:
        if node is None:
            return 0
        lsubtree_height: int = self._recursive_height(node.lchild)
        rsubtree_height: int = self._recursive_height(node.rchild)
        factor: int = lsubtree_height - rsubtree_height
        return factor

    @property
    def balance_factor(self) -> int:
        return self._recursive_balance_factor(self.__root)

    def _check(self, node: Node) -> Node | None:
        parent: Node | None = node.parent
        while parent is not None:
            parent_factor: int = self._recursive_balance_factor(parent)
            if abs(parent_factor) == 2:
                return parent
            parent = parent.parent
        return None

    def _rotate_left(self, node: Node) -> None:
        if node.parent is None:
            hold: Node = node.rchild
            node.rchild = node.rchild.lchild
            node.parent = hold
            hold.lchild = node
            self.__root = hold
        else:
            hold: Node = node.rchild
            hold2: Node = node.parent
            node.rchild = node.rchild.lchild
            node.parent = hold
            hold.lchild = node
            hold.parent = hold2
            hold2.rchild = hold

    def _rotate_right(self, node: Node) -> None:
        if node.parent is None:
            hold: Node | None = node.lchild
            node.lchild.parent = None
            node.lchild = None
            node.parent = hold
            node.lchild = hold.rchild
            hold.rchild = node
            self.__root = hold
        else:
            hold: Node | None = node.lchild
            hold2: Node = node.parent
            node.lchild.parent = None
            node.lchild = None
            node.parent = hold
            node.lchild = hold.rchild
            hold.rchild = node
            hold.parent = hold2
            hold2.rchild = hold

    def _recursive_rotation(self, node: Node) -> None:
        factor: int = self._recursive_balance_factor(node)
        if factor > 0:
            child_factor: int = self._recursive_balance_factor(node.lchild)
            if child_factor > 0: # LL
                ...
            else: # LR
                ...
        else:
            child_factor: int = self._recursive_balance_factor(node.rchild)
            if child_factor > 0: # RL
                ...
            else: # RR
                ...


if __name__ == '__main__':
    ...

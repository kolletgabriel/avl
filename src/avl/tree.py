from collections.abc import Generator
from avl.node import Node


class Tree:

    def __init__(self, root: Node | None = None) -> None:
        self.root = root


    @staticmethod
    def _recursive_insert(key: int, node: Node) -> bool:
        if key < node:
            if node.lchild is None:
                node.lchild = Node(key)
                node.lchild.parent = node
                return True
            return Tree._recursive_insert(key, node.lchild)
        if key > node:
            if node.rchild is None:
                node.rchild = Node(key)
                node.rchild.parent = node
                return True
            return Tree._recursive_insert(key, node.rchild)
        return False

    @staticmethod
    def _recursive_find(key: int, node: Node) -> Node | None:
        if key < node:
            if node.lchild is None:
                return None
            return Tree._recursive_find(key, node.lchild)
        if key > node:
            if node.rchild is None:
                return None
            return Tree._recursive_find(key, node.rchild)
        return node

    @staticmethod
    def _get_successor(node: Node) -> Node | None:
        curr: Node | None = node.rchild
        while curr is not None and curr.lchild is not None:
            curr = curr.lchild
        return curr

    @staticmethod
    def _recursive_delete(node: Node) -> Node:
        if node.lchild is not None and node.rchild is not None:  # has both
            successor: Node | None = Tree._get_successor(node)
            node.key = successor.key
            return Tree._recursive_delete(successor)
        if node.lchild is not None:  # has left only
            node.key = node.lchild.key
            return Tree._recursive_delete(node.lchild)
        if node.rchild is not None:  # has right only
            node.key = node.rchild.key
            return Tree._recursive_delete(node.rchild)
        return node  # reched leaf

    @staticmethod
    def _recursive_preorder(node: Node | None) -> Generator[int, None, None]:
        if node is None:
            return None
        yield node.key
        yield from Tree._recursive_preorder(node.lchild)
        yield from Tree._recursive_preorder(node.rchild)

    @staticmethod
    def _recursive_inorder(node: Node | None) -> Generator[int, None, None]:
        if node is None:
            return None
        yield from Tree._recursive_inorder(node.lchild)
        yield node.key
        yield from Tree._recursive_inorder(node.rchild)

    @staticmethod
    def _recursive_postorder(node: Node | None) -> Generator[int, None, None]:
        if node is None:
            return None
        yield from Tree._recursive_postorder(node.lchild)
        yield from Tree._recursive_postorder(node.rchild)
        yield node.key

    @staticmethod
    def _recursive_height(node: Node | None) -> int:
        if node is None:
            return 0
        lsubtree_height: int = Tree._recursive_height(node.lchild)
        rsubtree_height: int = Tree._recursive_height(node.rchild)
        height: int = max(lsubtree_height, rsubtree_height) + 1
        return height

    @staticmethod
    def _recursive_balance_factor(node: Node | None) -> int:
        if node is None:
            return 0
        lsubtree_height: int = Tree._recursive_height(node.lchild)
        rsubtree_height: int = Tree._recursive_height(node.rchild)
        factor: int = lsubtree_height - rsubtree_height
        return factor

    @staticmethod
    def _find_1st_unbalanced_parent_from(node: Node) -> Node | None:
        parent: Node | None = node.parent
        while parent is not None:
            parent_factor: int = Tree._recursive_balance_factor(parent)
            if abs(parent_factor) == 2:
                return parent
            parent = parent.parent
        return None


    def insert(self, *keys: int) -> bool:
        if len(keys) == 1:
            if self.root is None:
                self.root = Node(keys[0])
                return True
            return Tree._recursive_insert(keys[0], self.root)
        if self.root is None:
            self.root = Node(keys[0])
            return any([Tree._recursive_insert(k, self.root) for k in keys[1:]])
        return any([Tree._recursive_insert(k, self.root) for k in keys])

    def find(self, key: int) -> Node | None:
        if self.root is None:
            return None
        return Tree._recursive_find(key, self.root)

    def delete(self, key: int) -> bool:
        to_delete: Node | None = self.find(key)
        if to_delete is None:
            return False
        to_delete = Tree._recursive_delete(to_delete)
        if to_delete.parent is None:
            self.root = None
            return True
        if to_delete.parent.lchild == to_delete:
            to_delete.parent.lchild = None
        else:
            to_delete.parent.rchild = None
        to_delete.parent = None
        return True

    def traverse(self, order:str) -> Generator[int, None, None]:
        if order == 'preorder':
            yield from Tree._recursive_preorder(self.root)
        elif order == 'inorder':
            yield from Tree._recursive_inorder(self.root)
        elif order == 'postorder':
            yield from Tree._recursive_postorder(self.root)
        else:
            raise ValueError('Order must be: preorder, inorder or postorder.')


if __name__ == '__main__':
    ...

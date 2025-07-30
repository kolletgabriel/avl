from collections.abc import Generator, Iterator
from avl.node import Node


class Tree:

    def __init__(self, root: Node | None = None) -> None:
        self.root = root

    def __iter__(self) -> Iterator:
        yield from self.traverse('preorder')

    def __len__(self) -> int:
        len: int = 0
        g: Generator = self.traverse('preorder')
        while True:
            try:
                next(g)
                len += 1
            except StopIteration:
                return len
    
    def _recursive_insert(self, key: int, node: Node) -> bool:
        if key < node:
            if node.lchild is None:
                node.lchild = Node(key)
                node.lchild.parent = node
                needs_balancing: Node | None = (
                    self._find_1st_unbalanced_parent_from(node.lchild)
                )
                if needs_balancing is not None:
                    return self._rotate(needs_balancing)
                return True
            return self._recursive_insert(key, node.lchild)
        if key > node:
            if node.rchild is None:
                node.rchild = Node(key)
                node.rchild.parent = node
                needs_balancing: Node | None = (
                    self._find_1st_unbalanced_parent_from(node.rchild)
                )
                if needs_balancing is not None:
                    return self._rotate(needs_balancing)
                return True
            return self._recursive_insert(key, node.rchild)
        return False
    
    def _recursive_find(self, key: int, node: Node) -> Node | None:
        if key < node:
            if node.lchild is None:
                return None
            return self._recursive_find(key, node.lchild)
        if key > node:
            if node.rchild is None:
                return None
            return self._recursive_find(key, node.rchild)
        return node
    
    def _get_successor(self, node: Node) -> Node | None:
        curr: Node | None = node.rchild
        while curr is not None and curr.lchild is not None:
            curr = curr.lchild
        return curr
    
    def _recursive_delete(self, node: Node) -> Node:
        if node.lchild is not None and node.rchild is not None:  # has both
            successor: Node | None = self._get_successor(node)
            node.key = successor.key
            return self._recursive_delete(successor)
        if node.lchild is not None:  # has left only
            node.key = node.lchild.key
            return self._recursive_delete(node.lchild)
        if node.rchild is not None:  # has right only
            node.key = node.rchild.key
            return self._recursive_delete(node.rchild)
        return node  # reched leaf

    def _recursive_preorder(self, node: Node | None) -> Generator[int, None, None]:
        if node is None:
            return None
        yield node.key
        yield from self._recursive_preorder(node.lchild)
        yield from self._recursive_preorder(node.rchild)

    def _recursive_inorder(self, node: Node | None) -> Generator[int, None, None]:
        if node is None:
            return None
        yield from self._recursive_inorder(node.lchild)
        yield node.key
        yield from self._recursive_inorder(node.rchild)

    def _recursive_postorder(self, node: Node | None) -> Generator[int, None, None]:
        if node is None:
            return None
        yield from self._recursive_postorder(node.lchild)
        yield from self._recursive_postorder(node.rchild)
        yield node.key

    def _recursive_height(self, node: Node | None) -> int:
        if node is None:
            return 0
        lsubtree_height: int = self._recursive_height(node.lchild)
        rsubtree_height: int = self._recursive_height(node.rchild)
        height: int = max(lsubtree_height, rsubtree_height) + 1
        return height

    def _recursive_balance_factor(self, node: Node | None) -> int:
        if node is None:
            return 0
        lsubtree_height: int = self._recursive_height(node.lchild)
        rsubtree_height: int = self._recursive_height(node.rchild)
        factor: int = lsubtree_height - rsubtree_height
        return factor

    def _find_1st_unbalanced_parent_from(self, node: Node | None) -> Node | None:
        while node is not None:
            node_factor: int = self._recursive_balance_factor(node)
            if abs(node_factor) == 2:
                return node
            node = node.parent
        return None


    def _rotate_left(self, node: Node) -> bool:
        if node.rchild is None:
            return False
        hold_parent: Node | None = node.parent
        hold_child: Node | None = node.rchild.lchild
        node.parent = node.rchild
        node.parent.lchild = node
        node.parent.parent = hold_parent
        if node.parent.parent is None:
            self.root = node.parent
        elif node.parent.parent < node.parent:
            node.parent.parent.rchild = node.parent
        else:
            node.parent.parent.lchild = node.parent
        node.rchild = hold_child
        if node.rchild is not None:
            node.rchild.parent = node
        return True

    def _rotate_right(self, node: Node) -> bool:
        if node.lchild is None:
            return False
        hold_parent: Node | None = node.parent
        hold_child: Node | None = node.lchild.rchild
        node.parent = node.lchild
        node.parent.rchild = node
        node.parent.parent = hold_parent
        if node.parent.parent is None:
            self.root = node.parent
        elif node.parent.parent > node.parent:
            node.parent.parent.lchild = node.parent
        else:
            node.parent.parent.rchild = node.parent
        node.lchild = hold_child
        if node.lchild is not None:
            node.lchild.parent = node
        return True

    def _rotate(self, node: Node) -> bool:
        if self._recursive_balance_factor(node) < 0:
            if self._recursive_balance_factor(node.rchild) < 0:
                return self._rotate_left(node)
            return all(
                [self._rotate_right(node.rchild), self._rotate_left(node)]
            )
        if self._recursive_balance_factor(node.lchild) >= 0:
            return self._rotate_right(node)
        return all(
            [self._rotate_left(node.lchild), self._rotate_right(node)]
        )

    def insert(self, *keys: int) -> bool:
        if len(keys) == 1:
            if self.root is None:
                self.root = Node(keys[0])
                return True
            return self._recursive_insert(keys[0], self.root)
        if self.root is None:
            self.root = Node(keys[0])
            return any([self._recursive_insert(k, self.root) for k in keys[1:]])
        return any([self._recursive_insert(k, self.root) for k in keys])

    def find(self, key: int) -> Node | None:
        if self.root is None:
            return None
        return self._recursive_find(key, self.root)

    def delete(self, key: int) -> bool:
        to_delete: Node | None = self.find(key)
        if to_delete is None:
            return False
        to_delete = self._recursive_delete(to_delete)
        if to_delete.parent is None:
            self.root = None
            return True
        hold_parent: Node = to_delete.parent
        if to_delete.parent.lchild == to_delete:
            to_delete.parent.lchild = None
        else:
            to_delete.parent.rchild = None
        to_delete.parent = None
        needs_balancing: Node | None = (
            self._find_1st_unbalanced_parent_from(hold_parent)
        )
        if needs_balancing is not None:
            self._rotate(needs_balancing)
        return True

    def traverse(self, order:str) -> Generator[int, None, None]:
        if order == 'preorder':
            yield from self._recursive_preorder(self.root)
        elif order == 'inorder':
            yield from self._recursive_inorder(self.root)
        elif order == 'postorder':
            yield from self._recursive_postorder(self.root)
        else:
            raise ValueError('Order must be: preorder, inorder or postorder.')


if __name__ == '__main__':
    ...

import unittest
from avl.tree import Tree


class TestTree(unittest.TestCase):
    def setUp(self) -> None:
        self.t = Tree()

    def tearDown(self) -> None:
        del self.t

    def test_insert(self) -> None:
        self.assertIsNone(self.t.root)
        self.t.insert(8)
        self.assertIsNotNone(self.t.root)
        self.t.insert(6)
        self.assertIsNotNone(self.t.root.lchild)
        self.assertEqual(self.t.root.lchild.key, 6)
        self.t.insert(9)
        self.assertIsNotNone(self.t.root.rchild)
        self.assertEqual(self.t.root.rchild.key, 9)

    def test_find(self) -> None:
        self.t.insert(8)
        self.assertTrue(self.t.find(8))
        self.t.insert(6)
        self.assertTrue(self.t.find(6))
        self.assertFalse(self.t.find(9))
        self.t.insert(9)
        self.assertTrue(self.t.find(9))

    def test_preorder(self) -> None:
        correct_order = [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15]
        t = Tree()
        t.insert(8)
        t.insert(4)
        t.insert(12)
        t.insert(2)
        t.insert(6)
        t.insert(10)
        t.insert(14)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        t.insert(9)
        t.insert(11)
        t.insert(13)
        t.insert(15)
        self.assertEqual(t.traverse('preorder'), correct_order)

    def test_inorder(self) -> None:
        t = Tree()
        t.insert(9)
        t.insert(7)
        t.insert(8)
        t.insert(6)
        t.insert(5)
        t.insert(1)
        t.insert(3)
        t.insert(2)
        t.insert(4)
        t.insert(10)
        t.insert(16)
        t.insert(15)
        t.insert(14)
        t.insert(13)
        t.insert(12)
        t.insert(11)
        self.assertEqual(t.traverse('inorder'), list(range(1,17)))

    def test_postorder(self) -> None:
        correct_order = [1, 3, 2, 5, 7, 6, 4, 9, 11, 10, 13, 15, 14, 12, 8]
        t = Tree()
        t.insert(8)
        t.insert(4)
        t.insert(12)
        t.insert(2)
        t.insert(6)
        t.insert(10)
        t.insert(14)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        t.insert(9)
        t.insert(11)
        t.insert(13)
        t.insert(15)
        self.assertEqual(t.traverse('postorder'), correct_order)


if __name__ == '__main__':
    unittest.main()

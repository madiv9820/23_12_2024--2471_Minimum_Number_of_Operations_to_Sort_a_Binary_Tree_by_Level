from Solution import Solution
import unittest
from timeout_decorator import timeout

class TreeNode:
    def __init__(self, val = 0, left = None, right = 0):
        self.val = val
        self.left = left
        self.right = right

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = {1: (["1","4","3","7","6","8","5","null","null","null","null","9","null","10"], 3), 
                            2: (["1","3","2","7","6","5","4"], 3), 
                            3: (["1","2","3","4","5","6"], 0)}
        self.__sol = Solution()
        return super().setUp()
    
    def __createBinaryTree(self, array):
        root = None
        if array[0] != 'null': root = TreeNode(int(array[0]))
        
        queue, index, n = [root], 0, len(array)
        while index < n:
            node = queue[0]; queue.pop()
            if array[index] != 'null':
                node.left = TreeNode(int(array[index]))
                queue.append(node.left)
                index += 1
            if index < n and array[index] != 'null':
                node.right = TreeNode(int(array[index]))
                queue.append(node.right)
                index += 1
    
    @timeout(0.5)
    def test_case_1(self):
        input, output = self.__testcases[1]
        root = self.__createBinaryTree(input)
        result = self.__sol.minimumOperations(root = root)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_2(self):
        input, output = self.__testcases[2]
        root = self.__createBinaryTree(input)
        result = self.__sol.minimumOperations(root = root)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_3(self):
        input, output = self.__testcases[3]
        root = self.__createBinaryTree(input)
        result = self.__sol.minimumOperations(root = root)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()
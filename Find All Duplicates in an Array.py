import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        inputList = []
        self.assertEqual(Solution().findDuplicates(inputList),[])

class Solution(object):
    def findDuplicates(self, nums):
        if nums == []:
            return []

if __name__ == '__main__':
    unittest.main()

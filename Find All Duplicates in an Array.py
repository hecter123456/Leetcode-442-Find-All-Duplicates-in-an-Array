import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        inputList = []
        self.assertEqual(Solution().findDuplicates(inputList),[])
    def testDuplicates(self):
        inputList = [4,3,2,7,8,2,3,1]
        ans = [2,3]
        self.assertEqual(Solution().findDuplicates(inputList),ans)
    def testSpecialCase(self):
        inputList = [4,3,2,7,8,2,3,1,2]
        ans = [2,3,2]
        self.assertEqual(Solution().findDuplicates(inputList),ans)
class Solution(object):
    def findDuplicates(self, nums):
        ans = []
        if nums == []:
            return ans
        searchset = set() 
        for node in nums:
            if node in searchset:
                ans.append(node)
            else:
                searchset.add(node)
        return ans

if __name__ == '__main__':
    unittest.main()

class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        return ''.join(word1) == ''.join(word2)


solution = Solution()
print(solution.arrayStringsAreEqual(["ab", "c"],["a", "bc"]))

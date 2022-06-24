class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        return not False in [letter in sentence for letter in letters]


solution = Solution()
print(solution.checkIfPangram('leetcode'))

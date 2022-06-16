class Solution:
    def mostWordsFound(self, sentences):
        return max([len(sentence.split(' ')) for sentence in sentences])


solution = Solution()
print(solution.mostWordsFound(["please wait","continue to fight","continue to win"]))

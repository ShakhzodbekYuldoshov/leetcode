class Solution:
    def truncateSentence(self, s, k):
        return ' '.join(s.split(' ')[:k])


solution = Solution()
print(solution.truncateSentence(s = "Hello how are you Contestant", k = 4))

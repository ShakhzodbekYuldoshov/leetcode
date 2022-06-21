class Solution:
    def sortSentence(self, s):
        return ' '.join([st[:-1] for st in sorted(s.split(' '), key=lambda x:x[-1])])


solution = Solution()
print(solution.sortSentence("is2 sentence4 This1 a3"))

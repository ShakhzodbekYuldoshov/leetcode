class Solution:
    def restoreString(self, s, indices):
        string = ''
        string = ''.join([s[indices.index(idx)] for idx in range(len(indices))])
        return string


solution = Solution()
print(solution.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))

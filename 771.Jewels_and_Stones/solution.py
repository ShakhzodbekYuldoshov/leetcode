class Solution:
    def numJewelsInStones(self, jewels, stones):
        return sum([1 for stone in stones if stone in jewels])

solution = Solution()
print(solution.numJewelsInStones('z', 'ZZ'))

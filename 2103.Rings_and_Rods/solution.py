class Solution:
    def countPoints(self, rings):
        colors = {}
        for chars in zip(rings[::2],rings[1::2]):
            if not colors.get(chars[1]):
                colors[chars[1]] = chars[0].lower()
            else:
                colors[chars[1]] += chars[0].lower()
        
        return sum([1 for k, v in colors.items() if ('b' in v) and ('g' in v) and ('r' in v)])


solution = Solution()
print(solution.countPoints("B0B6G0R6R0R6G9"))

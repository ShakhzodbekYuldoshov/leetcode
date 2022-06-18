class Solution:
    def getConcatenation(self, nums):
        nums.extend(nums)
        return nums


solution = Solution()

print(solution.getConcatenation([1,2,1]))

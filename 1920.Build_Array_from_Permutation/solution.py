class Solution:
    def buildArray(self, nums):
        return [nums[nums[idx]] for idx in range(len(nums))]


solution = Solution()

print(solution.buildArray([0,2,1,5,3,4]))

class Solution:
    def runningSum(self, nums):
        prev = 0
        ret_nums = []
        for num in nums:
            prev += num
            ret_nums.append(prev)
        return ret_nums


solution = Solution()

print(solution.runningSum([1, 2, 3, 4]))

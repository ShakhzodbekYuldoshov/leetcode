from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for i, num in enumerate(nums):
            diff, num = str(target - num), str(num)
            if num in diff_dict.keys():
                return [diff_dict[num], i]
            diff_dict[diff] = i

solution = Solution()
sol = solution.twoSum([2,7,11,15], 9)

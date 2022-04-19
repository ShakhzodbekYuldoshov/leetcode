class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # if number more than 0 convert x to string reverse it and convert to integer
        # if number less than 0 multiply x by -1 convert to string reverse it and convert to integer and multiply by -1 again to make it negative
        ret_x = int(str(x*(-1))[::-1]) *(-1) if x < 0 else int(str(x)[::-1])
        
        # validate returning object
        # if validation is passed then return found image
        # if validation is not passed return 0
        return ret_x if ret_x >= -2**31 and ret_x <= 2**31 else 0
        

solution = Solution()
print(solution.reverse(321))

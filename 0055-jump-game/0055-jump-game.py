class Solution:
    def canJump(self, nums):
        final_position = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= final_position:
                final_position = i

        return final_position == 0
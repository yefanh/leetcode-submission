class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        '''                  j
                             i   j
                       0 1 2 3 4 5
        Input: nums = [5,7,7,8,8,10], target = 8
        Output: [3,4]
        '''
        def findStart(target) -> int: # find the 1st idx >= target
            l, r = -1, len(nums)
            while l + 1 < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m
                else:
                    r = m
            return r

        start = findStart(target)

        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        
        end = findStart(target + 1) - 1 # end idx <= target

        return [start, end]
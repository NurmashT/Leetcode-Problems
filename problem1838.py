class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # sort the input array
        # left and right pointer that start from the same index 0
        # create a loop that itrates over the whole array
        # check if the size of the window is enough for 'k' additions
        # return the max size of the window

        nums.sort()
        l, r = 0, 0
        max_size = 0
        total = 0
        while r < len(nums):
            total += nums[r]
            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
            max_size = max(max_size, r - l + 1)
            r += 1
        
        return max_size

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        #pivot point
        while l <= r:
            mid = (l + r) // 2            
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1
        
        def binary_search(l, r, target):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        answer = binary_search(0, l - 1, target) 
        if answer != -1:
            return answer
        else:
            return binary_search(l, len(nums) - 1, target)

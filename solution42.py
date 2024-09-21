class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        maxR, maxL = height[r], height[l]

        while l < r:
            if maxR < maxL:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
            else:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            
        return res

from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = max(piles)
        if h == len(piles): return max_val

        l, r = 1, max_val
        k = max_val
        while l <= r:
            mid = l + (r - l) // 2
            hours = 0
            for p in piles:
                hours += ceil((p / mid))
            if hours > h:
                l = mid + 1
            elif hours <= h:
                r = mid - 1
                k = min(k, mid)
            
        return k

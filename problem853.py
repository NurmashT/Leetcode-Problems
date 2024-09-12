class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = {}
        length = len(position)
        for i in range(length):
            pair[position[i]] = speed[i]
        position.sort() 
        stack = []

        for i in range(length - 1, -1, -1):
            stack.append((target - position[i]) / pair[position[i]])
            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
        
        return len(stack)

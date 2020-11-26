class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while len(stack) and T[stack[-1]] < T[i]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        
        return result
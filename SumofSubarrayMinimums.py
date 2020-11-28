class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        prev = [-1 for _ in range(len(arr))]
        next_ = [len(arr) for _ in range(len(arr))]
        
        stack = []
        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                index = stack.pop()
                next_[index] = i
            stack += [i]
        
        print(next_)
        
        stack = []
        for i in reversed(range(len(arr))):
            while stack and arr[i] <= arr[stack[-1]]:
                index = stack.pop()
                prev[index] = i
            stack += [i]
            
        print(prev)
        
        m = 10 ** 9 + 7
        sum_ = 0
        for i in range(len(arr)):
            prev_sum = i - prev[i]
            next_sum = next_[i] - i
            count = prev_sum * next_sum
            sum_ += count * arr[i]
        
        return sum_ % m
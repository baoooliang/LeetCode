class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        arr = []
        j = 0
        for i in range(len(pushed)):
            arr.append(pushed[i])
            while arr and j < len(popped) and arr[-1] == popped[j]:
                arr.pop()
                j+=1
        return len(arr) == 0
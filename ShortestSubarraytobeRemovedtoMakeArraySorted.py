class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        i, j = 0, len(arr) - 1
        while j > 0 and arr[j-1] <= arr[j]:
            j-=1
        
        if j == 0:
            return 0
        
        res = j
        while i < j and (i == 0 or arr[i-1] <= arr[i]):
            while j < len(arr) and arr[i] > arr[j]:
                j+=1
            res = min(res, j-i-1)
            i+=1
        return res
        
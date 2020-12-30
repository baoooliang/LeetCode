class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if len(arr) == m: return m
        res, seats = -1, [0] * (len(arr) + 2)
        for i in range(len(arr)):
            a = arr[i]
            left, right = a - 1, a + 1
            if seats[left] == m or seats[right] == m:
                res = i
            seats[a - seats[left]] = seats[a + seats[right]] = seats[left] + seats[right] + 1
        return res
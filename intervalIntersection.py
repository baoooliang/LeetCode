class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        while i < len(firstList) and j < len(secondList):
            if firstList[i][0] <= secondList[j][1] and firstList[i][1] >= secondList[j][0]:
                new_i = max(firstList[i][0], secondList[j][0])
                new_j = min(firstList[i][1], secondList[j][1])
                res.append([new_i, new_j])
            if firstList[i][1] > secondList[j][1]:
                j+=1
            else:
                i+=1
        return res
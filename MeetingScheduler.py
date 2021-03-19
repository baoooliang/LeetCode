class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        i, j = 0, 0
        slots1.sort()
        slots2.sort()
        while i < len(slots1) and j < len(slots2):
            start1, end1 = slots1[i]
            start2, end2 = slots2[j]
            if start1 < end2 and end1 > start2:
                intersect = [max(start1, start2), min(end1, end2)]
                if intersect[1] - intersect[0] >= duration:
                    intersect[1] = intersect[0] + duration
                    return intersect
            
            if end1 > end2:
                j+=1
            else:
                i+=1
        
        return []
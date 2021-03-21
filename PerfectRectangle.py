class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        _set = set()
        area = 0
        for x1,y1,x2,y2 in rectangles:
            tl = (x1,y2)
            tr = (x2,y2)
            bl = (x1,y1)
            br = (x2,y1)
            
            area += (x2-x1) * (y2-y1)
            for point in [tl,tr,bl,br]:
                if point in _set:
                    _set.remove(point)
                else:
                    _set.add(point)
            
        
        if len(_set) != 4:
            return False
        
        sorted_points = sorted(list(_set))
        x1,y1 = sorted_points[0]
        x2,y2 = sorted_points[3]
        area_ref = (y2 - y1) * (x2 - x1)
        
        return area_ref == area
        
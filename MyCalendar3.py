class MyCalendarThree:

    def __init__(self):
        self.list = []

    def book(self, start: int, end: int) -> int:
        self.list.append((start, 1))
        self.list.append((end, -1))
        
        res = float('-inf')
        sum_ = 0
        for time, num in sorted(self.list):
            sum_ += num
            res = max(res, sum_)
        return res
            
class StockSpanner:

    def __init__(self):
        self.stack = []        

    def next(self, price: int) -> int:
        count = 1
        while len(self.stack) and self.stack[-1][0] <= price:
            element = self.stack.pop()
            count += element[1]
        self.stack += [(price, count)]
        
        return count
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.score = 0
        self.foodQueue = collections.deque(food)
        self.coordinate = (0,0)
        self.map = {
            'R': (0, 1),
            'L': (0, -1),
            'U': (-1, 0),
            'D': (1, 0)
        }
        self.body = collections.deque([(0,0)])
        self.body_size = 1
    
    def set_body(self, x, y):
        self.body.append((x,y))
        if len(self.body) > self.body_size:
            self.body.popleft()
        
    def hit_body(self, x, y):
        return (x,y) in list(self.body)[:len(self.body)-1]
    
    def move(self, direction: str) -> int:         
        _x, _y = self.map[direction]
        x, y = self.coordinate
        new_x, new_y = (x + _x, y + _y)
        
        self.set_body(new_x, new_y)
        
        if new_x < 0 or new_x >= self.height or new_y < 0 or new_y >= self.width or self.hit_body(new_x, new_y):
            return -1
        
        if self.foodQueue:
            food_x, food_y = self.foodQueue[0]
            if new_x == food_x and new_y == food_y:
                self.score += 1
                self.foodQueue.popleft()
                self.body_size += 1
        
        self.coordinate = (new_x, new_y)
        
        return self.score
            
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
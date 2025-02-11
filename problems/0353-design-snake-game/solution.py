class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.board = [[""] * width for _ in range(height)]
        self. width = width
        self.height = height
        self.food = deque(food)
        fr, fc = self.food.popleft()
        self.board[fr][fc] = "f"
        
        self.snake = deque()
        self.snake.append([0, 0])
        self.board[0][0] = "s"    
        self.eatenCount = 0    
        

    def move(self, direction: str) -> int:
        # print(self.snake)
        r = self.snake[-1][0]
        c = self.snake[-1][1]

        if direction == "U":
            r -= 1
        if direction == "D":
            r += 1
        if direction == "L":
            c -= 1
        if direction == "R":
            c += 1
        
        isOutOfBounds = r < 0 or r >= self.height or c < 0 or c >= self.width
        if isOutOfBounds:
            return -1
            
        if self.board[r][c] == "f":
            self.eatenCount += 1
            if self.food:
                fr, fc = self.food.popleft()
                self.board[fr][fc] = "f"
        else:
            tr, tc = self.snake.popleft()
            self.board[tr][tc] = ""
        
        if self.board[r][c] == "s":
            return -1
        
        self.board[r][c] = "s"
        self.snake.append([r, c])

        return self.eatenCount



# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

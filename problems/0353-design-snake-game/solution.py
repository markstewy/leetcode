class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.board = [[""] * width for _ in range(height)]
        
        self.food = deque(food)
        foodR = self.food[0][0]
        foodC = self.food[0][1]
        self.board[foodR][foodC] = "food"
        self.food.popleft()

        self.snake = deque()
        self.snake.append([0, 0])
        self.board[0][0] = "snake"

        self.eatenCount = 0


    def move(self, direction: str) -> int:
        headR = self.snake[-1][0]
        headC = self.snake[-1][1]
        tailR = self.snake[0][0]
        tailC = self.snake[0][1]


        if direction == "U":
            headR -= 1
        if direction == "D":
            headR += 1
        if direction == "R":
            headC += 1
        if direction == "L":
            headC -= 1
        
        if headR < 0 or headC < 0 or headR >= self.height or headC >= self.width:
            return -1
        
        isSnake = self.board[headR][headC] == "snake"
        isTail = headR == tailR and headC == tailC
        if isSnake and not isTail:
            return -1

        if self.board[headR][headC] == "food":
            self.eatenCount += 1
            if self.food:
                foodR = self.food[0][0]
                foodC = self.food[0][1]
                self.board[foodR][foodC] = "food"
                self.food.popleft()
        else:
            self.board[tailR][tailC] = ""
            self.snake.popleft()
        
        self.snake.append([headR, headC])
        self.board[headR][headC] = "snake"
        
        return self.eatenCount




        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

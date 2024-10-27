class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.board = [[""] * width for _ in range(height)]
        self.eatenCount = 0
        
        self.food = deque(food)
        foodR = self.food[0][0]
        foodC = self.food[0][1]
        self.board[foodR][foodC] = "food"
        self.food.popleft()

        self.snake = deque()
        self.snake.append([0, 0])
        self.board[0][0] = "snake"


    def move(self, direction: str) -> int:
        # is valid move
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
        
        if headR < 0 or headR >= self.height or headC < 0 or headC >= self.width:
            return -1

        isTailVacancy = headR == tailR and headC == tailC
        isSnakeOccupied = self.board[headR][headC] == "snake" and not isTailVacancy
        
        if isSnakeOccupied:
            return -1
        
        if self.board[headR][headC] == "food":
            # increase score
            self.eatenCount += 1

            # add food
            if self.food:
                foodR = self.food[0][0]
                foodC = self.food[0][1]
                self.board[foodR][foodC] = "food"
                self.food.popleft()

        else:
            # bring up tail
            self.board[tailR][tailC] = ""
            self.snake.popleft()
        
        # add to head
        self.snake.append([headR, headC])
        self.board[headR][headC] = "snake"
        return self.eatenCount

        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

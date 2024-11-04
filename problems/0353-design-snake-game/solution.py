class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height

        self.board = [[""] * self.width for _ in range(self.height)]

        self.food = deque(food)
        if self.food:
            foodR = self.food[0][0]
            foodC = self.food[0][1]
            self.board[foodR][foodC] = "food"
            self.food.popleft()

        self.snake = deque()
        self.snake.append([0,0])
        self.board[0][0] = "snake"

        self.eatCount = 0

    def move(self, direction: str) -> int:
        hr = self.snake[-1][0]
        hc = self.snake[-1][1]
        tr = self.snake[0][0]
        tc = self.snake[0][1]

        if direction == "U":
            hr -= 1
        if direction == "D":
            hr += 1
        if direction == "L":
            hc -= 1
        if direction == "R":
            hc += 1

        # if out of bounds
        if hr < 0 or hc < 0 or hr >= self.height or hc >= self.width:
            return -1
        # if crashes into self
        isSnake = self.board[hr][hc] == "snake"
        isTail = (hr == tr and hc == tc)
        if isSnake and not isTail:
            return -1

        if self.board[hr][hc] == "food":
            self.eatCount += 1
            if self.food:
                foodR = self.food[0][0]
                foodC = self.food[0][1]
                self.board[foodR][foodC] = "food"
                self.food.popleft()
        else:
            self.board[tr][tc] = ""
            self.snake.popleft()
        
        self.snake.append([hr, hc])
        self.board[hr][hc] = "snake"

        return self.eatCount

        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

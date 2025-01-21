class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.board = [[""] * width for _ in range(height)]
        self.width = width
        self.height = height
        self.food = deque(food)
        self.eatenCount = 0

        self.board[0][0] = "s"
        self.snake = deque()
        self.snake.append([0, 0])
        
        foodr = self.food[0][0]
        foodc = self.food[0][1]
        self.board[foodr][foodc] = "f"
        self.food.popleft()


    def move(self, direction: str) -> int:
        currR = self.snake[-1][0]
        currC = self.snake[-1][1]

        if direction == "U":
            currR -= 1
        if direction == "D":
            currR += 1
        if direction == "L":
            currC -= 1
        if direction == "R":
            currC += 1
        
        # if out of bounds
        if currC < 0 or currR < 0 or currC >= self.width or currR >= self.height:
            return -1
        
        # crashes into self
        tailR = self.snake[0][0]
        tailC = self.snake[0][1]
        isTailEnd = currC == tailC and currR == tailR
        if self.board[currR][currC] == "s" and not isTailEnd:
            print(f"{currR} {currC}")
            print(self.snake)
            return -1

        # food
        if self.board[currR][currC] == "f":
            self.eatenCount += 1
            if self.food:
                foodr = self.food[0][0]
                foodc = self.food[0][1]
                self.board[foodr][foodc] = "f"
                self.food.popleft()
        else:
            self.snake.popleft()
            self.board[tailR][tailC] = ""
        
        self.snake.append([currR, currC])
        self.board[currR][currC] = "s"
        
        return self.eatenCount
        


            

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

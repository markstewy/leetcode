class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = deque()
        self.snake.append({"r": 0, "c": 0})

        self.board = [[""] * width for _ in range(height)]
        self.height = height
        self.width = width
        self.food = deque(food)
        self.addNextFood()

    def addNextFood(self):
        if self.food:
            foodRow = self.food[0][0]
            foodCol = self.food[0][1]
            self.board[foodRow][foodCol] = "o"
            self.food.popleft()

    def move(self, direction: str) -> int:
        r = self.snake[-1]["r"]
        c = self.snake[-1]["c"]

        if direction == "U":
            r -= 1
        elif direction == "D":
            r += 1
        elif direction == "L":
            c -= 1
        elif direction == "R":
            c += 1

        # return -1 if wall
        if r < 0 or r > self.height - 1:
            return -1
        if c < 0 or c > self.width - 1:
            return -1

        # if no fodd move up the tail else do nothing
        if self.board[r][c] != "o":
            self.board[self.snake[0]["r"]][self.snake[0]["c"]] = ""
            self.snake.popleft()
        else:
            self.addNextFood()
        
        # check self collision after updating self.snake tail 
        if self.board[r][c] == "x":
            return -1

        # valid move, no food or wall
        self.board[r][c] = "x"
        self.snake.append({"r": r, "c": c})
        return len(self.snake) - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

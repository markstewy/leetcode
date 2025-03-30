class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height

        self.grid = [[""] * self.width for _ in range(self.height)]
        self.snake = deque([[0, 0]])
        self.grid[0][0] = "s"

        self.food = deque(food)
        fr, fc = self.food.popleft()
        self.grid[fr][fc] = "f"


    def move(self, direction: str) -> int:
        directions = {
            "U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1),
        }
        
        nr, nc = directions[direction]
        nr += self.snake[-1][0]
        nc += self.snake[-1][1]
        
        # inbounds
        if not (0 <= nr < self.height and 0 <= nc < self.width):
            return -1
        
        # is snake
        if self.grid[nr][nc] == "s" and [nr, nc] != self.snake[0]:
            return -1

        # add food
        if self.grid[nr][nc] != "f":
            tr, tc = self.snake.popleft()
            self.grid[tr][tc] = ""
        else:
            if self.food:
                fr, fc = self.food.popleft()
                self.grid[fr][fc] = "f"
        
        # update board, and snake
        self.grid[nr][nc] = "s"
        self.snake.append([nr, nc])
        
        return len(self.snake) - 1

        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

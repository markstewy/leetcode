class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.height = height
        self.width = width
        self.food = deque(food)

        self.snake = deque()
        self.snake.append((0, 0))

        self.grid = [[""] * self.width for _ in range(self.height)]
        self.grid[0][0] = "s"

        fr, fc = self.food.popleft()
        self.grid[fr][fc] = "f"

    def move(self, direction: str) -> int:
        print(self.snake)
        dirs = {
            "U": (-1, 0), 
            "D": (1, 0), 
            "L": (0, -1), 
            "R": (0, 1)
            }
        r, c = self.snake[-1]
        nr, nc = dirs[direction]
        nr += r
        nc += c

        if nr < 0 or nc < 0 or nr >= len(self.grid) or nc >= len(self.grid[0]):
            return -1
        
        # "", "f", "s"
        if self.grid[nr][nc] == "f":
            self.snake.append([nr, nc])
            self.grid[nr][nc] = "s"
            if self.food:
                fr, fc = self.food.popleft()
                self.grid[fr][fc] = "f"
        elif self.grid[nr][nc] == "":
            self.snake.append([nr, nc])
            self.grid[nr][nc] = "s"
            tr, tc = self.snake.popleft()
            self.grid[tr][tc] = ""
        elif self.grid[nr][nc] == "s":
            # print(f"{nr} {nc}. {self.snake[0]}")
            if (nr, nc) == tuple(self.snake[0]):
                tail = self.snake.popleft()
                self.snake.append(tail)
            else:
                print("HIT")
                return -1      
        
        return len(self.snake) - 1
        

        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

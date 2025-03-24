class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        
        self.board = [[""] * self.width for _ in range(self.height)]
        
        self.food = deque(food)
        fr, fc = self.food.popleft()
        self.board[fr][fc] = "f"

        self.snake = deque([[0, 0]])
        self.board[0][0] = "s"
        
        self.directions = {
            "U": [-1, 0],
            "D": [1, 0],
            "L": [0, -1],
            "R": [0, 1]
        }

    def isValid(self, r, c):
        if not (0 <= r < self.height and 0 <= c < self.width):
            return False
        
        tr, tc = self.snake[0]
        isTail = r == tr and c == tc
        isSnake = self.board[r][c] == "s" and not isTail

        if isSnake:
            return False

        return True


    def move(self, direction: str) -> int:
        nr, nc = self.directions[direction]
        nr += self.snake[-1][0]
        nc += self.snake[-1][1]

        if not self.isValid(nr, nc):
            return -1
        
        if self.board[nr][nc] != "f":
            tr, tc = self.snake.popleft()
            self.board[tr][tc] = ""
        else:
            if self.food:
                fr, fc = self.food.popleft()
                self.board[fr][fc] = "f"
        
        self.snake.append([nr, nc])
        self.board[nr][nc] = "s"
        return len(self.snake) - 1
        
            
        




        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

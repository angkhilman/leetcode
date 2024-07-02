class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.ans_x = 0
        self.ans_y = 0
        self.direction = 'East'
        self.next_directions = {'East': 'North',
                                'North': 'West',
                                'West': 'South',
                                'South': 'East'}
        self.direction_to_position_diffs = {'East': (1, 0),
                                            'North': (0, 1),
                                            'West': (-1, 0),
                                            'South': (0, -1)}
        

    def step(self, num: int) -> None:
        is_started_from = (self.ans_x == 0 and self.ans_y == 0)
        per = 2 * (self.width + self.height - 2)
        num = num % per
        while num > 0:
            max_step = self.get_max_step()
            move = min(num, max_step)
            self.ans_x += self.direction_to_position_diffs[self.direction][0] * move
            self.ans_y += self.direction_to_position_diffs[self.direction][1] * move
            num -= move
            
            if num > 0:
                self.direction = self.next_directions[self.direction]
        if is_started_from and (self.ans_x == 0 and self.ans_y == 0):
            self.direction = 'South'

    def get_max_step(self):
        max_step = 0
        if self.direction == 'East':
             max_step = self.width - 1 - self.ans_x
        elif self.direction == 'North':
            max_step = self.height - 1 - self.ans_y
        elif self.direction == 'West':
            max_step = self.ans_x
        elif self.direction == 'South':
            max_step = self.ans_y
        return max_step
        

    def getPos(self) -> List[int]:
        return [self.ans_x, self.ans_y]
        

    def getDir(self) -> str:
        return self.direction
        

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()

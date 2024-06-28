from collections import defaultdict
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dd = defaultdict(list)
        for i in obstacles:
            dd[i[0]].append(i[1])
        distance = 0
        ans_x, ans_y = 0, 0
        x, y = 0, 1
        for c in commands:
            if c == -1:
                if x == 0 and y == 1:
                    x, y = 1, 0
                    continue
                if x == 1 and y == 0:
                    x, y = 0, -1
                    continue
                if x == 0 and y == -1:
                    x, y = -1, 0
                    continue
                if x == -1 and y == 0:
                    x, y = 0, 1
                    continue
            elif c == -2:
                if x == 0 and y == 1:
                    x, y = -1, 0
                    continue
                if x == -1 and y == 0:
                    x, y = 0, -1
                    continue
                if x == 0 and y == -1:
                    x, y = 1, 0
                    continue
                if x == 1 and y == 0:
                    x, y = 0, 1
                    continue
                
            else:
                for i in range(c):
                    ans_y += y
                    ans_x += x
                    if ans_x in dd:
                        if ans_y in dd[ans_x]:
                            ans_y -= y
                            ans_x -= x
                            break
                    distance = max(distance, ans_x**2 + ans_y**2)
            
        return distance
        

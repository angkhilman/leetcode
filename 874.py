from collections import defaultdict
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dd = defaultdict(list)
        for i in obstacles:
            dd[i[0]].append(i[1])
        distance = 0
        ans_x, ans_y = 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_drct_ind = 0
        x, y = directions[cur_drct_ind]
        for c in commands:
            if c == -1:
                cur_drct_ind = (cur_drct_ind + 1) % 4
                x, y = directions[cur_drct_ind]
            elif c == -2:
                cur_drct_ind = (cur_drct_ind - 1) % 4
                x, y = directions[cur_drct_ind]
                
            else:
                for i in range(c):
                    if ans_x + x in dd and ans_y + y in dd[ans_x+x]:
                        break
                    ans_y += y
                    ans_x += x
                    distance = max(distance, ans_x**2 + ans_y**2)
            
        return distance
        

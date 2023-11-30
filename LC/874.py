from typing import List
from collections import defaultdict
from bisect import *
class Solution:
    # [-8, -4, -1, 3, 6, 9]
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        current_direction = 0
        horizontal_obstacle_mapping = defaultdict(list) # y -> obstacles in x
        vertical_obstacle_mapping = defaultdict(list) #  x -> obstacles in y
        x = 0
        y = 0
        for obstacle in obstacles:
            insort(horizontal_obstacle_mapping[obstacle[1]],obstacle[0])
            insort(vertical_obstacle_mapping[obstacle[0]],obstacle[1])
        max_distance = 0
        for command in commands:
            max_distance = max(max_distance,x*x+y*y)
            if command == -1:
                current_direction = (current_direction + 1)%4
                continue
            if command == -2:
                current_direction = (current_direction - 1)%4
                continue
            if directions[current_direction][0]==0: # Vertical movement
                if not vertical_obstacle_mapping[x]:
                    y += command*directions[current_direction][1]
                    continue
                if directions[current_direction][1]==-1:
                    obstacle_idx = bisect_left(vertical_obstacle_mapping[x],y) - 1
                    if obstacle_idx == -1:
                        y -= command
                    elif vertical_obstacle_mapping[x][obstacle_idx]>y:
                        y -= command
                    else:
                        distance = y-vertical_obstacle_mapping[x][obstacle_idx]-1
                        y -= min(command,distance)
                else:
                    obstacle_idx = bisect_left(vertical_obstacle_mapping[x],y)
                    if obstacle_idx==len(vertical_obstacle_mapping[x]) or vertical_obstacle_mapping[x][obstacle_idx]<=y:
                        y += command
                    else:
                        distance = vertical_obstacle_mapping[x][obstacle_idx]-y-1
                        y += min(command,distance)
            else: # Horizontal movement
                if not horizontal_obstacle_mapping[y]:
                    x += command*directions[current_direction][0]
                    continue
                if directions[current_direction][0]==-1:
                    obstacle_idx = bisect_left(horizontal_obstacle_mapping[y],x) - 1
                    if obstacle_idx == -1:
                        x -= command
                    elif horizontal_obstacle_mapping[y][obstacle_idx]>x:
                        x -= command
                    else:
                        distance = x-horizontal_obstacle_mapping[y][obstacle_idx]-1
                        x -= min(command,distance)
                else:
                    obstacle_idx = bisect_left(horizontal_obstacle_mapping[y],x)
                    if obstacle_idx==len(horizontal_obstacle_mapping[y]) or horizontal_obstacle_mapping[y][obstacle_idx]<=x:
                        x += command
                    else:
                        distance = horizontal_obstacle_mapping[y][obstacle_idx]-x-1
                        x += min(command,distance)
        return max(max_distance,x*x+y*y)
    
# commands = [4,-1,3]
# obstacles = [[0,0]]
# commands = [-2,8,3,7,-1]
# obstacles = [[-4,-1],[1,-1],[1,4],[5,0],[4,5],[-2,-1],[2,-5],[5,1],[-3,-1],[5,-3]]
commands = [5,4,-1,8,3,4,-1,-1,-2,5,6,-2,6,-1,7,2,8,7,7,9,-1,4,6,9,4,9,3,-2,-2,4,1,2,-1,9,-1,-1,3,-1,6,3,3,1,-1,9,-1,-1,2,8,6,1,9,-2,4,3,9,-2,7,-1,3,9,2,-2,7,3,9,9,9,7,3,2,1,9,-1,8,-1,1,3,2,6,-2,1,3,5,-2,3,6,-1,4,3,6,5,1,2,3,3,5,-1,-1,1,4]
obstacles = [[-14,-73],[78,46],[75,20],[-93,-75],[38,-50],[-52,4],[-87,-14],[52,93],[61,-21],[15,7],[-60,-38],[-93,-38],[-37,-76],[-80,-50],[-85,-74],[46,43],[-19,-74],[33,-2],[32,70],[65,58],[-49,-34],[79,-94],[24,17],[-4,-72],[-40,83],[-1,52],[91,-38],[17,41],[72,-7],[-87,20],[37,84],[-9,-96],[-84,-93],[-96,66],[13,-20],[-84,24],[-51,-13],[6,-62],[-65,-61],[-89,64],[77,0],[-60,2],[-29,-83],[-79,33],[26,83],[-66,-34],[66,53],[2,-39],[72,93],[75,61],[78,-39],[86,40],[-85,62],[-73,-8],[-3,-95],[56,-31],[95,-25],[18,20],[-14,-44],[42,59],[84,-38],[-50,90],[-72,90],[82,-22],[-34,-46],[-35,-12],[-24,-69],[41,93],[37,76],[42,-8],[-91,-37],[38,-74],[98,63],[50,53],[98,94],[-65,9],[66,14],[30,33],[-56,-15],[99,-82],[78,-16],[-98,-45],[55,14],[-89,94],[-22,25],[-65,60],[-76,39],[-10,33],[36,-41],[98,-5],[84,-3],[25,-57],[2,-63],[5,66],[-14,86],[-11,-24],[86,51],[-8,22],[30,-46],[2,-68],[18,47],[15,33],[0,21],[-62,35],[88,-63],[-7,29],[-39,39],[-4,35],[50,85],[61,72],[87,54],[-46,-41],[-56,96],[7,-70],[20,22],[73,54],[-69,-5],[-69,-34],[-19,-31],[-20,-100],[-39,21],[-88,-85],[-100,-41],[-41,70],[23,32],[28,27],[69,60],[-65,-27],[-90,8],[57,76],[-6,-36],[-94,18],[81,-18],[15,-81],[24,-94],[-100,57],[-31,58],[32,-88],[-55,-16],[6,93],[78,72],[-12,96],[3,-38],[33,46],[79,-40],[-96,15],[-5,93],[-70,66],[72,-69],[-72,-6],[-90,16],[-79,-33],[15,-84],[-18,53],[11,82],[67,57],[65,-24],[-17,-100],[81,35],[-47,27],[52,94],[83,-88],[64,57],[2,-26],[15,78],[-95,-81],[45,3],[-73,-71],[73,35],[-53,-1],[-30,41],[93,-62],[86,67],[16,99],[-52,-98],[57,50],[49,-67],[-36,90],[64,-23],[-69,71],[-25,-49],[37,77],[49,99],[-42,-39],[84,-74],[60,-85],[-47,-67],[-14,-40],[91,2],[-18,-33],[-49,-12],[87,73],[-27,99],[-37,-36],[-62,-35],[-37,-61],[70,17],[-29,-8],[-33,-17],[68,-59]]
new_commands = [commands[0]]
for command in commands[1:]:
    if new_commands[-1]<0 or command<0:
        new_commands.append(command)
    else:
        new_commands[-1] += command
sol = Solution()
print(sol.robotSim(new_commands,obstacles))
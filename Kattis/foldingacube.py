from collections import deque
from copy import deepcopy
def hash_state(state):
    return ''.join([str(int(elem)) for elem in sum(state[0],[])+state[1]+state[2]])

def validate_move(state,move_index):
    x = state[2][0] + directions[move_index][0]
    y = state[2][1] + directions[move_index][1]
    return x>=0 and y>=0 and x<6 and y<6

def rotate_cube(state,move_index):
    map,cube,pos = state
    affected_face_indices = rotations[move_index]
    prev_face = cube[affected_face_indices[0]]
    for idx in affected_face_indices[1:]:
        cube[idx],prev_face = prev_face, cube[idx]
    cube[affected_face_indices[0]] = prev_face
    pos[0] += directions[move_index][0]
    pos[1] += directions[move_index][1]
    return (map,cube,pos)

def perform_move(state,move_index):
    state = rotate_cube(state,move_index)
    map,cube,pos = state
    try:
        map[pos[1]][pos[0]],cube[5] = cube[5],map[pos[1]][pos[0]]
    except:
        print('uh oh')
    return (map,cube,pos)

def check_complete(state):
    for face in state[1]:
        if not face:return False
    return True

map = [[False for _ in range(6)] for _ in range(6)]
# T N E S W B
cube = [False for _ in range(6)]
cube[5] = True

pos = [-1,-1]
# R L U D
directions = [[1,0],[-1,0],[0,-1],[0,1]]
rotations = [[0,2,5,4],[0,4,5,2],[0,1,5,3],[0,3,5,1]]
for row in range(6):
    line = input()
    for col in range(6):
        map[row][col] = line[col] == '#'
        if map[row][col]:pos = [row,col]
map[pos[1]][pos[0]] = False
visited_states = set()
state_queue = deque()
state_queue.append((map,cube,pos))
visited_states.add(hash_state(state_queue[0]))

def solve(state_queue):
    while state_queue:
        current_state = state_queue.popleft()
        for move_index in range(4):
            if validate_move(current_state[0],move_index):
                temp_state = deepcopy(current_state)
                temp_state = perform_move(temp_state,move_index)
                if hash_state(temp_state) in visited_states:continue
                if check_complete(temp_state):
                    return True
                state_queue.append(temp_state)
                visited_states.add(hash_state(temp_state))
    return False

print(solve(state_queue))
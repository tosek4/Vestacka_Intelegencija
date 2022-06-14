from searching_framework.utils import Problem
from searching_framework.uninformed_search import *



class Search(Problem):
    def __init__(self, initial,goal=None):
        super().__init__(initial,goal)
        self.goal_size = [6,4]


    def successor(self, state):

        successors = dict()

        pacman_x = state[0]
        pacman_y = state[1]
        obstacle1 = [state[2],state[3],state[4]]
        obstacle2 = [state[5],state[6],state[7]]


                               #Dvizejne na preckite

        if obstacle1[2] == 1:         #desno
            if obstacle1[0] == 6:
                obstacle1[2] = 0
                obstacle1[0] -= 1
            else:
                obstacle1[0] += 1
        else:                         #levo
            if obstacle1[0] == 0:
                obstacle1[2] = 1
                obstacle1[0] += 1
            else:
                obstacle1[0] -= 1

        if obstacle2[2] == 1:        #gore
            if obstacle2[1] == 5:
                obstacle2[2] = 0
                obstacle2[1] -= 1
            else:
                obstacle2[1] += 1
        else:                         #dolu
            if obstacle2[1] == 0:
                obstacle2[2] = 1
                obstacle2[1] += 1
            else:
                obstacle2[1] -= 1

        obstacles = [[obstacle1[0],obstacle1[1]],[obstacle2[0],obstacle2[1]]]

        if 0 <= pacman_x+1 < 7 and [pacman_x + 1, pacman_y] not in obstacles: #move right
            successors['Desno'] = (pacman_x + 1, pacman_y, obstacle1[0], obstacle1[1], obstacle1[2],
                                                      obstacle2[0], obstacle2[1], obstacle2[2])

        if 0 <= pacman_x-1 < 7 and [pacman_x - 1, pacman_y] not in obstacles: #move left
            successors['Levo'] = (pacman_x - 1, pacman_y, obstacle1[0], obstacle1[1], obstacle1[2],
                                                     obstacle2[0], obstacle2[1], obstacle2[2])

        if 0 <= pacman_y + 1 < 7 and [pacman_x , pacman_y + 1] not in obstacles: #move up
            successors['Gore'] = (pacman_x,pacman_y + 1,obstacle1[0],obstacle1[1],obstacle1[2],
                                                     obstacle2[0],obstacle2[1],obstacle2[2])

        if 0 <= pacman_y - 1 < 7 and [pacman_x , pacman_y - 1] not in obstacles: #move down
            successors['Dolu'] = (pacman_x,pacman_y - 1,obstacle1[0],obstacle1[1],obstacle1[2],
                                                     obstacle2[0],obstacle2[1],obstacle2[2])



        return successors

    def actions(self, state):

        return self.successor(state).keys()

    def result(self, state, action):

        return self.successor(state)[action]


    def goal_test(self, state):

        position = (state[0],state[1])

        return  position == self.goal

if __name__ == '__main__':
    goal_state = (6,4)
    initial_state = (0,0)

    obstacle_1 = (2, 2, 0)  # left - Right
    obstacle_2 = (4, 5, 0)  # up - down

    exp = Search((initial_state[0],initial_state[1],
                   obstacle_1[0],obstacle_1[1],obstacle_1[2],
                   obstacle_2[0],obstacle_2[1],obstacle_2[2]),goal_state)

    result = breadth_first_graph_search(exp)
    print(result.solution())
    print(result.solve())
from searching_framework.utils import Problem
from searching_framework.uninformed_search import *
from searching_framework.informed_search import greedy_best_first_graph_search, astar_search, \
    recursive_best_first_search


def ProdolziDesno(x, y, obstacles):
    if 0 <= x + 1 < 5 and [x + 1, y] not in obstacles:
        x += 1
    return x


def ProdolziLevo(x, y, obstacles):
    if 0 <= x - 1 < 5 and [x - 1, y] not in obstacles:
        x -= 1
    return x


def ProdolziGore(x, y, obstacles):
    if 0 <= y + 1 < 5 and [x, y + 1] not in obstacles:
        y += 1
    return y


def ProdolziDolu(x, y, obstacles):
    if 0 <= y - 1 < 5 and [x, y - 1] not in obstacles:
        y -= 1
    return y


class Search(Problem):
    def __init__(self, obstacles, initial, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles

    def successor(self, state):

        successors = dict()

        pacman_x = state[0]
        pacman_y = state[1]

        new_pacman_x = ProdolziDesno(pacman_x, pacman_y, self.obstacles)
        if new_pacman_x != pacman_x:
            successors['Desno'] = (new_pacman_x, pacman_y)

        new_pacman_x = ProdolziLevo(pacman_x, pacman_y, self.obstacles)
        if new_pacman_x != pacman_x:
            successors['Levo'] = (new_pacman_x, pacman_y)

        new_pacman_y = ProdolziGore(pacman_x, pacman_y, self.obstacles)
        if new_pacman_y != pacman_y:
            successors['Gore'] = (pacman_x, new_pacman_y)

        new_pacman_y = ProdolziDolu(pacman_x, pacman_y, self.obstacles)
        if new_pacman_y != pacman_y:
            successors['Dolu'] = (pacman_x, new_pacman_y)

        return successors

    def actions(self, state):

        return self.successor(state).keys()

    def result(self, state, action):

        return self.successor(state)[action]

    def goal_test(self, state):

        posicion = (state[0], state[1])

        return posicion == self.goal

    def h(self, node):
        x_pacman = node.state[0]
        y_pacman = node.state[1]
        x_house = self.goal[0]
        y_house = self.goal[1]
        return abs(x_pacman - x_house) + abs(y_pacman - y_house)


if __name__ == '__main__':
    """
     Потребно е со најмал број на чекори ПАКМАН да стигне од поцетната позиција дадена на сликата до 
     целта. Без притоа да застане на било кој пречка. Користи информирано пребарувње.

    """

    obstacles = [[0, 1], [1, 2], [3, 0], [3, 2], [3, 3]]
    gold_state = (0, 2)
    pacman = (0, 0)

    explorer = Search(obstacles, (pacman[0], pacman[1]), gold_state)

    result = astar_search(explorer)
    print(result.solution())




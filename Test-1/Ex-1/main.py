from searching_framework.utils import Problem
from searching_framework.uninformed_search import *
import bisect

"""
Дефинирање на класа за структурата на проблемот кој ќе го решаваме со пребарување.
Класата Problem е апстрактна класа од која правиме наследување за дефинирање на основните 
карактеристики на секој проблем што сакаме да го решиме
"""

def ProdolzhiPrvo(x, y, obstacles, nasoka):
    if nasoka == "istok" :
        if 0 <= x + 1 < 10 and [x + 1, y] not in obstacles:
            x += 1
        return x, y, nasoka

    if nasoka == "zapad":
        if 0 <= x-1 < 10 and [x-1, y] not in obstacles:
            x -= 1
        return x, y, nasoka

    if nasoka == "sever":
        if 0 <= y + 1 < 10 and [x, y+1] not in obstacles:
            y += 1
        return x, y, nasoka

    if nasoka == "jug":
        if 0 <= y-1 < 10 and [x, y-1] not in obstacles:
            y -= 1
        return x, y, nasoka

def ProdolzhiNazad(x,y,obstacles,nasoka):
    if nasoka == "istok":
        if 0 <= x - 1 < 10 and [x - 1, y ] not in obstacles:
            x -= 1
            nasoka = "zapad"
        return x, y, nasoka

    if nasoka == "zapad":
        if 0 <= x+1 < 10 and [x+1, y] not in obstacles:
            x += 1
            nasoka = "istok"
        return x, y, nasoka

    if nasoka == "sever":
        if 0 <= y-1 < 10 and [x, y-1] not in obstacles:
            y -= 1
            nasoka = "jug"
        return x, y, nasoka

    if nasoka == "jug":
        if 0<= y+1 <10 and [x, y+1] not in obstacles:
            y += 1
            nasoka = "sever"
        return x, y, nasoka

def SvrtiLevo(x,y,obstacles, nasoka):
    if nasoka == "istok":
        if 0 <= y+1 < 10 and [x , y+1] not in obstacles:
            y += 1
            nasoka = "sever"
        return x, y, nasoka

    if nasoka == "zapad":
        if 0 <= y - 1 < 10 and [x, y-1] not in obstacles:
            y -= 1
            nasoka = "jug"
        return x, y, nasoka

    if nasoka == "sever":
        if 0 <= x - 1 < 10 and [x-1, y] not in obstacles:
            x -= 1
            nasoka = "zapad"
        return x, y, nasoka

    if nasoka == "jug":
        if 0 <= x + 1 < 10 and [x+1, y] not in obstacles:
            x += 1
            nasoka = "istok"
        return x, y, nasoka


def SvrtiDesno(x, y, obstacles, nasoka):
    if nasoka == "istok":
        if 0 <= y - 1 < 10 and [x, y - 1] not in obstacles:
            y -= 1
            nasoka = "jug"
        return x, y, nasoka

    if nasoka == "zapad":
        if 0 <= y + 1 < 10 and [x, y + 1] not in obstacles:
            y += 1
            nasoka = "sever"
        return x, y, nasoka
    if nasoka == "sever":
        if 0 <= x + 1 < 10 and [x + 1, y] not in obstacles:
            x += 1
            nasoka = "istok"
        return x, y, nasoka

    if nasoka == "jug":
        if 0 <= x - 1 < 10 and [x - 1, y] not in obstacles:
            x -= 1
            nasoka = "zapad"
        return x, y, nasoka




class PacMan(Problem):
    def __init__(self, obstacles,initial, goal=None):
        self.initial = initial
        self.goal = goal
        self.obstacle = obstacles

    def successor(self, state):
        """За дадена состојба, врати речник од парови {акција : состојба}
        достапни од оваа состојба. Ако има многу следбеници, употребете
        итератор кој би ги генерирал следбениците еден по еден, наместо да
        ги генерирате сите одеднаш.
        :param state: дадена состојба
        :return:  речник од парови {акција : состојба} достапни од оваа
                  состојба
        :rtype: dict
        """

        successors = dict()

        pacman_x = state[0]
        pacman_y = state[1]

        nasoka = state[2]

        peleti = state[3]

        new_pacman_x, new_pacman_y, new_nasoka = ProdolzhiPrvo(pacman_x, pacman_y, self.obstacle, nasoka)
        if[pacman_x, pacman_y] != [new_pacman_x,new_pacman_y]:
            successors['ProdolzhiPravo'] = (new_pacman_x, new_pacman_y,new_nasoka,
                                            tuple([s for s in peleti if s[0] != new_pacman_x or s[1] != new_pacman_y]))

        new_pacman_x, new_pacman_y, new_nasoka = ProdolzhiNazad(pacman_x, pacman_y, self.obstacle, nasoka)
        if [pacman_x, pacman_y] != [new_pacman_x, new_pacman_y]:
            successors['ProdolzhiNazad'] = (new_pacman_x, new_pacman_y, new_nasoka,
                                            tuple([s for s in peleti if s[0] != new_pacman_x or s[1] != new_pacman_y]))

        new_pacman_x, new_pacman_y, new_nasoka = SvrtiLevo(pacman_x, pacman_y, self.obstacle, nasoka)
        if[pacman_x, pacman_y] != [new_pacman_x,new_pacman_y]:
            successors['SvrtiLevo'] = (new_pacman_x, new_pacman_y,new_nasoka,
                                            tuple([s for s in peleti if s[0] != new_pacman_x or s[1] != new_pacman_y]))

        new_pacman_x, new_pacman_y, new_nasoka = SvrtiDesno(pacman_x, pacman_y, self.obstacle, nasoka)
        if[pacman_x, pacman_y] != [new_pacman_x,new_pacman_y]:
            successors['SvrtiDesno'] = (new_pacman_x, new_pacman_y,new_nasoka,
                                            tuple([s for s in peleti if s[0] != new_pacman_x or s[1] != new_pacman_y]))


        return successors




    def actions(self, state):
        """За дадена состојба state, врати листа од сите акции што може да
        се применат над таа состојба
        :param state: дадена состојба
        :return: листа на акции
        :rtype: list
        """
        return self.successor(state).keys()

    def result(self, state, action):
        """За дадена состојба state и акција action, врати ја состојбата
        што се добива со примена на акцијата над состојбата
        :param state: дадена состојба
        :param action: дадена акција
        :return: резултантна состојба
        """
        return self.successor(state)[action]

    def goal_test(self, state):
        """Врати True ако state е целна состојба. Даденава имплементација
        на методот директно ја споредува state со self.goal, како што е
        специфицирана во конструкторот. Имплементирајте го овој метод ако
        проверката со една целна состојба self.goal не е доволна.
        :param state: дадена состојба
        :return: дали дадената состојба е целна состојба
        :rtype: bool
        """
        return len(state[-1]) == 0



if __name__ == "__main__":

    obstacles_list = [[0,6],[0,8],[0,9],[1,2],[1,3],[1,4],[1,9],[2,9],[3,6],[3,9],[4,1],[4,5]
                      ,[4,6],[4,7],[5,1],[5,6],[6,0],[6,1],[6,2],[6,9],[8,1],[8,4],[8,7],[8,8]
                      ,[9,4],[9,7],[9,8]]


    initial_state = []

    initial_state.append(int(input()))
    initial_state.append(int(input()))


    nasoka_pacman = input()
    br_peleti = int(input())
    peleti_pozicia = []
    tmp = []

    while br_peleti > 0:
        tmp = input().split(',')
        tmp[0] = int(tmp[0])
        tmp[1] = int(tmp[1])
        peleti_pozicia.append(tuple(tmp))
        br_peleti = br_peleti - 1

    peleti_pozicia = tuple(peleti_pozicia)

    pacman = PacMan(obstacles_list, (initial_state[0],initial_state[1], nasoka_pacman, peleti_pozicia))

    result = breadth_first_graph_search(pacman)
    print(result.solution())






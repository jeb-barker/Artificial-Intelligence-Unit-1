# Jeb Barker
# Sep. 25, 2020
import random
from collections import deque


def getInitialState():
    x = "_12345678"
    l = list(x)
    random.shuffle(l)
    y = ''.join(l)
    return y


'''precondition: i<j
   swap characters at position i and j and return the new state'''
def swap(state, i, j):
    li = list(state) # create a list of each character in state
    li[i], li[j] = li[j], li[i] # swap the elements of li at i/j
    return "".join(s for s in li) # join every element in li into a string


'''Generate a list which hold all children of the current state
   and return the list'''
def generate_children(state):
    sIndex = state.index("_") # store index of space (not necessary, just saves a little bit of space)

    return [swap(state, sIndex, j) for j, val in enumerate(list(state)) if not sIndex == j and (sIndex % 3 == j % 3 and abs(sIndex - j) <= 3) or ((sIndex - 1 == j and ((sIndex % 3) - 1 == j % 3)) or (sIndex + 1 == j and ((sIndex % 3) + 1 == j % 3)))]
    # Return state after swapping space/j for every index in the given state. The following conditions are in order in the line above.
    # Make sure the space and the index you are checking isn't the same
    # Check if the space and the index you are ckecking are in the same column (Mod 3 produces this), only if the space and j are less than 4 spaces apart.
    # Check of the character to the left/right of the space is in the same row using mod 3 +/- 1. E.X. space at index 2, j at index 3: 2%3 + 1 != 3%3.


def display_path(n, explored):  # key: current, value: parent
    l = []
    while explored[n] != "s":  # "s" is initial's parent
        l.append(n)
        n = explored[n]
    print()
    l = l[::-1]
    for i in l:
        print(i[0:3], end="   ")
    print()
    for j in l:
        print(j[3:6], end="   ")
    print()
    for k in l:
        print(k[6:9], end="   ")
    print("\n\nThe shortest path length is :", len(l))
    return ""


'''Find the shortest path to the goal state "_12345678" and
   returns the path by calling display_path() function to print all steps.
   You can make other helper methods, but you must use dictionary for explored.'''


def BFS(initial_state):
    explored = {initial_state:"s"}
    nodeQueue = [[initial_state]]
    while(True):
        if nodeQueue == []:
            return display_path(s, explored)
        path = nodeQueue.pop(0)
        try:
            explored[path[-1]] = s
        except UnboundLocalError:
            explored[path[-1]] = "s"
        s = path[-1]

        if s == "_12345678": display_path(s, explored)
        for state in generate_children(list(s)):
            if state not in nodeQueue and state not in list(explored):
                path.append(state)
                nodeQueue.append(path)
        # display_path(nodeQueue, explored)




'''Find the shortest path to the goal state "_12345678" and
   returns the path by calling display_path() function to print all steps.
   You can make other helper methods, but you must use dictionary for explored.'''


def DFS(initial):
    '''Your code goes here'''
    return ("No solution")


def main():

    initial = getInitialState()
    print(initial)
    #print(generate_children(initial)) # Test generate children
    print("BFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
    print(BFS(initial))
    print("DFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
    print(DFS(initial))


if __name__ == '__main__':
    main()